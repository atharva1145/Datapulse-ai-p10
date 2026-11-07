"""
CSV INSIGHT AI - Enterprise Application Entrypoint
Student: Atharva Shelar | Roll No: 10
Course: Generative AI | Academic Problem: P10
"""

import sys
from pathlib import Path
import streamlit as st
import pandas as pd

# Add root directory to python path for modular imports
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from config.settings import (
    APP_NAME,
    APP_SUBTITLE,
    STUDENT_NAME,
    ROLL_NUMBER,
    COURSE_NAME,
    SAMPLE_DATASETS,
    SAMPLE_DATA_DIR,
    MAX_UPLOAD_SIZE_MB
)
from modules.data_loader import load_csv
from modules.ui_components import render_page_header, get_logo_html

# Configure page layout and metadata
st.set_page_config(
    page_title=f"{APP_NAME} - Enterprise AI Platform",
    page_icon=str(ROOT_DIR / "assets" / "favicon.png"),
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
css_path = ROOT_DIR / "assets" / "styles.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize Session State
if "df" not in st.session_state:
    st.session_state["df"] = None
if "metadata" not in st.session_state:
    st.session_state["metadata"] = None
if "dataset_name" not in st.session_state:
    st.session_state["dataset_name"] = None
if "target_column" not in st.session_state:
    st.session_state["target_column"] = None
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "synthetic_df" not in st.session_state:
    st.session_state["synthetic_df"] = None
if "ctgan_metrics" not in st.session_state:
    st.session_state["ctgan_metrics"] = None

# If no dataset loaded, load Iris by default so the dashboard is immediately interactive
if st.session_state["df"] is None:
    iris_path = SAMPLE_DATA_DIR / "iris.csv"
    if iris_path.exists():
        df_init, meta_init, _ = load_csv(iris_path)
        if df_init is not None:
            st.session_state["df"] = df_init
            st.session_state["metadata"] = meta_init
            st.session_state["dataset_name"] = "Iris Flower Dataset"
            st.session_state["target_column"] = "species"

# ==============================================================================
# SIDEBAR: Dataset Upload & Information Panel (Enterprise Dark)
# ==============================================================================
with st.sidebar:
    st.markdown(f"""
    <div class="sidebar-brand-card" style="display: flex; align-items: center; gap: 12px;">
        {get_logo_html(size=38)}
        <div style="flex: 1; min-width: 0;">
            <div style="font-size: 1.15rem; font-weight: 800; color: #FFFFFF; letter-spacing: -0.02em; line-height: 1.2;">
                {APP_NAME}
            </div>
            <div style="font-size: 0.72rem; color: #38BDF8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-top: 3px;">
                Autonomous ML Engine
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='font-size: 0.8rem; font-weight: 700; color: #94A3B8; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px;'>Dataset Ingestion</div>", unsafe_allow_html=True)
    data_source = st.radio(
        "Ingestion Source:",
        ["Public Benchmark Dataset", "Custom CSV Upload"],
        index=0,
        label_visibility="collapsed"
    )

    if data_source == "Public Benchmark Dataset":
        selected_sample = st.selectbox(
            "Select Benchmark:",
            list(SAMPLE_DATASETS.keys()),
            index=0
        )
        sample_info = SAMPLE_DATASETS[selected_sample]
        st.markdown(f"<div style='font-size: 0.74rem; color: #94A3B8; margin-top: -8px; margin-bottom: 12px;'>Task: <span style='color: #38BDF8; font-weight: 600;'>{sample_info['task_type']}</span></div>", unsafe_allow_html=True)
        
        if st.button("Load Benchmark Dataset", use_container_width=True, type="primary"):
            sample_path = SAMPLE_DATA_DIR / sample_info["filename"]
            df, meta, err = load_csv(sample_path)
            if err:
                st.error(err)
            else:
                st.session_state["df"] = df
                st.session_state["metadata"] = meta
                st.session_state["dataset_name"] = selected_sample
                st.session_state["target_column"] = meta["columns"][-1]
                st.rerun()

    else:
        uploaded_file = st.file_uploader(
            "Upload CSV File:",
            type=["csv"],
            help=f"Upload a CSV dataset up to {MAX_UPLOAD_SIZE_MB}MB."
        )
        col_delim, col_enc = st.columns(2)
        with col_delim:
            delimiter = st.selectbox("Delimiter:", ["auto", ",", ";", "\t", "|"], index=0)
        with col_enc:
            encoding = st.selectbox("Encoding:", ["utf-8", "latin1", "cp1252"], index=0)

        if uploaded_file is not None:
            if st.button("Process CSV File", use_container_width=True, type="primary"):
                df, meta, err = load_csv(
                    uploaded_file,
                    delimiter=None if delimiter == "auto" else delimiter,
                    encoding=encoding,
                    max_size_mb=MAX_UPLOAD_SIZE_MB
                )
                if err:
                    st.error(err)
                else:
                    st.session_state["df"] = df
                    st.session_state["metadata"] = meta
                    st.session_state["dataset_name"] = meta["filename"]
                    st.session_state["target_column"] = meta["columns"][-1]
                    st.rerun()

    # Active Dataset Status Box
    if st.session_state["df"] is not None:
        st.markdown(f"""
        <div class="sidebar-status-box">
            <div style="font-weight: 700; color: #F8FAFC; display: flex; align-items: center; justify-content: space-between;">
                <span>ACTIVE DATASET</span>
                <span style="display: flex; align-items: center; gap: 4px; color: #10B981; font-size: 0.7rem;">
                    <span class="status-dot-active"></span> READY
                </span>
            </div>
            <div style="font-size: 0.85rem; color: #38BDF8; font-weight: 600; margin-top: 4px;">{st.session_state['dataset_name']}</div>
            <div style="font-size: 0.75rem; color: #94A3B8; margin-top: 2px;">
                {len(st.session_state['df']):,} rows • {len(st.session_state['df'].columns)} features
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# MAIN PAGE: ENTERPRISE TOP APP BAR & HERO SECTION
# ==============================================================================
render_page_header(
    page_title="Platform Ingestion & Overview",
    module_tag="CORE PLATFORM",
    subtitle="Continuous Assessment P10 | Autonomous CSV Profiling, ML Task Recommendation & AI Analytics"
)

# 1-Click Fast Dataset Switcher
col_btn1, col_btn2, col_btn3 = st.columns(3)
with col_btn1:
    if st.button("🌸 Load Iris (Multiclass)", use_container_width=True):
        df_i, meta_i, _ = load_csv(SAMPLE_DATA_DIR / "iris.csv")
        st.session_state["df"] = df_i
        st.session_state["metadata"] = meta_i
        st.session_state["dataset_name"] = "Iris Flower Dataset"
        st.session_state["target_column"] = "species"
        st.toast("✅ Ingested Iris Dataset (150 rows × 5 features)")
        st.rerun()

with col_btn2:
    if st.button("🚢 Load Titanic (Binary / Imbalance)", use_container_width=True):
        df_t, meta_t, _ = load_csv(SAMPLE_DATA_DIR / "titanic.csv")
        st.session_state["df"] = df_t
        st.session_state["metadata"] = meta_t
        st.session_state["dataset_name"] = "Titanic Survival Dataset"
        st.session_state["target_column"] = "Survived"
        st.toast("✅ Ingested Titanic Dataset (891 rows × 12 features)")
        st.rerun()

with col_btn3:
    if st.button("🍷 Load Wine Quality (Regression)", use_container_width=True):
        df_w, meta_w, _ = load_csv(SAMPLE_DATA_DIR / "winequality_red.csv")
        st.session_state["df"] = df_w
        st.session_state["metadata"] = meta_w
        st.session_state["dataset_name"] = "Wine Quality Dataset"
        st.session_state["target_column"] = "quality"
        st.toast("✅ Ingested Wine Quality Dataset (1,599 rows × 12 features)")
        st.rerun()

st.markdown(f"""
<div class="hero-executive-card">
    <div class="hero-executive-title">Autonomous Tabular Intelligence &amp; ML Recommender</div>
    <div class="hero-executive-subtitle">
        Upload or select any CSV dataset to instantly generate statistical health profiles, optimal ML algorithms, 
        natural-language query synthesis with AST security guardrails, Sentence-BERT semantic column embeddings, 
        and PyTorch CTGAN synthetic tabular data.
    </div>
    <div class="hero-stats-row">
        <div class="hero-stat-item">Paradigm: <strong>Generative &amp; Discriminative AI</strong></div>
        <div class="hero-stat-item">Project Code: <strong>Problem P10</strong></div>
        <div class="hero-stat-item">Engine: <strong>Gemini 2.5 + PyTorch CTGAN</strong></div>
    </div>
</div>
""", unsafe_allow_html=True)

# Enterprise Feature Navigation Grid
st.markdown("<div style='font-size: 1.15rem; font-weight: 700; color: #F8FAFC; margin-bottom: 14px;'>Core Architectural Studios</div>", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown("""
    <div class="module-card">
        <div class="module-header">
            <span class="module-tag-badge">MODULE U1</span>
            <span class="module-title">Visual Analytics &amp; ML Lifecycle</span>
        </div>
        <div class="module-desc">
            Automated column distributions, IQR outlier detection, correlation heatmaps, 
            and deterministic machine learning task recommendation with candidate models.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="module-card">
        <div class="module-header">
            <span class="module-tag-badge">MODULE U2</span>
            <span class="module-title">LLM Data Assistant &amp; AST Sandbox</span>
        </div>
        <div class="module-desc">
            Natural language conversational dataset queries powered by Gemini 2.5 Flash, 
            verified through an <b>AST security allowlist</b> blocking malicious imports and writes.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

c3, c4 = st.columns(2)
with c3:
    st.markdown("""
    <div class="module-card">
        <div class="module-header">
            <span class="module-tag-badge">MODULE U3</span>
            <span class="module-title">Column Intelligence &amp; Multimodal Vision</span>
        </div>
        <div class="module-desc">
            Sentence-BERT (384-d) semantic column clustering and Gemini Multimodal Vision 
            chart reasoning for skewness, central tendencies, and anomalies.
        </div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="module-card">
        <div class="module-header">
            <span class="module-tag-badge">MODULE U4 &amp; U5</span>
            <span class="module-title">CTGAN Synthetic Data &amp; Responsible AI</span>
        </div>
        <div class="module-desc">
            PyTorch-based CTGAN synthetic tabular generation with Kolmogorov-Smirnov test 
            fidelity validation, automated PII auditing, and class imbalance alerts.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Active Dataset Overview Table
if st.session_state["df"] is not None:
    st.markdown("<div style='height: 22px;'></div>", unsafe_allow_html=True)
    st.markdown(f"### 📋 Active Dataset Inspection: `{st.session_state['dataset_name']}`")
    st.dataframe(st.session_state["df"].head(10), use_container_width=True)
    st.caption(f"Displaying top 10 rows of {len(st.session_state['df']):,} records. Navigate via the sidebar to access dedicated analytics studios.")
