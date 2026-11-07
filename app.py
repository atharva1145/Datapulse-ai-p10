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

# ==============================================================================
# SIDEBAR: Dataset Upload & Information Panel
# ==============================================================================
with st.sidebar:
    st.markdown(f"## 📊 {APP_NAME}")
    st.caption(f"**P10:** CSV Dataset Insight & Task Recommender")
    st.markdown(f"**Student:** {STUDENT_NAME}  \n**Roll No:** {ROLL_NUMBER} | **Subject:** {COURSE_NAME}")
    st.markdown("---")

    st.subheader("📁 Dataset Selection")
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
        st.info(f"**Task:** {sample_info['task_type']}\n\n{sample_info['description']}")
        
        if st.button("Load Selected Dataset", use_container_width=True, type="primary"):
            sample_path = SAMPLE_DATA_DIR / sample_info["filename"]
            df, meta, err = load_csv(sample_path)
            if err:
                st.error(err)
            else:
                st.session_state["df"] = df
                st.session_state["metadata"] = meta
                st.session_state["dataset_name"] = selected_sample
                st.session_state["target_column"] = meta["columns"][-1]
                st.success(f"Loaded {selected_sample} ({meta['row_count']} rows, {meta['col_count']} cols)")
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
            if st.button("Process Uploaded CSV", use_container_width=True, type="primary"):
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
                    st.success(f"Successfully loaded {meta['filename']}!")
                    st.rerun()

    # Active Dataset Status Widget
    st.markdown("---")
    st.subheader("📌 Active Dataset Status")
    if st.session_state["df"] is not None:
        st.success(f"**Active:** `{st.session_state['dataset_name']}`")
        st.markdown(f"- **Rows:** `{len(st.session_state['df']):,}`")
        st.markdown(f"- **Columns:** `{len(st.session_state['df'].columns)}`")
        if st.session_state["target_column"]:
            st.markdown(f"- **Default Target:** `{st.session_state['target_column']}`")
    else:
        st.warning("No dataset loaded yet. Please select or upload a dataset.")

# ==============================================================================
# MAIN PAGE: Welcome & System Navigation Overview
# ==============================================================================
st.title(f"🚀 {APP_NAME}")
st.markdown(f"*{APP_SUBTITLE}*")
st.markdown(f"**Student:** {STUDENT_NAME} (Roll No: {ROLL_NUMBER}) | **Continuous Assessment Practical:** P10")

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

st.markdown("---")

# Quick Navigation Grid
st.markdown("### 🧭 Architecture & Module Navigation")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    #### 📈 U1 – Visual Analytics
    - Column distributions (Hist, Box, Bar)
    - Correlation heatmaps
    - Supervised / Unsupervised Recommender
    - 10-Stage ML Lifecycle roadmap
    """)

with col2:
    st.markdown("""
    #### 💬 U2 – AI Data Assistant
    - Natural language query to Pandas
    - Strict AST security validator
    - Sandboxed execution runner
    - Plain-English output explanations
    """)

with col3:
    st.markdown("""
    #### 🧠 U3 – Column Intelligence
    - Sentence-BERT column embeddings
    - Cosine similarity clustering
    - Gemini Multimodal Vision API
    - Automated chart insight reader
    """)

with col4:
    st.markdown("""
    #### 🧬 U4 & U5 – Synthetic & Responsible AI
    - PyTorch CTGAN tabular generation
    - Real vs. Synthetic KS tests
    - Sensitive PII column detection
    - Target class imbalance analysis
    """)

# Current Loaded Dataset Quick Preview
if st.session_state["df"] is not None:
    st.markdown("---")
    st.markdown(f"### 📋 Dataset Quick Preview: `{st.session_state['dataset_name']}`")
    st.dataframe(st.session_state["df"].head(10), use_container_width=True)
    st.caption(f"Displaying first 10 rows of {len(st.session_state['df']):,} total records.")
