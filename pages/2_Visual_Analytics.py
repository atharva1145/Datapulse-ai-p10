"""
Page: 2_Visual_Analytics
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Task U1: Plot column distributions (numerical & categorical),
correlation heatmaps, and bivariate relationships.
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
    plot_numerical_distribution,
    plot_categorical_distribution,
    plot_correlation_heatmap,
    plot_scatter_relationship
)
from modules.ui_components import render_page_header, render_empty_state_warning

st.set_page_config(page_title="Visual Analytics - CSV INSIGHT AI", page_icon="📈", layout="wide")

# Load CSS
css_path = ROOT_DIR / "assets" / "styles.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

render_page_header(
    page_title="Visual Analytics & Distribution Studio",
    module_tag="MODULE U1",
    subtitle="Interactive Column Distributions, Outlier Boxplots, and Pearson Correlation Matrix"
)

if "df" not in st.session_state or st.session_state["df"] is None:
    render_empty_state_warning()
    st.stop()

df = st.session_state["df"]
profile = profile_dataset(df)

tab_dist, tab_corr, tab_bivariate, tab_stats = st.tabs([
    "📊 Single Column Distributions",
    "🔥 Correlation Heatmap",
    "🔗 Bivariate Relationships",
    "📑 Descriptive Statistics"
])

# ==============================================================================
# TAB 1: SINGLE COLUMN DISTRIBUTIONS
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
            <div class="metric-sub" style="color: #94A3B8;">Pandas dtype</div>
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

    st.markdown("---")

    if col_type == "Numerical":
        fig_num = plot_numerical_distribution(df, selected_col)
        st.plotly_chart(fig_num, use_container_width=True)
        
        # Outlier & Summary Callout
        st.info(
            f"📈 **Summary for {selected_col}:** "
            f"Mean: `{col_meta.get('mean')}` | Median: `{col_meta.get('median')}` | "
            f"Std Dev: `{col_meta.get('std')}` | Min: `{col_meta.get('min')}` | Max: `{col_meta.get('max')}` | "
            f"IQR Outliers: `{col_meta.get('outlier_count', 0)}` records"
        )
    else:
        fig_cat = plot_categorical_distribution(df, selected_col)
        st.plotly_chart(fig_cat, use_container_width=True)

# ==============================================================================
# TAB 2: CORRELATION HEATMAP
# ==============================================================================
with tab_corr:
    st.markdown("### 🔥 Pearson Feature Correlation Matrix")
    num_cols = profile["numerical_cols"]
    if len(num_cols) < 2:
        st.warning("At least two numerical columns are required to generate a correlation heatmap.")
    else:
        fig_corr = plot_correlation_heatmap(df, num_cols)
        if fig_corr:
            st.plotly_chart(fig_corr, use_container_width=True)
            st.caption("Values range from -1.0 (strong inverse correlation) to +1.0 (strong positive correlation).")

# ==============================================================================
# TAB 3: BIVARIATE RELATIONSHIPS
# ==============================================================================
with tab_bivariate:
    st.markdown("### 🔗 Bivariate Scatter Analysis")
    if len(num_cols) < 2:
        st.warning("At least two numerical columns are required for scatter plot analysis.")
    else:
        b1, b2, b3 = st.columns(3)
        with b1:
            x_col = st.selectbox("X-Axis Feature:", num_cols, index=0)
        with b2:
            y_col = st.selectbox("Y-Axis Feature:", num_cols, index=min(1, len(num_cols) - 1))
        with b3:
            hue_options = ["None"] + profile["categorical_cols"]
            hue_choice = st.selectbox("Color By (Grouping):", hue_options, index=0)

        fig_scat = plot_scatter_relationship(
            df,
            x_col=x_col,
            y_col=y_col,
            color_col=None if hue_choice == "None" else hue_choice
        )
        st.plotly_chart(fig_scat, use_container_width=True)

# ==============================================================================
# TAB 4: DESCRIPTIVE STATISTICS
# ==============================================================================
with tab_stats:
    st.markdown("### 📑 Full Descriptive Statistics Summary")
    if not profile["numeric_summary"].empty:
        st.markdown("#### Numerical Attributes (Five-Number Summary + Mean & Std)")
        st.dataframe(profile["numeric_summary"], use_container_width=True)
    else:
        st.info("No numerical attributes detected in this dataset.")

    st.markdown("#### Categorical Attributes Breakdown")
    cat_summary = []
    for c in profile["categorical_cols"]:
        meta = profile["column_profiles"][c]
        top_dict = meta.get("top_values", {})
        top_str = ", ".join([f"{k} ({v})" for k, v in list(top_dict.items())[:3]])
        cat_summary.append({
            "Column": c,
            "Unique Count": meta["unique_count"],
            "Missing Count": meta["missing_count"],
            "Top Values (Frequencies)": top_str
        })
    if cat_summary:
        st.dataframe(pd.DataFrame(cat_summary), use_container_width=True)
