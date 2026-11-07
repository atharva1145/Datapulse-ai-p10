"""
Page: 7_Responsible_AI
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Task U5 & Unit V:
- Sensitive Column (PII) Detection
- Class Imbalance & Metric Recommender
- Safety Guardrails Audit
- Empirical Bias & Hallucination Test Bench with Documented Failure Cases
"""

import sys
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from modules.responsible_ai import (
    scan_sensitive_columns,
    analyze_class_imbalance,
    run_empirical_hallucination_benchmark
)
from modules.ui_components import render_page_header, render_empty_state_warning

try:
    st.set_page_config(page_title="Responsible AI - DataPulse AI", page_icon="🛡️", layout="wide")
except Exception:
    pass

render_page_header(
    page_title="Responsible AI & Ethical Guardrails Studio",
    module_tag="MODULE U5 & UNIT V",
    subtitle="Automated PII Auditing, Class Imbalance Accuracy Paradox Analysis & Empirical Hallucination Test Bench"
)

if "df" not in st.session_state or st.session_state["df"] is None:
    render_empty_state_warning()
    st.stop()

df = st.session_state["df"]
dataset_name = st.session_state.get("dataset_name", "Uploaded Dataset")

tab_pii, tab_imbalance, tab_bench = st.tabs([
    "🕵️ Sensitive Data & PII Detection",
    "⚖️ Class Imbalance Analysis",
    "🧪 Empirical Bias & Hallucination Test Bench"
])

# ==============================================================================
# TAB 1: SENSITIVE COLUMN (PII) DETECTION (TASK U5)
# ==============================================================================
with tab_pii:
    st.markdown(f"### 🕵️ Automated PII & Sensitive Column Audit on `{dataset_name}`")
    st.caption("Evaluates column headers and data values against GDPR, DPDP, and HIPAA sensitive attribute patterns.")

    pii_findings = scan_sensitive_columns(df)

    if not pii_findings:
        st.success("✅ **No Direct High-Risk PII Detected.** The dataset attributes appear to be non-identifying features.")
    else:
        st.warning(f"⚠️ **Identified {len(pii_findings)} Potentially Sensitive Attributes:**")
        pii_df = pd.DataFrame(pii_findings)
        
        # Display formatted table
        st.dataframe(
            pii_df[["column", "risk_category", "risk_level", "detection_method", "reason", "recommendation"]],
            use_container_width=True,
            hide_index=True
        )

        st.markdown("#### 👤 Student Privacy Confirmation & Anonymization Action:")
        for idx, row in enumerate(pii_findings):
            col_c1, col_c2 = st.columns([3, 1])
            with col_c1:
                st.markdown(f"**Attribute `{row['column']}`** ({row['risk_category']}): `{row['recommendation']}`")
            with col_c2:
                confirmed = st.checkbox("Confirm Sensitive", value=True, key=f"pii_{idx}")
                if not confirmed:
                    st.caption("Marked as False Positive by User")

# ==============================================================================
# TAB 2: CLASS IMBALANCE ANALYSIS (TASK U5)
# ==============================================================================
with tab_imbalance:
    st.markdown("### ⚖️ Target Class Imbalance Evaluation")
    st.caption("Detects majority-to-minority distribution skew and prevents the Accuracy Paradox in classification.")

    target_options = list(df.columns)
    default_target = st.session_state.get("target_column", df.columns[-1])
    default_idx = target_options.index(default_target) if default_target in target_options else len(target_options) - 1

    selected_target = st.selectbox(
        "Select Target Column for Imbalance Audit:",
        target_options,
        index=default_idx
    )

    imb_res = analyze_class_imbalance(df, selected_target)

    if imb_res is None or not imb_res["is_applicable"]:
        st.info(f"ℹ️ {imb_res['reason'] if imb_res else 'Select a valid discrete target column.'}")
    else:
        c_i1, c_i2, c_i3, c_i4 = st.columns(4)
        with c_i1:
            st.metric("Total Records", f"{imb_res['total_records']:,}")
        with c_i2:
            st.metric("Imbalance Ratio", f"{imb_res['imbalance_ratio']} : 1", help="Ratio of majority class count to minority class count.")
        with c_i3:
            st.metric("Majority Class", f"{imb_res['majority_class']} ({imb_res['majority_count']})")
        with c_i4:
            st.metric("Minority Class", f"{imb_res['minority_class']} ({imb_res['minority_count']})")

        st.markdown(f"**Severity Level:** `{imb_res['severity']}` – *{imb_res['severity_desc']}*")

        # Visual bar chart
        counts_df = pd.DataFrame({
            "Class": list(imb_res["counts"].keys()),
            "Record Count": list(imb_res["counts"].values()),
            "Percentage": [f"{p}%" for p in imb_res["percentages"].values()]
        })

        fig_imb = px.bar(
            counts_df,
            x="Class",
            y="Record Count",
            text="Percentage",
            color="Class",
            title=f"Target Distribution: '{selected_target}'",
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig_imb.update_layout(margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig_imb, use_container_width=True)

        # Metric guidance box
        st.markdown("#### 🚨 Academic Metric Recommendation:")
        st.info(imb_res["metric_guidance"])

# ==============================================================================
# TAB 3: EMPIRICAL BIAS & HALLUCINATION TEST BENCH (UNIT V)
# ==============================================================================
with tab_bench:
    st.markdown("### 🧪 Empirical Bias & Hallucination Test Bench")
    st.caption("Standardized test battery evaluating query accuracy, code validity, and response latency against mathematical ground truth.")

    if st.button("▶️ Execute Hallucination & Safety Benchmark", type="primary"):
        with st.spinner("Executing empirical test battery against ground truth..."):
            bench_output = run_empirical_hallucination_benchmark(df)
            st.session_state["halluc_bench_res"] = bench_output

    if "halluc_bench_res" in st.session_state:
        res = st.session_state["halluc_bench_res"]
        
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Total Tests Evaluated", res["total_tests"])
        with m2:
            st.metric("Tests Passed", res["passed_tests"])
        with m3:
            st.metric("Empirical Accuracy", f"{res['accuracy_pct']}%")

        st.markdown("#### Test Execution Ledger:")
        st.dataframe(res["results_table"], use_container_width=True, hide_index=True)

        st.markdown("#### 🔬 Documented Failure Cases & Error Analysis:")
        st.markdown("""
        1. **Adversarial Import Injection (Q6):** When prompted to execute system-level operations (`import os`), the AST security visitor interceptor successfully rejected the syntax tree with an unapproved import violation.
        2. **Multi-Feature Continuous Ambiguity:** In datasets with identical numerical properties across multiple columns, zero-shot LLM queries without explicit column references may select the first encountered column rather than the intended domain target.
        3. **Vision LLM Fine-Scale Resolution:** Gemini Vision models can accurately detect distribution curvature (e.g. right-skewness) but occasionally approximate exact numerical bin boundaries compared to raw DataFrame percentiles.
        """)
