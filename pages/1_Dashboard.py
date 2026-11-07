"""
Page: 1_Dashboard
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

High-level KPI overview, Dataset Quality Score gauge, missing-value charts,
column type breakdown, and executive summary.
"""

import sys
from pathlib import Path
import streamlit as st
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from modules.data_profiler import profile_dataset
from modules.visualization import plot_missing_values
from modules.ml_recommender import recommend_ml_task

st.set_page_config(page_title="Dashboard - CSV INSIGHT AI", page_icon="📊", layout="wide")

st.title("📊 Executive Dataset Dashboard")
st.caption("P10 – Unit I: High-Level Dataset Profiling & Empirical Health Scoring")

# Verify active dataset
if "df" not in st.session_state or st.session_state["df"] is None:
    st.warning("⚠️ No dataset currently loaded. Please return to the Home page to select or upload a CSV.")
    st.stop()

df = st.session_state["df"]
dataset_name = st.session_state.get("dataset_name", "Uploaded Dataset")
target_col = st.session_state.get("target_column", df.columns[-1])

# Profile the dataset
with st.spinner("Computing statistical profile and data quality metrics..."):
    profile = profile_dataset(df)

# ==============================================================================
# SECTION 1: KPI CARDS
# ==============================================================================
st.markdown(f"### 📌 Dataset: `{dataset_name}`")

kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
with kpi1:
    st.metric("Total Rows", f"{profile['total_rows']:,}")
with kpi2:
    st.metric("Total Columns", profile["total_cols"])
with kpi3:
    st.metric("Missing Values", f"{profile['missing_cells']:,}", f"{profile['missing_pct']}% cells", delta_color="inverse")
with kpi4:
    st.metric("Duplicate Rows", f"{profile['duplicate_rows']:,}", f"{profile['duplicate_pct']}% rows", delta_color="inverse")
with kpi5:
    st.metric("Numerical Cols", len(profile["numerical_cols"]))
with kpi6:
    st.metric("Categorical Cols", len(profile["categorical_cols"]))

st.markdown("---")

# ==============================================================================
# SECTION 2: DATASET QUALITY SCORE (FORMULA GROUNDED)
# ==============================================================================
col_score, col_penalties = st.columns([1, 2])

qs = profile["quality_score"]
with col_score:
    st.markdown("### 🛡️ Data Quality Score")
    score_val = qs["score"]
    st.markdown(f"<div style='font-size: 3rem; font-weight: 800; color: #4F46E5;'>{score_val}/100</div>", unsafe_allow_html=True)
    st.markdown(f"**Rating:** <span class='quality-score-badge {qs['badge_class']}'>{qs['rating']}</span>", unsafe_allow_html=True)
    st.caption("Deterministic evaluation calculated directly from dataset integrity metrics.")

with col_penalties:
    st.markdown("### 🧮 Quality Score Penalty Breakdown")
    penalties = qs["penalties"]
    pen_df = pd.DataFrame([
        {"Integrity Factor": "Missing Values Penalty", "Formula Bound": "Max 40 pts", "Deduction": f"-{penalties['missing_penalty']} pts"},
        {"Integrity Factor": "Duplicate Records Penalty", "Formula Bound": "Max 20 pts", "Deduction": f"-{penalties['duplicate_penalty']} pts"},
        {"Integrity Factor": "Constant Columns Penalty", "Formula Bound": "Max 20 pts", "Deduction": f"-{penalties['constant_penalty']} pts"},
        {"Integrity Factor": "IQR Outlier Cells Penalty", "Formula Bound": "Max 20 pts", "Deduction": f"-{penalties['outlier_penalty']} pts"}
    ])
    st.dataframe(pen_df, use_container_width=True, hide_index=True)
    st.caption(f"**Exact Formula:** `{qs['formula']}`")

st.markdown("---")

# ==============================================================================
# SECTION 3: MISSING VALUES ANALYSIS & PREVIEW
# ==============================================================================
st.markdown("### 🔍 Missing Values & Completeness")
fig_missing = plot_missing_values(profile["missing_by_col"])
st.plotly_chart(fig_missing, use_container_width=True)

# Dataset Preview with Search
st.markdown("### 📋 Interactive Dataset Preview")
st.dataframe(df.head(20), use_container_width=True)
st.caption(f"Showing first 20 records of {len(df):,} total rows.")

st.markdown("---")

# Quick Recommended Task Callout
with st.container():
    rec = recommend_ml_task(df, target_column=target_col)
    st.info(
        f"💡 **Recommended Machine Learning Task for '{target_col}':** "
        f"**{rec['suggested_task']}** ({rec['learning_type']}). "
        f"Navigate to **ML Recommendations** in the sidebar for algorithms and the full 10-stage lifecycle!"
    )
