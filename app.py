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
from modules.ui_components import render_page_header, get_logo_html, apply_theme

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

# Apply dynamic active theme early before sidebar and components
apply_theme()

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
            <div style="font-size: 1.15rem; font-weight: 800; color: var(--text-primary, #FFFFFF); letter-spacing: -0.02em; line-height: 1.2;">
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

    # 1-Click Fast Benchmarks
    st.markdown("<div style='font-size: 0.72rem; font-weight: 700; color: var(--text-tertiary, #64748B); text-transform: uppercase; margin-top: 10px; margin-bottom: 6px;'>Fast Benchmarks</div>", unsafe_allow_html=True)
    sb_c1, sb_c2, sb_c3 = st.columns(3)
    with sb_c1:
        if st.button("🌸 Iris", use_container_width=True, help="Load 150 rows multiclass benchmark"):
            df_i, meta_i, _ = load_csv(SAMPLE_DATA_DIR / "iris.csv")
            st.session_state["df"] = df_i
            st.session_state["metadata"] = meta_i
            st.session_state["dataset_name"] = "Iris Flower Dataset"
            st.session_state["target_column"] = "species"
            st.rerun()
    with sb_c2:
        if st.button("🚢 Titanic", use_container_width=True, help="Load 891 rows binary imbalance benchmark"):
            df_t, meta_t, _ = load_csv(SAMPLE_DATA_DIR / "titanic.csv")
            st.session_state["df"] = df_t
            st.session_state["metadata"] = meta_t
            st.session_state["dataset_name"] = "Titanic Survival Dataset"
            st.session_state["target_column"] = "Survived"
            st.rerun()
    with sb_c3:
        if st.button("🍷 Wine", use_container_width=True, help="Load 1,599 rows regression benchmark"):
            df_w, meta_w, _ = load_csv(SAMPLE_DATA_DIR / "winequality_red.csv")
            st.session_state["df"] = df_w
            st.session_state["metadata"] = meta_w
            st.session_state["dataset_name"] = "Wine Quality Dataset"
            st.session_state["target_column"] = "quality"
            st.rerun()

    # Active Dataset Status Box
    if st.session_state["df"] is not None:
        st.markdown(f"""
        <div class="sidebar-status-box">
            <div style="font-weight: 700; color: var(--text-primary, #F8FAFC); display: flex; align-items: center; justify-content: space-between;">
                <span>ACTIVE DATASET</span>
                <span style="display: flex; align-items: center; gap: 4px; color: #10B981; font-size: 0.7rem;">
                    <span class="status-dot-active"></span> READY
                </span>
            </div>
            <div style="font-size: 0.85rem; color: #38BDF8; font-weight: 600; margin-top: 4px;">{st.session_state['dataset_name']}</div>
            <div style="font-size: 0.75rem; color: var(--text-secondary, #94A3B8); margin-top: 2px;">
                {len(st.session_state['df']):,} rows • {len(st.session_state['df'].columns)} features
            </div>
        </div>
        """, unsafe_allow_html=True)

# ==============================================================================
# MULTIPAGE ROUTER (EXACT 6 CORE MODULES)
# ==============================================================================
pages = [
    st.Page("pages/1_Visual_Analytics.py", title="Visual Analytics", icon="📈", default=True),
    st.Page("pages/2_ML_Recommendations.py", title="ML", icon="🤖"),
    st.Page("pages/3_AI_Data_Assistant.py", title="AI Data Assistant", icon="💬"),
    st.Page("pages/4_Column_Intelligence.py", title="Column Intelligence", icon="🧠"),
    st.Page("pages/5_Synthetic_Data_Lab.py", title="Synthetic Data Lab", icon="🧬"),
    st.Page("pages/6_Responsible_AI.py", title="Responsible AI", icon="🛡️"),
]

pg = st.navigation(pages, position="sidebar")
pg.run()
