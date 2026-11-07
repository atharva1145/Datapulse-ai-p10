"""
Page: 3_ML_Recommendations
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Task U1: Recommend ML task and candidate algorithms.
Unit I Syllabus: 10-stage ML lifecycle guide, GenAI vs Discriminative AI,
and empirical class probability distribution visualization.
"""

import sys
from pathlib import Path
import streamlit as st
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from modules.ml_recommender import recommend_ml_task
from modules.lifecycle import get_ml_lifecycle_stages, get_genai_vs_discriminative_comparison
from modules.visualization import plot_class_probability_distribution

st.set_page_config(page_title="ML Recommender - CSV INSIGHT AI", page_icon="🤖", layout="wide")

# Load CSS
css_path = ROOT_DIR / "assets" / "styles.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🤖 ML Task Recommender & Lifecycle Studio")
st.caption("P10 – Module U1 & Unit I: Machine Learning Task Recommendation, Candidate Algorithms & 10-Stage Lifecycle")

if "df" not in st.session_state or st.session_state["df"] is None:
    st.warning("⚠️ No dataset loaded. Please load a dataset from the Home page.")
    st.stop()

df = st.session_state["df"]
dataset_name = st.session_state.get("dataset_name", "Uploaded Dataset")

tab_recommender, tab_lifecycle, tab_unit1 = st.tabs([
    "🎯 ML Task & Algorithm Recommendation",
    "🔄 10-Stage ML Lifecycle Roadmap",
    "📚 Unit I Theoretical Foundations (GenAI vs Discriminative)"
])

# ==============================================================================
# TAB 1: ML TASK RECOMMENDATION
# ==============================================================================
with tab_recommender:
    st.markdown("### 🎯 Task Recommendation Configuration")
    
    col_target, col_info = st.columns([1, 2])
    with col_target:
        target_options = ["None (Unsupervised / Clustering)"] + list(df.columns)
        current_target = st.session_state.get("target_column", df.columns[-1])
        default_index = target_options.index(current_target) if current_target in target_options else len(target_options) - 1
        
        selected_target_choice = st.selectbox(
            "Select Prediction Target Column:",
            target_options,
            index=default_index,
            help="Choose which variable you wish to predict, or select 'None' for unsupervised analysis."
        )
        target_val = None if selected_target_choice.startswith("None") else selected_target_choice
        st.session_state["target_column"] = target_val

    # Run recommendation engine
    rec = recommend_ml_task(df, target_column=target_val)

    with col_info:
        st.success(f"**Recommended Learning Paradigm:** `{rec['learning_type']}`")
        st.markdown(f"### **Suggested Task:** {rec['suggested_task']}")
        st.write(rec["reason"])

    st.markdown("---")
    st.markdown("### 🛠️ Candidate Machine Learning Algorithms")
    algo_df = pd.DataFrame(rec["candidate_algorithms"])
    algo_df.columns = ["Algorithm", "Architectural Role & Justification"]
    st.dataframe(algo_df, use_container_width=True, hide_index=True)

    c_assump, c_limits = st.columns(2)
    with c_assump:
        st.markdown("#### 📌 Key Modeling Assumptions")
        for a in rec.get("assumptions", []):
            st.markdown(f"- {a}")

    with c_limits:
        st.markdown("#### ⚠️ Technical Limitations & Caveats")
        for l in rec.get("limitations", []):
            st.markdown(f"- {l}")

    st.markdown("---")
    st.markdown("#### 💡 Note on Reinforcement Learning (RL)")
    st.warning(f"**Academic Notice:** {rec.get('rl_note')}")

# ==============================================================================
# TAB 2: 10-STAGE ML LIFECYCLE ROADMAP
# ==============================================================================
with tab_lifecycle:
    st.markdown("### 🔄 End-to-End Machine Learning Lifecycle")
    st.caption("Customized sequentially for the uploaded dataset's features, sample size, and recommended task.")

    stages = get_ml_lifecycle_stages(df, target_col=target_val if target_val else "None", ml_task_info=rec)

    for stage in stages:
        with st.expander(f"**Stage {stage['step']}: {stage['icon']} {stage['name']}**", expanded=(stage['step'] <= 3)):
            st.markdown(f"**General Objective:** {stage['objective']}")
            st.markdown(f"**👉 Action on `{dataset_name}`:** {stage['dataset_action']}")

# ==============================================================================
# TAB 3: UNIT I SYLLABUS FOUNDATIONS
# ==============================================================================
with tab_unit1:
    st.markdown("### 📚 Unit I – Foundations of Generative AI")
    
    st.markdown("#### 1. Generative AI vs. Discriminative AI Theoretical Comparison")
    gen_disc_df = get_genai_vs_discriminative_comparison()
    st.dataframe(gen_disc_df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("#### 2. Empirical Probability Distribution Visualization")
    st.caption(
        "Grounded in real dataset frequencies: "
        "P(C_k) = N_k / N. Shows prior probabilities without fabricated model confidence."
    )
    if target_val and target_val in df.columns:
        fig_prob = plot_class_probability_distribution(df, target_val)
        st.plotly_chart(fig_prob, use_container_width=True)
    else:
        # Fallback to first categorical or discrete column
        discrete_candidates = [c for c in df.columns if df[c].nunique() <= 10]
        if discrete_candidates:
            fallback_col = discrete_candidates[0]
            st.info(f"Showing class probabilities for discrete column `{fallback_col}`:")
            fig_prob = plot_class_probability_distribution(df, fallback_col)
            st.plotly_chart(fig_prob, use_container_width=True)
        else:
            st.info("Select a discrete or categorical target column above to visualize its prior probability distribution.")
