"""
Page: 6_Synthetic_Data_Lab
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Task U4: Generate synthetic rows with PyTorch CTGAN; compare real vs. synthetic distributions.
Unit IV Syllabus: PyTorch tabular GAN integration & Generative AI visual infographic card.
"""

import sys
from pathlib import Path
import streamlit as st
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from modules.ctgan_generator import (
    prepare_data_for_ctgan,
    train_ctgan_synthesizer,
    generate_synthetic_samples
)
from modules.synthetic_evaluator import (
    evaluate_numerical_columns,
    evaluate_categorical_columns,
    evaluate_correlation_difference,
    plot_real_vs_synthetic_overlay
)
from modules.image_generator import (
    generate_dataset_infographic_card,
    get_diffusion_model_metadata
)
from modules.data_profiler import profile_dataset
from modules.ml_recommender import recommend_ml_task

st.set_page_config(page_title="Synthetic Data Lab - CSV INSIGHT AI", page_icon="🧬", layout="wide")

st.title("🧬 Synthetic Data Lab & Generative AI Studio")
st.caption("P10 – Module U4 & Unit IV: PyTorch CTGAN Tabular Generation, KS-Fidelity Metrics & Visual Infographic Synthesis")

if "df" not in st.session_state or st.session_state["df"] is None:
    st.warning("⚠️ No dataset loaded. Please load a dataset from the Home page.")
    st.stop()

df = st.session_state["df"]
dataset_name = st.session_state.get("dataset_name", "Uploaded Dataset")
profile = profile_dataset(df)

tab_train, tab_eval, tab_infographic = st.tabs([
    "🧬 CTGAN Tabular Generation",
    "📊 Real vs. Synthetic Statistical Evaluation",
    "🎨 Unit IV: Generative AI Visual Infographic"
])

# ==============================================================================
# TAB 1: CTGAN TABULAR GENERATION (TASK U4)
# ==============================================================================
with tab_train:
    st.markdown(f"### 🧬 PyTorch CTGAN Training on `{dataset_name}`")
    st.caption("Conditional GAN architecture using mode-specific normalization for mixed-type tabular data.")

    # Column selector
    avail_cols = list(df.columns)
    selected_cols = st.multiselect(
        "Select Columns to Synthesize:",
        avail_cols,
        default=avail_cols[:min(8, len(avail_cols))],
        help="Select attributes to model with CTGAN. Capped to prevent CPU timeouts."
    )

    c_cfg1, c_cfg2 = st.columns(2)
    with c_cfg1:
        epochs = st.slider(
            "Training Epochs:",
            min_value=5,
            max_value=35,
            value=15,
            step=5,
            help="Higher epochs improve fidelity but increase CPU training time. 15-20 is optimal for fast demo."
        )
    with c_cfg2:
        num_synth_rows = st.slider(
            "Synthetic Rows to Generate:",
            min_value=25,
            max_value=500,
            value=100,
            step=25,
            help="Number of synthetic records to sample from the generator."
        )

    if st.button("🚀 Train CTGAN & Generate Synthetic Rows", type="primary", use_container_width=True):
        if not selected_cols:
            st.error("Please select at least one column to train CTGAN.")
        else:
            with st.spinner("1. Sanitizing columns and preparing PyTorch dataloader..."):
                clean_train_df, disc_cols, num_cols = prepare_data_for_ctgan(df, selected_columns=selected_cols)

            st.info(f"Training on {len(clean_train_df)} rows across {len(selected_cols)} features ({len(disc_cols)} discrete, {len(num_cols)} continuous).")

            with st.spinner(f"2. Training CTGAN Generator & Discriminator for {epochs} epochs on CPU..."):
                model, train_time, err = train_ctgan_synthesizer(clean_train_df, discrete_columns=disc_cols, epochs=epochs)

            if err:
                st.error(err)
            else:
                st.success(f"✅ CTGAN Training Complete in **{train_time}s**!")
                with st.spinner(f"3. Sampling {num_synth_rows} synthetic records..."):
                    synth_df, samp_err = generate_synthetic_samples(model, num_rows=num_synth_rows, reference_df=clean_train_df)

                if samp_err:
                    st.error(samp_err)
                else:
                    st.session_state["synth_df"] = synth_df
                    st.session_state["clean_train_df"] = clean_train_df
                    st.session_state["synth_cols_num"] = num_cols
                    st.session_state["synth_cols_disc"] = disc_cols

    # Display synthetic records if generated
    if "synth_df" in st.session_state and st.session_state["synth_df"] is not None:
        synth_df = st.session_state["synth_df"]
        st.markdown(f"#### 📋 Generated Synthetic Records ({len(synth_df)} rows):")
        st.dataframe(synth_df.head(25), use_container_width=True)

        # Download button
        csv_bytes = synth_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Synthetic CSV",
            data=csv_bytes,
            file_name=f"synthetic_{dataset_name.replace(' ', '_').lower()}.csv",
            mime="text/csv",
            type="primary"
        )
        st.warning(
            "⚠️ **Academic Privacy Notice:** Statistical similarity does NOT guarantee absolute differential privacy. "
            "Synthetic records can occasionally reflect training distribution clusters (membership inference considerations)."
        )

# ==============================================================================
# TAB 2: REAL VS. SYNTHETIC STATISTICAL EVALUATION (TASK U4)
# ==============================================================================
with tab_eval:
    st.markdown("### 📊 Real vs. Synthetic Statistical Evaluation")
    st.caption("Rigorous empirical comparison: Kolmogorov-Smirnov (KS) two-sample tests, JS-divergence, and correlation deltas.")

    if "synth_df" not in st.session_state or st.session_state["synth_df"] is None:
        st.info("Please train CTGAN and generate synthetic rows in Tab 1 first to run the evaluation.")
    else:
        synth_df = st.session_state["synth_df"]
        real_df = st.session_state["clean_train_df"]
        num_cols = st.session_state.get("synth_cols_num", [])
        disc_cols = st.session_state.get("synth_cols_disc", [])

        # 1. Numerical KS Evaluation
        if num_cols:
            st.markdown("#### 1. Continuous Distribution Fidelity (Kolmogorov-Smirnov Test):")
            st.latex(r"D_{\text{KS}} = \sup_x |F_{\text{real}}(x) - F_{\text{synth}}(x)|")
            st.caption("KS Statistic: 0.0 indicates identical cumulative distributions; values ≤ 0.20 represent high tabular fidelity.")

            ks_df = evaluate_numerical_columns(real_df, synth_df, num_cols)
            st.dataframe(ks_df, use_container_width=True, hide_index=True)

        # 2. Categorical JS Evaluation
        if disc_cols:
            st.markdown("#### 2. Categorical Distribution Fidelity (Jensen-Shannon Divergence):")
            st.caption("JS Divergence: 0.0 indicates identical category proportions.")
            js_df = evaluate_categorical_columns(real_df, synth_df, disc_cols)
            st.dataframe(js_df, use_container_width=True, hide_index=True)

        # 3. Correlation Difference Norm
        if len(num_cols) >= 2:
            st.markdown("#### 3. Inter-Feature Correlation Preservation:")
            corr_mae, corr_delta = evaluate_correlation_difference(real_df, synth_df, num_cols)
            st.metric("Correlation Matrix Mean Absolute Error (MAE)", f"{corr_mae:.3f}", help="Average difference between real and synthetic Pearson correlation coefficients.")

        # 4. Interactive Overlay Distribution Plot
        st.markdown("---")
        st.markdown("#### 4. Visual Distribution Overlay (Real vs. Synthetic):")
        all_synth_cols = list(synth_df.columns)
        chosen_col = st.selectbox("Select Feature to Overlay:", all_synth_cols, index=0)
        fig_overlay = plot_real_vs_synthetic_overlay(real_df, synth_df, chosen_col)
        st.plotly_chart(fig_overlay, use_container_width=True)

# ==============================================================================
# TAB 3: UNIT IV GENERATIVE AI VISUAL INFOGRAPHIC
# ==============================================================================
with tab_infographic:
    st.markdown("### 🎨 Unit IV: Generative AI Visual Infographic Card")
    st.caption("Generative visual representation synthesizing dataset insights, KPIs, and recommendations into an illustrative asset.")

    rec = recommend_ml_task(df, target_column=df.columns[-1])
    top_insight = (
        f"The {dataset_name} profile comprises {len(df):,} records with a data quality health score of "
        f"{profile['quality_score']['score']}/100. Key modeling recommendation points to {rec['suggested_task']}. "
        f"CTGAN synthesis preserves continuous feature distributions with bounded Kolmogorov-Smirnov fidelity."
    )

    if st.button("🖼️ Synthesize Dataset Intelligence Infographic", type="primary"):
        with st.spinner("Generating illustrative dataset intelligence infographic card..."):
            card_bytes = generate_dataset_infographic_card(
                dataset_name=dataset_name,
                total_rows=len(df),
                total_cols=len(df.columns),
                quality_score=profile["quality_score"]["score"],
                recommended_task=rec["suggested_task"],
                top_insight=top_insight
            )
            st.session_state["infographic_card"] = card_bytes

    if "infographic_card" in st.session_state:
        st.markdown("#### Synthesized Generative Infographic Asset:")
        st.image(st.session_state["infographic_card"], caption=f"Generative Infographic: {dataset_name}", use_container_width=True)
        st.download_button(
            label="📥 Download Infographic (PNG)",
            data=st.session_state["infographic_card"],
            file_name=f"{dataset_name.replace(' ', '_').lower()}_infographic.png",
            mime="image/png"
        )

    st.markdown("---")
    st.markdown("#### 📜 Generative Model Documentation & License Card:")
    meta = get_diffusion_model_metadata()
    st.markdown(f"- **Architecture / Engine:** `{meta['model_name']}`")
    st.markdown(f"- **Methodology:** `{meta['method']}`")
    st.markdown(f"- **Modality:** `{meta['modality']}`")
    st.markdown(f"- **License:** `{meta['license']}`")
    st.markdown(f"- **Hardware Profile:** `{meta['hardware_profile']}`")
    st.markdown("##### Technical Limitations:")
    for lim in meta["limitations"]:
        st.markdown(f"- {lim}")
