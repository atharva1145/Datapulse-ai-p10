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

# Load CSS
css_path = ROOT_DIR / "assets" / "styles.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

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
# SECTION 1: KPI CARDS (MODERN SaaS STYLE)
# ==============================================================================
st.markdown(f"### 📌 Active Dataset: `{dataset_name}`")

k1, k2, k3, k4, k5, k6 = st.columns(6)

with k1:
    st.markdown(f"""
    <div class="kpi-metric-card">
        <div class="kpi-label">Total Rows</div>
        <div class="kpi-value">{profile['total_rows']:,}</div>
        <div class="kpi-delta">Records Loaded</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    st.markdown(f"""
    <div class="kpi-metric-card">
        <div class="kpi-label">Total Columns</div>
        <div class="kpi-value">{profile['total_cols']}</div>
        <div class="kpi-delta">Attributes</div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    st.markdown(f"""
    <div class="kpi-metric-card" style="border-left-color: {'#10B981' if profile['missing_cells'] == 0 else '#EF4444'};">
        <div class="kpi-label">Missing Values</div>
        <div class="kpi-value">{profile['missing_cells']:,}</div>
        <div class="kpi-delta" style="color: {'#10B981' if profile['missing_cells'] == 0 else '#EF4444'};">{profile['missing_pct']}% of Cells</div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    st.markdown(f"""
    <div class="kpi-metric-card" style="border-left-color: {'#10B981' if profile['duplicate_rows'] == 0 else '#F59E0B'};">
        <div class="kpi-label">Duplicate Rows</div>
        <div class="kpi-value">{profile['duplicate_rows']:,}</div>
        <div class="kpi-delta" style="color: {'#10B981' if profile['duplicate_rows'] == 0 else '#F59E0B'};">{profile['duplicate_pct']}% Rows</div>
    </div>
    """, unsafe_allow_html=True)

with k5:
    st.markdown(f"""
    <div class="kpi-metric-card">
        <div class="kpi-label">Numerical</div>
        <div class="kpi-value">{len(profile['numerical_cols'])}</div>
        <div class="kpi-delta">Continuous Features</div>
    </div>
    """, unsafe_allow_html=True)

with k6:
    st.markdown(f"""
    <div class="kpi-metric-card">
        <div class="kpi-label">Categorical</div>
        <div class="kpi-value">{len(profile['categorical_cols'])}</div>
        <div class="kpi-delta">Discrete Features</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# SECTION 2: DATASET QUALITY SCORE (FORMULA GROUNDED)
# ==============================================================================
col_score, col_penalties = st.columns([1, 2])

qs = profile["quality_score"]
with col_score:
    st.markdown(f"""
    <div class="quality-card">
        <div style="font-size: 0.82rem; font-weight: 700; color: #4F46E5; text-transform: uppercase; letter-spacing: 0.06em;">DATA QUALITY HEALTH</div>
        <div class="quality-score-number">{qs['score']}</div>
        <div style="font-size: 0.85rem; color: #64748B;">Out of 100 Points</div>
        <div class="quality-score-badge {qs['badge_class']}">{qs['rating']}</div>
    </div>
    """, unsafe_allow_html=True)

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

# Dataset Preview
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
