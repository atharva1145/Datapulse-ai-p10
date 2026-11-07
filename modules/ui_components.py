"""
Module: UI Components & Enterprise Executive Banners
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Provides high-end UI components, consistent enterprise app headers,
breadcrumb navigation, and status indicators across all pages.
"""

from typing import Optional
import streamlit as st
import pandas as pd


def render_page_header(
    page_title: str,
    module_tag: str,
    subtitle: str,
    current_page_name: Optional[str] = None
) -> None:
    """
    Renders an executive, Datadog/Linear-style enterprise app header on every page.
    Includes breadcrumbs, live engine indicator, active dataset pill, and student badge.
    """
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
