"""
Page: 1_Visual_Analytics
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Task U1: Visual Analytics Studio
- Tab 1: Dataset Health, Quality Score & Completeness
- Tab 2: Univariate Distributions (Numerical & Categorical)
- Tab 3: Pearson Correlation Heatmap
- Tab 4: Bivariate Relationships & Outlier Boxplots
- Tab 5: Descriptive Statistics Inventory
"""

import sys
from pathlib import Path
import streamlit as st
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from modules.data_profiler import profile_dataset
from modules.visualization import (
    plot_missing_values,
    plot_numerical_distribution,
    plot_categorical_distribution,
    plot_correlation_heatmap,
    plot_scatter_relationship
)
from modules.ml_recommender import recommend_ml_task
from modules.ui_components import render_page_header, render_empty_state_warning

render_page_header(
    page_title="Visual Analytics",
    module_tag="MODULE U1",
    subtitle="Interactive Column Distributions, Health Index, Correlation Matrix & Bivariate Analytics"
)

if "df" not in st.session_state or st.session_state["df"] is None:
    render_empty_state_warning()
    st.stop()

df = st.session_state["df"]
dataset_name = st.session_state.get("dataset_name", "Uploaded Dataset")
target_col = st.session_state.get("target_column", df.columns[-1])

# Profile the dataset
with st.spinner("Computing statistical profile and data quality metrics..."):
    profile = profile_dataset(df)

tab_health, tab_dist, tab_corr, tab_bivariate, tab_stats = st.tabs([
    "📋 Health & Overview",
    "📊 Column Distributions",
    "🔥 Correlation Heatmap",
    "🔗 Bivariate Relationships",
    "📑 Descriptive Statistics"
])

# ==============================================================================
# TAB 1: DATASET HEALTH & EXECUTIVE KPIS
# ==============================================================================
with tab_health:
    st.markdown(f"##### 📌 Current Ingestion: `{dataset_name}`")

    m1, m2, m3, m4, m5, m6 = st.columns(6)
    with m1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-tag">Total Rows</div>
            <div class="metric-num">{profile['total_rows']:,}</div>
            <div class="metric-sub" style="color: var(--text-tertiary, #64748B);">Population</div>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-tag">Total Columns</div>
            <div class="metric-num">{profile['total_cols']}</div>
            <div class="metric-sub" style="color: var(--text-tertiary, #64748B);">Features</div>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        missing_color = "#10B981" if profile['missing_cells'] == 0 else "#EF4444"
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-tag">Missing Values</div>
            <div class="metric-num">{profile['missing_cells']:,}</div>
            <div class="metric-sub" style="color: {missing_color};">{profile['missing_pct']}% of Cells</div>
        </div>
        """, unsafe_allow_html=True)
    with m4:
        dupe_color = "#10B981" if profile['duplicate_rows'] == 0 else "#F59E0B"
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
            <div class="metric-sub" style="color: #38BDF8;">Numerical</div>
        </div>
        """, unsafe_allow_html=True)
    with m6:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-tag">Discrete</div>
            <div class="metric-num">{len(profile['categorical_cols'])}</div>
            <div class="metric-sub" style="color: #818CF8;">Categorical</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

    col_score, col_penalties = st.columns([1, 2])
    qs = profile["quality_score"]
    with col_score:
        badge_bg = "#065F46" if qs['score'] >= 90 else ("#1E40AF" if qs['score'] >= 75 else "#92400E")
        st.markdown(f"""
        <div class="health-score-container">
            <div class="health-score-title">Data Quality Health Index</div>
            <div class="health-score-value">{qs['score']}</div>
            <div style="font-size: 0.8rem; color: var(--text-secondary, #94A3B8); margin-top: 4px;">Normalized 100-Point Scale</div>
            <div class="health-badge-status" style="background: {badge_bg}; color: #FFFFFF;">{qs['rating']} Reliability</div>
        </div>
        """, unsafe_allow_html=True)

    with col_penalties:
        st.markdown("<div style='font-size: 1.05rem; font-weight: 700; color: var(--text-primary, #0F172A); margin-bottom: 8px;'>Mathematical Penalty Factor Breakdown</div>", unsafe_allow_html=True)
        penalties = qs["penalties"]
        pen_df = pd.DataFrame([
            {"Integrity Component": "Missing Values Penalty", "Formula Limit": "Max 40.0 pts", "Calculated Deduction": f"-{penalties['missing_penalty']} pts", "Severity": "🟢 Minimal" if penalties['missing_penalty'] < 5 else "🔴 High"},
            {"Integrity Component": "Duplicate Records Penalty", "Formula Limit": "Max 20.0 pts", "Calculated Deduction": f"-{penalties['duplicate_penalty']} pts", "Severity": "🟢 Zero" if penalties['duplicate_penalty'] == 0 else "🟡 Moderate"},
            {"Integrity Component": "Zero-Variance / Constant Columns", "Formula Limit": "Max 20.0 pts", "Calculated Deduction": f"-{penalties['constant_penalty']} pts", "Severity": "🟢 Clean" if penalties['constant_penalty'] == 0 else "🔴 Alert"},
            {"Integrity Component": "IQR Outlier Cells (1.5×IQR Rule)", "Formula Limit": "Max 20.0 pts", "Calculated Deduction": f"-{penalties['outlier_penalty']} pts", "Severity": "🟢 Nominal" if penalties['outlier_penalty'] < 5 else "🟡 Attention"}
        ])
        st.table(pen_df)
        st.caption(f"**Deterministic Formula Grounding:** `{qs['formula']}` (Evaluated strictly on uploaded records)")

    st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 1.05rem; font-weight: 700; color: var(--text-primary, #0F172A); margin-bottom: 8px;'>Attribute Completeness Audit</div>", unsafe_allow_html=True)
    fig_missing = plot_missing_values(profile["missing_by_col"])
    st.plotly_chart(fig_missing, use_container_width=True)

# ==============================================================================
# TAB 2: SINGLE COLUMN DISTRIBUTIONS
# ==============================================================================
with tab_dist:
    st.markdown("### 📊 Univariate Distribution Analysis")
    all_cols = list(df.columns)
    selected_col = st.selectbox("Select Column to Analyze:", all_cols, index=0)

    col_meta = profile["column_profiles"].get(selected_col, {})
    col_type = col_meta.get("type_category", "Unknown")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-tag">Detected Type</div>
            <div class="metric-num" style="font-size: 1.5rem;">{col_type}</div>
            <div class="metric-sub" style="color: #818CF8;">Category Inferred</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-tag">Data Type</div>
            <div class="metric-num" style="font-size: 1.5rem;">{col_meta.get('dtype', str(df[selected_col].dtype))}</div>
            <div class="metric-sub" style="color: var(--text-secondary, #94A3B8);">Pandas dtype</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-tag">Unique Values</div>
            <div class="metric-num" style="font-size: 1.5rem;">{col_meta.get('unique_count', df[selected_col].nunique()):,}</div>
            <div class="metric-sub" style="color: #38BDF8;">Cardinality</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        miss_color = "#10B981" if col_meta.get('missing_count', 0) == 0 else "#EF4444"
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-tag">Missing Count</div>
            <div class="metric-num" style="font-size: 1.5rem;">{col_meta.get('missing_count', 0)}</div>
            <div class="metric-sub" style="color: {miss_color};">{col_meta.get('missing_pct', 0)}% of column</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

    if col_type in ["Numerical (Continuous)", "Numerical (Discrete)"]:
        fig_dist = plot_numerical_distribution(df, selected_col)
        st.plotly_chart(fig_dist, use_container_width=True)

        s_col = df[selected_col].dropna()
        stat1, stat2, stat3, stat4, stat5 = st.columns(5)
        stat1.metric("Mean", f"{s_col.mean():.3f}" if len(s_col) > 0 else "N/A")
        stat2.metric("Median", f"{s_col.median():.3f}" if len(s_col) > 0 else "N/A")
        stat3.metric("Std Dev", f"{s_col.std():.3f}" if len(s_col) > 0 else "N/A")
        stat4.metric("Skewness", f"{s_col.skew():.3f}" if len(s_col) > 0 else "N/A")
        stat5.metric("Kurtosis", f"{s_col.kurt():.3f}" if len(s_col) > 0 else "N/A")

    else:
        fig_dist = plot_categorical_distribution(df, selected_col)
        st.plotly_chart(fig_dist, use_container_width=True)
        top_cats = df[selected_col].value_counts().head(5)
        st.markdown("**Top Categories Breakdown:**")
        st.dataframe(pd.DataFrame({"Category": top_cats.index.astype(str), "Count": top_cats.values, "Share (%)": (top_cats.values / len(df) * 100).round(2)}), use_container_width=True, hide_index=True)

# ==============================================================================
# TAB 3: CORRELATION HEATMAP
# ==============================================================================
with tab_corr:
    st.markdown("### 🔥 Pearson Correlation Matrix")
    num_cols = profile.get("numerical_cols", [])
    if len(num_cols) < 2:
        st.warning("At least 2 numerical columns are required to calculate Pearson correlation.")
    else:
        selected_heatmap_cols = st.multiselect(
            "Select columns to include in correlation matrix:",
            num_cols,
            default=num_cols[:12]
        )
        if len(selected_heatmap_cols) >= 2:
            fig_corr = plot_correlation_heatmap(df, numerical_cols=selected_heatmap_cols)
            if fig_corr is not None:
                st.plotly_chart(fig_corr, use_container_width=True)
        else:
            st.info("Please select at least 2 features.")

# ==============================================================================
# TAB 4: BIVARIATE RELATIONSHIPS
# ==============================================================================
with tab_bivariate:
    st.markdown("### 🔗 Bivariate Feature Interaction")
    num_cols = profile.get("numerical_cols", [])
    if len(num_cols) < 2:
        st.warning("At least 2 numerical columns are required for scatter plot relationships.")
    else:
        b1, b2, b3 = st.columns(3)
        with b1:
            x_col = st.selectbox("X-Axis Feature:", num_cols, index=0)
        with b2:
            y_col = st.selectbox("Y-Axis Feature:", num_cols, index=min(1, len(num_cols) - 1))
        with b3:
            color_candidates = ["None"] + list(df.columns)
            color_choice = st.selectbox("Color / Hue by:", color_candidates, index=len(color_candidates) - 1 if len(color_candidates) > 1 else 0)

        color_col = None if color_choice == "None" else color_choice
        fig_scatter = plot_scatter_relationship(df, x_col, y_col, color_col=color_col)
        st.plotly_chart(fig_scatter, use_container_width=True)

# ==============================================================================
# TAB 5: DESCRIPTIVE STATISTICS
# ==============================================================================
with tab_stats:
    st.markdown("### 📑 Tabular Feature Inventory & Summary Statistics")
    summary_data = []
    for col_name, cinfo in profile["column_profiles"].items():
        summary_data.append({
            "Column Name": col_name,
            "Type Category": cinfo.get("type_category", "Unknown"),
            "dtype": cinfo.get("dtype", str(df[col_name].dtype)),
            "Unique Count": cinfo.get("unique_count", df[col_name].nunique()),
            "Missing Count": cinfo.get("missing_count", 0),
            "Missing %": f"{cinfo.get('missing_pct', 0):.2f}%",
            "Outlier Count": cinfo.get("outlier_count", "N/A"),
            "Outlier %": f"{cinfo.get('outlier_pct', 0):.2f}%" if "outlier_pct" in cinfo else "N/A"
        })
    st.dataframe(pd.DataFrame(summary_data), use_container_width=True, hide_index=True)

    num_summary = df.describe()
    if not num_summary.empty:
        st.markdown("##### 🔢 Numerical Distribution Summary (`df.describe()`)")
        st.dataframe(num_summary.round(3), use_container_width=True)
