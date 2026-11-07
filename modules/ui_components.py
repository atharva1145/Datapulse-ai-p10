"""
Module: UI Components, Enterprise Banners & Multi-Theme Controller
Subject: Generative AI (Continuous Assessment Problem P10)

Provides a clean, minimalist top app bar with Logo, Dataset Indicator,
and a 3-Dots (⋮) Action Popover in the upper-right corner housing
Theme Switching (Dark/Light/System) and Screen Recording.
"""

from typing import Optional
from pathlib import Path
import streamlit as st
from modules.screen_recorder import render_screen_recorder


def get_logo_html(size: int = 28) -> str:
    """Returns an inline SVG logo HTML string for DataPulse AI."""
    svg_path = Path(__file__).resolve().parent.parent / "assets" / "logo.svg"
    if svg_path.exists():
        try:
            with open(svg_path, "r", encoding="utf-8") as f:
                svg = f.read()
                svg_sized = svg.replace('width="120"', f'width="{size}"').replace('height="120"', f'height="{size}"')
                return f'<div style="width: {size}px; height: {size}px; display: inline-flex; align-items: center; justify-content: center; flex-shrink: 0;">{svg_sized}</div>'
        except Exception:
            pass
    return '<span style="font-size: 1.25rem;">📊</span>'


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
        :root {
            --bg-base: #F8FAFC !important;
            --bg-surface: #FFFFFF !important;
            --bg-surface-elevated: #F1F5F9 !important;
            --bg-surface-hover: #E2E8F0 !important;
            --border-subtle: #E2E8F0 !important;
            --border-medium: #CBD5E1 !important;
            --border-accent: #6366F1 !important;
            --text-primary: #0F172A !important;
            --text-secondary: #475569 !important;
            --text-tertiary: #64748B !important;
            --sidebar-bg: #FFFFFF !important;
            --sidebar-card-bg: #F8FAFC !important;
            --sidebar-card-border: #E2E8F0 !important;
            --sidebar-text: #0F172A !important;
            --sidebar-text-muted: #64748B !important;
            --hero-bg: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 100%) !important;
            --hero-border: #C7D2FE !important;
            --health-bg: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 100%) !important;
            --health-border: #C7D2FE !important;
            --health-title-color: #4338CA !important;
            --health-val-gradient: linear-gradient(180deg, #1E1B4B 0%, #4F46E5 100%) !important;
            --terminal-bg: #F8FAFC !important;
            --terminal-header-bg: #F1F5F9 !important;
            --popover-bg: #FFFFFF !important;
            --popover-border: #CBD5E1 !important;
            --popover-btn-bg: #FFFFFF !important;
            --popover-btn-border: #CBD5E1 !important;
            --popover-btn-color: #0F172A !important;
        }

        html, body, .stApp, [data-testid="stAppViewContainer"] {
            background-color: #F8FAFC !important;
            color: #0F172A !important;
        }

        /* Typography high contrast */
        .stMarkdownContainer p, h1, h2, h3, h4, h5, h6, label {
            color: #0F172A !important;
        }

        /* Sidebar Light Styling */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0 !important;
        }
        section[data-testid="stSidebar"] a {
            color: #1E293B !important;
            font-weight: 500 !important;
            transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1) !important;
        }
        section[data-testid="stSidebar"] a:hover {
            background-color: #F1F5F9 !important;
            color: #4F46E5 !important;
            transform: translateX(4px) !important;
        }
        section[data-testid="stSidebar"] a[aria-current="page"] {
            background-color: #EEF2FF !important;
            color: #4F46E5 !important;
            font-weight: 700 !important;
            border-left: 3px solid #6366F1 !important;
        }
        section[data-testid="stSidebar"] a * {
            color: inherit !important;
        }
        section[data-testid="stSidebar"] .stMarkdownContainer p,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] label *,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] div[role="radiogroup"] label,
        section[data-testid="stSidebar"] div[role="radiogroup"] label *,
        section[data-testid="stSidebar"] .stSelectbox label,
        section[data-testid="stSidebar"] .stSelectbox label * {
            color: #1E293B !important;
            font-weight: 600 !important;
        }
        section[data-testid="stSidebar"] button[kind="secondary"] {
            background-color: #F8FAFC !important;
            border: 1px solid #CBD5E1 !important;
            color: #0F172A !important;
        }
        section[data-testid="stSidebar"] button[kind="secondary"]:hover {
            background-color: #EEF2FF !important;
            border-color: #6366F1 !important;
            color: #4F46E5 !important;
        }
        section[data-testid="stSidebar"] .sidebar-brand-card {
            background: #F8FAFC !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
        }
        section[data-testid="stSidebar"] .sidebar-brand-card * {
            color: #0F172A !important;
        }
        section[data-testid="stSidebar"] .sidebar-status-box {
            background: #F8FAFC !important;
            border: 1px solid #E2E8F0 !important;
            border-left: 3px solid #10B981 !important;
        }
        section[data-testid="stSidebar"] .sidebar-status-box * {
            color: #0F172A !important;
        }

        /* Tables & Data in Light Mode */
        div[data-testid="stTable"],
        div[data-testid="stTable"] table,
        div[data-testid="stTable"] tbody,
        div[data-testid="stTable"] tr,
        div[data-testid="stTable"] th,
        div[data-testid="stTable"] td,
        div[data-testid="stTable"] * {
            color: #0F172A !important;
            background-color: #FFFFFF !important;
        }
        div[data-testid="stTable"] th {
            background-color: #F1F5F9 !important;
            color: #0F172A !important;
            border-bottom: 2px solid #CBD5E1 !important;
            font-weight: 700 !important;
        }
        div[data-testid="stTable"] td {
            border-bottom: 1px solid #E2E8F0 !important;
            color: #1E293B !important;
        }

        /* Hero Executive Card in Light Mode */
        .hero-executive-card {
            background: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 100%) !important;
            border: 1px solid #C7D2FE !important;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.08) !important;
        }
        .hero-executive-title {
            color: #0F172A !important;
        }
        .hero-executive-subtitle {
            color: #475569 !important;
        }
        .hero-stats-row {
            border-top: 1px solid #E2E8F0 !important;
        }
        .hero-stat-item {
            color: #475569 !important;
        }
        .hero-stat-item strong {
            color: #4F46E5 !important;
        }

        /* Module Cards in Light Mode */
        .module-card {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 1px 4px rgba(0,0,0,0.04) !important;
        }
        .module-card:hover {
            border-color: #6366F1 !important;
            box-shadow: 0 8px 16px -2px rgba(99, 102, 241, 0.12) !important;
        }
        .module-title {
            color: #0F172A !important;
        }
        .module-desc {
            color: #475569 !important;
        }
        .module-tag-badge {
            background: #EEF2FF !important;
            border: 1px solid #C7D2FE !important;
            color: #4F46E5 !important;
        }

        /* Metric Boxes in Light Mode */
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

        /* Health Score Container in Light Mode */
        .health-score-container {
            background: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 100%) !important;
            border: 1px solid #C7D2FE !important;
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.08) !important;
        }
        .health-score-title {
            color: #4338CA !important;
        }
        .health-score-value {
            background: linear-gradient(180deg, #1E1B4B 0%, #4F46E5 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
        }

        /* Empty State Card in Light Mode */
        .empty-state-card {
            background: #FFFFFF !important;
            border: 1px dashed #CBD5E1 !important;
        }

        /* Terminal Window in Light Mode */
        .terminal-window {
            background: #F8FAFC !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
        }
        .terminal-header {
            background: #F1F5F9 !important;
            border-bottom: 1px solid #E2E8F0 !important;
        }
        .terminal-title {
            color: #475569 !important;
        }
        .terminal-body {
            color: #0F172A !important;
        }

        /* Tabs in Light Mode */
        .stTabs [data-baseweb="tab-list"] {
            background-color: #F1F5F9 !important;
            border: 1px solid #E2E8F0 !important;
        }
        .stTabs [data-baseweb="tab"] {
            color: #64748B !important;
        }
        .stTabs [aria-selected="true"] {
            background-color: #FFFFFF !important;
            color: #0F172A !important;
            border: 1px solid #CBD5E1 !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06) !important;
        }

        /* Data Tables & Expanders in Light Mode */
        div[data-testid="stDataFrame"] {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
        }
        div[data-testid="stExpander"] {
            background-color: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
        }
        div[data-testid="stExpander"] summary {
            color: #0F172A !important;
        }

        /* Form Controls in Light Mode */
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background-color: #FFFFFF !important;
            border: 1px solid #CBD5E1 !important;
            color: #0F172A !important;
        }
        div[data-baseweb="select"] * {
            color: #0F172A !important;
        }
        button[kind="secondary"] {
            background: #F1F5F9 !important;
            border: 1px solid #CBD5E1 !important;
            color: #0F172A !important;
        }
        button[kind="secondary"]:hover {
            background: #E2E8F0 !important;
            border-color: #6366F1 !important;
            color: #6366F1 !important;
        }

        /* Popover Button & Body in Light Mode */
        button[data-testid="stPopoverButton"],
        div[data-testid="stPopover"] button {
            background: #FFFFFF !important;
            border: 1px solid #CBD5E1 !important;
            color: #0F172A !important;
            box-shadow: 0 1px 4px rgba(0,0,0,0.08) !important;
        }
        button[data-testid="stPopoverButton"]:hover,
        div[data-testid="stPopover"] button:hover {
            background: #F1F5F9 !important;
            border-color: #6366F1 !important;
            color: #6366F1 !important;
        }
        div[data-testid="stPopoverBody"] {
            background: #FFFFFF !important;
            border: 1px solid #CBD5E1 !important;
            color: #0F172A !important;
            box-shadow: 0 16px 36px -4px rgba(0, 0, 0, 0.15) !important;
            animation: popoverSlideIn 0.2s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
        }
        div[data-testid="stPopoverBody"] * {
            color: #0F172A !important;
        }

        /* Alert Boxes in Light Mode */
        div[data-testid="stAlert"] {
            background-color: #F8FAFC !important;
            border: 1px solid #E2E8F0 !important;
        }
        div[data-testid="stAlert"] * {
            color: #0F172A !important;
        }
        </style>
        """, unsafe_allow_html=True)
        return "light"

    elif theme == "System Default":
        st.markdown("""
        <style>
        @media (prefers-color-scheme: light) {
            :root {
                --bg-base: #F8FAFC !important;
                --bg-surface: #FFFFFF !important;
                --bg-surface-elevated: #F1F5F9 !important;
                --border-subtle: #E2E8F0 !important;
                --border-medium: #CBD5E1 !important;
                --text-primary: #0F172A !important;
                --text-secondary: #475569 !important;
                --text-tertiary: #64748B !important;
                --sidebar-bg: #FFFFFF !important;
                --sidebar-card-bg: #F8FAFC !important;
                --hero-bg: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 100%) !important;
                --health-bg: linear-gradient(135deg, #EEF2FF 0%, #F8FAFC 100%) !important;
            }
            html, body, .stApp, [data-testid="stAppViewContainer"] {
                background-color: #F8FAFC !important;
                color: #0F172A !important;
            }
            .stMarkdownContainer p, h1, h2, h3, h4, label {
                color: #0F172A !important;
            }
            .metric-box, .module-card, div[data-testid="stDataFrame"], div[data-testid="stAlert"] {
                background: #FFFFFF !important;
                border-color: #E2E8F0 !important;
            }
            .metric-num, .module-title {
                color: #0F172A !important;
            }
            .metric-tag, .module-desc {
                color: #475569 !important;
            }
            section[data-testid="stSidebar"] {
                background-color: #FFFFFF !important;
                border-right-color: #E2E8F0 !important;
            }
            section[data-testid="stSidebar"] .stMarkdownContainer p,
            section[data-testid="stSidebar"] label {
                color: #1E293B !important;
            }
        }
        </style>
        """, unsafe_allow_html=True)
        return "system"

    return "dark"


@st.dialog("📹 Screen Recorder Studio", width="large")
def open_recorder_dialog():
    """Modal dialog displaying the HTML5 screen recorder and script teleprompter."""
    st.caption("Record your browser screen, tab audio, and microphone directly. Once stopped, download your recorded video file.")
    render_screen_recorder(theme=st.session_state.get("app_theme", "Dark"))


def render_page_header(
    page_title: str,
    module_tag: str = "",
    subtitle: str = ""
) -> None:
    """
    Renders a clean, minimalist top bar.
    - Left: Logo + Platform Name + Breadcrumb
    - Middle: Ingested Dataset Pill with active target
    - Upper Right Corner: 3-Dots (⋮) Action Popover hiding Theme & Screen Recording
    """
    apply_theme()

    top_col_brand, top_col_dataset, top_col_menu = st.columns(
        [5.5, 4.3, 0.2],
        vertical_alignment="center"
    )

    logo_icon = get_logo_html(size=28)
    logo_popover = get_logo_html(size=22)

    with top_col_brand:
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 10px;">
            {logo_icon}
            <span style="font-size: 1.05rem; font-weight: 800; letter-spacing: -0.02em;">DataPulse AI</span>
            <span style="color: #64748B; font-size: 0.85rem;">/</span>
            <span style="font-size: 0.88rem; font-weight: 600; color: #818CF8;">{page_title}</span>
        </div>
        """, unsafe_allow_html=True)

    with top_col_dataset:
        active_dataset = st.session_state.get("dataset_name", None)
        df = st.session_state.get("df", None)
        target = st.session_state.get("target_column", None)
        if df is not None:
            target_str = f" • 🎯 {target}" if target else ""
            st.markdown(f"""
            <div style="background: rgba(6, 182, 212, 0.1); border: 1px solid rgba(6, 182, 212, 0.3); border-radius: 6px; padding: 4px 10px; font-size: 0.76rem; color: #38BDF8; font-weight: 600; text-align: center; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
                📁 {active_dataset} ({len(df):,} × {len(df.columns)}){target_str}
            </div>
            """, unsafe_allow_html=True)

    # Upper Right Corner: 3-Dots (⋮) Menu Button
    with top_col_menu:
        safe_key_suffix = page_title.lower().replace(' ', '_').replace('/', '_')
        with st.popover("⋮", help="Settings, Theme & Screen Recording"):
            st.markdown(f"""
            <div style="font-weight: 800; font-size: 0.95rem; display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                {logo_popover}
                <span>DataPulse AI</span>
                <span style="font-size: 0.7rem; background: rgba(99,102,241,0.2); color: #818CF8; padding: 2px 6px; border-radius: 4px;">v2.4</span>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='font-size: 0.76rem; font-weight: 700; color: #94A3B8; margin-top: 6px; margin-bottom: 2px;'>🎨 Interface Theme</div>", unsafe_allow_html=True)
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
            chosen = st.radio(
                "Interface Theme",
                ["🌙 Dark", "☀️ Light", "💻 System"],
                index=["🌙 Dark", "☀️ Light", "💻 System"].index(reverse_map.get(curr_theme, "🌙 Dark")),
                key=f"pop_theme_{safe_key_suffix}",
                label_visibility="collapsed"
            )
            if theme_map[chosen] != curr_theme:
                st.session_state["app_theme"] = theme_map[chosen]
                st.rerun()

            st.markdown("<div style='font-size: 0.76rem; font-weight: 700; color: #94A3B8; margin-top: 10px; margin-bottom: 4px;'>📹 Screen Recording</div>", unsafe_allow_html=True)
            if st.button("🔴 Record Video", key=f"pop_rec_{safe_key_suffix}", use_container_width=True):
                open_recorder_dialog()

            st.markdown("<div style='font-size: 0.7rem; color: #64748B; margin-top: 10px; text-align: center;'>Problem P10 Continuous Assessment</div>", unsafe_allow_html=True)

    if subtitle:
        st.markdown(f"<div style='font-size: 0.82rem; color: #94A3B8; margin-top: 2px; margin-bottom: 12px;'>{subtitle}</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)


def render_empty_state_warning() -> None:
    """Renders a simple warning when no dataset has been ingested yet."""
    st.markdown("""
    <div class="empty-state-card">
        <div style="font-size: 2rem; margin-bottom: 6px;">📂</div>
        <div style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary, #F8FAFC); margin-bottom: 4px;">
            No CSV Dataset Currently Ingested
        </div>
        <div style="font-size: 0.85rem; color: var(--text-secondary, #94A3B8); max-width: 480px; margin: 0 auto 12px auto;">
            Please select an official benchmark dataset (Iris, Titanic, Wine) in the sidebar or upload your own CSV file.
        </div>
    </div>
    """, unsafe_allow_html=True)
