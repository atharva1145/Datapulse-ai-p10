"""
Module: UI Components, Enterprise Banners & Multi-Theme Controller
Subject: Generative AI (Continuous Assessment Problem P10)

Provides a clean, minimalist top app bar with Logo, Theme Switcher,
Screen Recorder modal dialog, and status indicators in the upper-right corner.
"""

from typing import Optional
import streamlit as st
from modules.screen_recorder import render_screen_recorder


def apply_theme() -> str:
    """
    Applies the active UI theme (Dark, Light, or System Default)
    and returns the active theme name ('dark' or 'light').
    """
    if "app_theme" not in st.session_state:
        st.session_state["app_theme"] = "Dark (Enterprise)"

    theme = st.session_state["app_theme"]

    if theme == "Light (Clean)":
        st.markdown("""
        <style>
        html, body, [class*="css"], .stApp {
            background-color: #F8FAFC !important;
            color: #0F172A !important;
        }
        .clean-top-bar {
            background: #FFFFFF !important;
            border-bottom: 1px solid #E2E8F0 !important;
        }
        .page-main-heading {
            color: #0F172A !important;
        }
        .metric-box {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        }
        .metric-num {
            color: #0F172A !important;
        }
        .metric-tag {
            color: #64748B !important;
        }
        .module-card {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
        }
        .module-title {
            color: #0F172A !important;
        }
        .module-desc {
            color: #475569 !important;
        }
        .stTabs [data-baseweb="tab-list"] {
            background-color: #F1F5F9 !important;
            border: 1px solid #E2E8F0 !important;
        }
        .stTabs [data-baseweb="tab"] {
            color: #475569 !important;
        }
        .stTabs [aria-selected="true"] {
            background-color: #FFFFFF !important;
            color: #0F172A !important;
            border: 1px solid #CBD5E1 !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        }
        section[data-testid="stSidebar"] {
            background-color: #F8FAFC !important;
            border-right: 1px solid #E2E8F0 !important;
        }
        section[data-testid="stSidebar"] * {
            color: #0F172A !important;
        }
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background-color: #FFFFFF !important;
            border: 1px solid #CBD5E1 !important;
            color: #0F172A !important;
        }
        div[data-testid="stAlert"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
        }
        div[data-testid="stDataFrame"] {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
        }
        </style>
        """, unsafe_allow_html=True)
        return "light"

    elif theme == "System Default":
        st.markdown("""
        <style>
        @media (prefers-color-scheme: light) {
            html, body, [class*="css"], .stApp {
                background-color: #F8FAFC !important;
                color: #0F172A !important;
            }
            .metric-box, .module-card, div[data-testid="stDataFrame"], div[data-testid="stAlert"] {
                background: #FFFFFF !important;
                border-color: #E2E8F0 !important;
            }
            .metric-tag, .page-main-subtext, .module-desc {
                color: #475569 !important;
            }
            section[data-testid="stSidebar"] {
                background-color: #F8FAFC !important;
                border-right-color: #E2E8F0 !important;
            }
            section[data-testid="stSidebar"] * {
                color: #0F172A !important;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        return "system"

    return "dark"


@st.dialog("📹 Demo Video Screen Recorder Studio", width="large")
def open_recorder_dialog():
    """Modal dialog displaying the HTML5 screen recorder and script teleprompter."""
    st.caption("Record your browser screen, tab audio, and microphone directly. Once stopped, download your demo video file.")
    render_screen_recorder(theme=st.session_state.get("app_theme", "Dark"))


def render_page_header(
    page_title: str,
    module_tag: str = "",
    subtitle: str = ""
) -> None:
    """
    Renders a clean, minimalist top bar.
    - Left: Logo + Platform Name + Breadcrumb
    - Middle: Ingested Dataset Pill
    - Right Upside Corner: Theme Selector (Dark/Light/System) & Record Demo Button
    """
    apply_theme()

    # Upper Bar: Logo on Left, Theme & Record on Upper Right Corner
    top_col_brand, top_col_dataset, top_col_rec, top_col_theme = st.columns(
        [4.2, 3.2, 1.3, 1.3],
        vertical_alignment="center"
    )

    with top_col_brand:
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 1.3rem;">📊</span>
            <span style="font-size: 1.05rem; font-weight: 800; letter-spacing: -0.02em;">CSV INSIGHT AI</span>
            <span style="color: #64748B; font-size: 0.85rem;">/</span>
            <span style="font-size: 0.88rem; font-weight: 600; color: #818CF8;">{page_title}</span>
        </div>
        """, unsafe_allow_html=True)

    with top_col_dataset:
        active_dataset = st.session_state.get("dataset_name", None)
        df = st.session_state.get("df", None)
        if df is not None:
            st.markdown(f"""
            <div style="background: rgba(6, 182, 212, 0.1); border: 1px solid rgba(6, 182, 212, 0.3); border-radius: 6px; padding: 4px 10px; font-size: 0.76rem; color: #38BDF8; font-weight: 600; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                📁 {active_dataset} ({len(df):,} × {len(df.columns)})
            </div>
            """, unsafe_allow_html=True)

    # Upper Right Corner: Record Demo Button
    with top_col_rec:
        safe_key_rec = f"rec_{page_title.lower().replace(' ', '_')}"
        if st.button("🔴 Record", key=safe_key_rec, use_container_width=True, help="Record 2-3 minute demo video"):
            open_recorder_dialog()

    # Upper Right Corner: Theme Dropdown
    with top_col_theme:
        theme_map = {
            "🌙 Dark": "Dark (Enterprise)",
            "☀️ Light": "Light (Clean)",
            "💻 System": "System Default"
        }
        reverse_map = {
            "Dark (Enterprise)": "🌙 Dark",
            "Light (Clean)": "☀️ Light",
            "System Default": "💻 System"
        }
        curr_theme = st.session_state.get("app_theme", "Dark (Enterprise)")
        safe_key_theme = f"theme_{page_title.lower().replace(' ', '_')}"
        
        chosen = st.selectbox(
            "Theme",
            ["🌙 Dark", "☀️ Light", "💻 System"],
            index=["🌙 Dark", "☀️ Light", "💻 System"].index(reverse_map.get(curr_theme, "🌙 Dark")),
            key=safe_key_theme,
            label_visibility="collapsed"
        )
        if theme_map[chosen] != curr_theme:
            st.session_state["app_theme"] = theme_map[chosen]
            st.rerun()

    # Optional subtext for context
    if subtitle:
        st.markdown(f"<div style='font-size: 0.82rem; color: #94A3B8; margin-top: 2px; margin-bottom: 12px;'>{subtitle}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)


def render_empty_state_warning() -> None:
    """Renders a simple warning when no dataset has been ingested yet."""
    st.markdown("""
    <div class="empty-state-card">
        <div style="font-size: 2rem; margin-bottom: 6px;">📂</div>
        <div style="font-size: 1.1rem; font-weight: 700; color: #F8FAFC; margin-bottom: 4px;">
            No CSV Dataset Currently Ingested
        </div>
        <div style="font-size: 0.85rem; color: #94A3B8; max-width: 480px; margin: 0 auto 12px auto;">
            Please select an official benchmark dataset (Iris, Titanic, Wine) in the sidebar or upload your own CSV file.
        </div>
    </div>
    """, unsafe_allow_html=True)
