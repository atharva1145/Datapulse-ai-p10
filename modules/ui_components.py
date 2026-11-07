"""
Module: UI Components, Enterprise Banners & Multi-Theme Controller
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Provides consistent executive app headers, multi-theme switching (System / Light / Dark),
breadcrumb navigation, and status indicators across all application pages.
"""

from typing import Optional
import streamlit as st


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
        .enterprise-app-bar {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 2px 6px rgba(0,0,0,0.04) !important;
        }
        .brand-title {
            color: #0F172A !important;
        }
        .brand-badge {
            background: #EEF2FF !important;
            border: 1px solid #C7D2FE !important;
            color: #4F46E5 !important;
        }
        .brand-breadcrumb-page {
            color: #475569 !important;
        }
        .meta-chip {
            background: #F1F5F9 !important;
            border: 1px solid #E2E8F0 !important;
            color: #334155 !important;
        }
        .meta-chip-dataset.active {
            background: #ECFEFF !important;
            border-color: #A5F3FC !important;
            color: #0891B2 !important;
        }
        .student-chip {
            background: #EEF2FF !important;
            border-color: #C7D2FE !important;
        }
        .page-main-heading {
            color: #0F172A !important;
        }
        .page-main-subtext {
            color: #475569 !important;
        }
        .module-pill-badge {
            background: #EEF2FF !important;
            border: 1px solid #C7D2FE !important;
            color: #4338CA !important;
        }
        .metric-box {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        }
        .metric-box:hover {
            border-color: #4F46E5 !important;
            box-shadow: 0 6px 16px rgba(79, 70, 229, 0.1) !important;
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
        .module-card:hover {
            border-color: #4F46E5 !important;
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
            color: #4338CA !important;
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
        .sidebar-brand-card {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
        }
        .sidebar-status-box {
            background: #FFFFFF !important;
            border: 1px solid #E2E8F0 !important;
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
        # System mode uses CSS media queries to respect OS preference
        st.markdown("""
        <style>
        @media (prefers-color-scheme: light) {
            html, body, [class*="css"], .stApp {
                background-color: #F8FAFC !important;
                color: #0F172A !important;
            }
            .enterprise-app-bar {
                background: #FFFFFF !important;
                border: 1px solid #E2E8F0 !important;
            }
            .brand-title, .page-main-heading, .metric-num, .module-title {
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

    # Default is Dark (Enterprise)
    return "dark"


def render_theme_selector(in_sidebar: bool = True) -> None:
    """Renders a clean dropdown to switch between Dark, Light, and System themes."""
    if "app_theme" not in st.session_state:
        st.session_state["app_theme"] = "Dark (Enterprise)"

    theme_options = ["Dark (Enterprise)", "Light (Clean)", "System Default"]
    current_idx = theme_options.index(st.session_state["app_theme"]) if st.session_state["app_theme"] in theme_options else 0

    if in_sidebar:
        with st.sidebar:
            st.markdown("<div style='font-size: 0.76rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.06em; margin-top: 14px; margin-bottom: 4px;'>Interface Theme</div>", unsafe_allow_html=True)
            chosen = st.selectbox(
                "Interface Theme:",
                theme_options,
                index=current_idx,
                label_visibility="collapsed",
                key="theme_selector_dropdown"
            )
            if chosen != st.session_state["app_theme"]:
                st.session_state["app_theme"] = chosen
                st.rerun()


def render_page_header(
    page_title: str,
    module_tag: str,
    subtitle: str,
    current_page_name: Optional[str] = None
) -> None:
    """
    Renders an executive, Datadog/Linear-style enterprise app header on every page.
    Includes theme applicator, breadcrumbs, live engine indicator, active dataset pill, and student badge.
    """
    # Apply theme dynamically and render theme selector in sidebar
    apply_theme()
    render_theme_selector(in_sidebar=True)

    active_dataset = st.session_state.get("dataset_name", "No Dataset Loaded")
    df = st.session_state.get("df", None)
    
    if df is not None:
        dataset_meta_str = f"📊 {active_dataset} ({len(df):,} × {len(df.columns)})"
        dataset_pill_class = "meta-chip-dataset active"
    else:
        dataset_meta_str = "⚠️ No Dataset Loaded"
        dataset_pill_class = "meta-chip-dataset warning"

    st.markdown(f"""
    <div class="enterprise-app-bar">
        <div class="brand-section">
            <span class="brand-badge">P10</span>
            <span class="brand-title">CSV INSIGHT AI</span>
            <span class="brand-breadcrumb-separator">/</span>
            <span class="brand-breadcrumb-page">{page_title}</span>
        </div>
        <div class="meta-chips-group">
            <div class="meta-chip {dataset_pill_class}">
                {dataset_meta_str}
            </div>
            <div class="meta-chip">
                <div class="status-dot-active"></div>
                <span>Engine Online</span>
            </div>
            <div class="meta-chip student-chip">
                <span style="color: #818CF8;">Atharva Shelar</span> [10]
            </div>
        </div>
    </div>
    
    <div class="page-subheader-container">
        <div class="page-title-row">
            <h1 class="page-main-heading">{page_title}</h1>
            <span class="module-pill-badge">{module_tag}</span>
        </div>
        <p class="page-main-subtext">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


def render_empty_state_warning() -> None:
    """Renders a sleek warning when no dataset has been ingested yet."""
    st.markdown("""
    <div class="empty-state-card">
        <div style="font-size: 2.2rem; margin-bottom: 8px;">📂</div>
        <div style="font-size: 1.15rem; font-weight: 700; color: #F8FAFC; margin-bottom: 6px;">
            No CSV Dataset Currently Ingested
        </div>
        <div style="font-size: 0.88rem; color: #94A3B8; max-width: 500px; margin: 0 auto 16px auto;">
            Please open the sidebar on the left or return to the <b>Home</b> page to select an official benchmark dataset (Iris, Titanic, Wine) or upload your own CSV file.
        </div>
    </div>
    """, unsafe_allow_html=True)
