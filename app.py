"""
CSV INSIGHT AI - Main Application Entrypoint
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

# Configure page layout and metadata
st.set_page_config(
    page_title=f"{APP_NAME} - P10",
    page_icon="📊",
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
# SIDEBAR: Dataset Upload & Information Panel
# ==============================================================================
with st.sidebar:
    st.markdown(f"""
    <div class="sidebar-brand-box">
        <div style="font-size: 1.25rem; font-weight: 800; color: #1E1B4B; display: flex; align-items: center; gap: 8px;">
            <span>📊</span> {APP_NAME}
        </div>
        <div style="font-size: 0.78rem; color: #64748B; font-weight: 600; margin-top: 2px;">
            P10: CSV Dataset Insight &amp; Task Recommender
        </div>
        <div style="font-size: 0.75rem; color: #4F46E5; font-weight: 700; margin-top: 6px;">
            Student: {STUDENT_NAME} (Roll: {ROLL_NUMBER})
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📁 Dataset Selector")
    data_source = st.radio(
        "Choose Data Source:",
        ["Sample Benchmark Dataset", "Upload Custom CSV"],
        index=0,
        help="Select one of the 3 verified benchmark datasets or upload your own file."
    )

    if data_source == "Sample Benchmark Dataset":
        selected_sample = st.selectbox(
            "Select Benchmark Dataset:",
            list(SAMPLE_DATASETS.keys()),
            index=0
        )
        sample_info = SAMPLE_DATASETS[selected_sample]
        st.caption(f"**Task:** {sample_info['task_type']}")
        
        if st.button("⚡ Load Selected Dataset", use_container_width=True, type="primary"):
            sample_path = SAMPLE_DATA_DIR / sample_info["filename"]
            df, meta, err = load_csv(sample_path)
            if err:
                st.error(err)
            else:
                st.session_state["df"] = df
                st.session_state["metadata"] = meta
                st.session_state["dataset_name"] = selected_sample
                st.session_state["target_column"] = meta["columns"][-1]
                st.success(f"Loaded {selected_sample}!")
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
            if st.button("⚡ Process Uploaded CSV", use_container_width=True, type="primary"):
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
                    st.success(f"Loaded {meta['filename']}!")
                    st.rerun()

    # Active Dataset Status Pill in Sidebar
    if st.session_state["df"] is not None:
        st.markdown(f"""
        <div class="sidebar-status-pill">
            <div class="pulse-dot"></div>
            <div>Active: <b>{st.session_state['dataset_name']}</b><br/>
            <span style="font-size: 0.74rem; color: #64748B;">{len(st.session_state['df']):,} rows × {len(st.session_state['df'].columns)} cols</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# MAIN PAGE: HERO BANNER & NAVIGATION CARDS
# ==============================================================================
st.markdown(f"""
<div class="hero-container">
    <div class="hero-title">{APP_NAME}</div>
    <div class="hero-subtitle">{APP_SUBTITLE}</div>
    <div class="hero-badge-pill">
        <span>🎓 Continuous Assessment Mini Project (P10)</span> • 
        <span>Student: {STUDENT_NAME} (Roll No: {ROLL_NUMBER})</span> • 
        <span>{COURSE_NAME}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Feature Navigation Grid
st.markdown("### 🧭 Architecture & Capabilities")

card1, card2 = st.columns(2)
with card1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-header">
            <div class="feature-icon-box">📈</div>
            <div>
                <div class="feature-title">Module U1: Visual Analytics &amp; ML Recommender</div>
            </div>
        </div>
        <div class="feature-description">
            Interactive Plotly column distributions, box plots, correlation heatmaps, 
            deterministic heuristic recommendations for Supervised/Unsupervised algorithms, 
            and a tailored 10-stage ML lifecycle roadmap.
        </div>
    </div>
    """, unsafe_allow_html=True)

with card2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-header">
            <div class="feature-icon-box">💬</div>
            <div>
                <div class="feature-title">Module U2: LLM + Pandas Data Assistant</div>
            </div>
        </div>
        <div class="feature-description">
            Natural language dataset querying powered by Gemini 2.5 Flash. 
            Synthesizes Pandas code protected by an <b>AST security allowlist</b> that blocks 
            malicious imports, executes in a sandboxed namespace, and explains findings in plain English.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

card3, card4 = st.columns(2)
with card3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-header">
            <div class="feature-icon-box">🧠</div>
            <div>
                <div class="feature-title">Module U3: Column Intelligence &amp; Vision LLM</div>
            </div>
        </div>
        <div class="feature-description">
            Sentence-BERT (<code>all-MiniLM-L6-v2</code>) semantic 384-d vector embeddings 
            with interactive cosine similarity clustering. Streamlined multimodal Gemini Vision 
            pipeline that visually reads and explains distribution charts.
        </div>
    </div>
    """, unsafe_allow_html=True)

with card4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-card-header">
            <div class="feature-icon-box">🧬</div>
            <div>
                <div class="feature-title">Module U4 &amp; U5: Synthetic CTGAN &amp; Responsible AI</div>
            </div>
        </div>
        <div class="feature-description">
            PyTorch-compatible CTGAN for tabular synthesis evaluated with Kolmogorov-Smirnov 
            two-sample tests, regex-based PII attribute detection, target class imbalance 
            audits, and verifiable hallucination benchmarks.
        </div>
    </div>
    """, unsafe_allow_html=True)

# Active Dataset Preview Table
if st.session_state["df"] is not None:
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    st.markdown(f"### 📋 Active Dataset Preview: `{st.session_state['dataset_name']}`")
    st.dataframe(st.session_state["df"].head(10), use_container_width=True)
    st.caption(f"Displaying first 10 rows of {len(st.session_state['df']):,} total records. Use the sidebar to navigate to all analytical studios.")
