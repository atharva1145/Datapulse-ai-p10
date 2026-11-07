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
from modules.ui_components import render_page_header, render_empty_state_warning

st.set_page_config(page_title="Dashboard - DataPulse AI", page_icon="📊", layout="wide")

# Load CSS
css_path = ROOT_DIR / "assets" / "styles.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

render_page_header(
    page_title="Executive Dataset Profiling Dashboard",
    module_tag="MODULE U1 & UNIT I",
    subtitle="Statistical Health Profiling, Missingness Breakdown & Formulaic Quality Scoring"
)

# Verify active dataset
if "df" not in st.session_state or st.session_state["df"] is None:
    render_empty_state_warning()
    st.stop()

df = st.session_state["df"]
dataset_name = st.session_state.get("dataset_name", "Uploaded Dataset")
target_col = st.session_state.get("target_column", df.columns[-1])

# Profile the dataset
with st.spinner("Computing statistical profile and data quality metrics..."):
    profile = profile_dataset(df)

# ==============================================================================
# SECTION 1: ENTERPRISE METRIC CARDS (DATADOG / SNOWFLAKE STYLE)
# ==============================================================================
st.markdown(f"##### 📌 Current Ingestion: `{dataset_name}`")

m1, m2, m3, m4, m5, m6 = st.columns(6)

with m1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-tag">Total Rows</div>
        <div class="metric-num">{profile['total_rows']:,}</div>
        <div class="metric-sub" style="color: #64748B;">Sample Population</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-tag">Total Columns</div>
        <div class="metric-num">{profile['total_cols']}</div>
        <div class="metric-sub" style="color: #64748B;">Features Profiled</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    missing_color = "#059669" if profile['missing_cells'] == 0 else "#DC2626"
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-tag">Missing Values</div>
        <div class="metric-num">{profile['missing_cells']:,}</div>
        <div class="metric-sub" style="color: {missing_color};">{profile['missing_pct']}% of Cells</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    dupe_color = "#059669" if profile['duplicate_rows'] == 0 else "#D97706"
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-tag">Duplicate Rows</div>
        <div class="metric-num">{profile['duplicate_rows']:,}</div>
        <div class="metric-sub" style="color: {dupe_color};">{profile['duplicate_pct']}% Rows</div>
    </div>
    """, unsafe_allow_html=True)

with m5:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-tag">Continuous</div>
        <div class="metric-num">{len(profile['numerical_cols'])}</div>
        <div class="metric-sub" style="color: #2563EB;">Numerical Cols</div>
    </div>
    """, unsafe_allow_html=True)

with m6:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-tag">Discrete</div>
        <div class="metric-num">{len(profile['categorical_cols'])}</div>
        <div class="metric-sub" style="color: #4F46E5;">Categorical Cols</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# SECTION 2: DATASET QUALITY SCORE (FORMULA GROUNDED)
# ==============================================================================
col_score, col_penalties = st.columns([1, 2])

qs = profile["quality_score"]
with col_score:
    badge_bg = "#065F46" if qs['score'] >= 90 else ("#1E40AF" if qs['score'] >= 75 else "#92400E")
    st.markdown(f"""
    <div class="health-score-container">
        <div class="health-score-title">Data Quality Health Index</div>
        <div class="health-score-value">{qs['score']}</div>
        <div style="font-size: 0.8rem; color: #94A3B8; margin-top: 4px;">Normalized 100-Point Scale</div>
        <div class="health-badge-status" style="background: {badge_bg}; color: #FFFFFF;">{qs['rating']} Reliability</div>
    </div>
    """, unsafe_allow_html=True)

with col_penalties:
    st.markdown("<div style='font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;'>Mathematical Penalty Factor Breakdown</div>", unsafe_allow_html=True)
    penalties = qs["penalties"]
    pen_df = pd.DataFrame([
        {"Integrity Component": "Missing Values Penalty", "Formula Limit": "Max 40.0 pts", "Calculated Deduction": f"-{penalties['missing_penalty']} pts", "Severity": "🟢 Minimal" if penalties['missing_penalty'] < 5 else "🔴 High"},
        {"Integrity Component": "Duplicate Records Penalty", "Formula Limit": "Max 20.0 pts", "Calculated Deduction": f"-{penalties['duplicate_penalty']} pts", "Severity": "🟢 Zero" if penalties['duplicate_penalty'] == 0 else "🟡 Moderate"},
        {"Integrity Component": "Zero-Variance / Constant Columns", "Formula Limit": "Max 20.0 pts", "Calculated Deduction": f"-{penalties['constant_penalty']} pts", "Severity": "🟢 Clean" if penalties['constant_penalty'] == 0 else "🔴 Alert"},
        {"Integrity Component": "IQR Outlier Cells (1.5×IQR Rule)", "Formula Limit": "Max 20.0 pts", "Calculated Deduction": f"-{penalties['outlier_penalty']} pts", "Severity": "🟢 Nominal" if penalties['outlier_penalty'] < 5 else "🟡 Attention"}
    ])
    st.dataframe(pen_df, use_container_width=True, hide_index=True)
    st.caption(f"**Deterministic Formula Grounding:** `{qs['formula']}` (Evaluated strictly on uploaded records)")

st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# SECTION 3: MISSING VALUES ANALYSIS & PREVIEW
# ==============================================================================
st.markdown("<div style='font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;'>Attribute Completeness Audit</div>", unsafe_allow_html=True)
fig_missing = plot_missing_values(profile["missing_by_col"])
fig_missing.update_layout(template="plotly_white")
st.plotly_chart(fig_missing, use_container_width=True)

# Dataset Preview
st.markdown("<div style='font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;'>Tabular Data Ingestion Sample</div>", unsafe_allow_html=True)
st.dataframe(df.head(20), use_container_width=True)
st.caption(f"Viewing first 20 records of {len(df):,} total rows.")

st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

# Quick Recommended Task Callout
with st.container():
    rec = recommend_ml_task(df, target_column=target_col)
    st.info(
        f"💡 **Recommended Machine Learning Task for Target '{target_col}':** "
        f"**{rec['suggested_task']}** ({rec['learning_type']}). "
        f"Navigate to **3_ML_Recommendations** in the sidebar to review candidate algorithms and the 10-stage lifecycle!"
    )
