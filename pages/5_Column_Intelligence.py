"""
Page: 5_Column_Intelligence
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Task U3: Group similar columns with Sentence-BERT embeddings;
let a vision-capable LLM interpret dataset charts.
Unit III Syllabus: Contrast GPT-style autoregressive models with BERT bidirectional models.
"""

import sys
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from modules.embeddings import (
    compute_column_embeddings,
    compute_similarity_matrix,
    cluster_similar_columns,
    get_gpt_vs_bert_architectural_comparison
)
from modules.visualization import create_static_distribution_plot
from modules.vision_analyzer import interpret_chart_with_vision
from modules.ui_components import render_page_header, render_empty_state_warning

st.set_page_config(page_title="Column Intelligence - CSV INSIGHT AI", page_icon="🧠", layout="wide")

# Load CSS
css_path = ROOT_DIR / "assets" / "styles.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

render_page_header(
    page_title="Column Intelligence & Multimodal Vision",
    module_tag="MODULE U3 & UNIT III",
    subtitle="Sentence-BERT 384-d Column Semantic Clustering & Gemini Multimodal Vision Chart Reasoning"
)

if "df" not in st.session_state or st.session_state["df"] is None:
    render_empty_state_warning()
    st.stop()

df = st.session_state["df"]
dataset_name = st.session_state.get("dataset_name", "Uploaded Dataset")

tab_bert, tab_vision, tab_models = st.tabs([
    "🔗 Sentence-BERT Column Clustering",
    "👁️ Gemini Multimodal Vision Chart Reader",
    "📖 Unit III: GPT vs. BERT Architecture"
])

# ==============================================================================
# TAB 1: SENTENCE-BERT COLUMN CLUSTERING (TASK U3)
# ==============================================================================
with tab_bert:
    st.markdown("### 🔗 Semantic Column Grouping via Sentence-BERT (`all-MiniLM-L6-v2`)")
    st.caption(
        "Encodes column names, data types, and non-sensitive sample values into 384-dimensional dense vectors. "
        "Cosine similarity measures semantic relatedness."
    )

    # Compute or retrieve cached embeddings
    if "sbert_data" not in st.session_state or st.session_state.get("sbert_dataset") != dataset_name:
        with st.spinner("Generating 384-dimensional Sentence-BERT embeddings..."):
            cols, emb_matrix, desc_dict = compute_column_embeddings(df)
            sim_matrix = compute_similarity_matrix(emb_matrix)
            st.session_state["sbert_data"] = {
                "columns": cols,
                "embeddings": emb_matrix,
                "descriptions": desc_dict,
                "sim_matrix": sim_matrix
            }
            st.session_state["sbert_dataset"] = dataset_name

    sbert = st.session_state["sbert_data"]
    cols = sbert["columns"]
    sim_matrix = sbert["sim_matrix"]
    desc_dict = sbert["descriptions"]

    # Threshold slider
    col_slide, col_count = st.columns([3, 1])
    with col_slide:
        sim_threshold = st.slider(
            "Cosine Similarity Threshold:",
            min_value=0.40,
            max_value=0.95,
            value=0.65,
            step=0.05,
            help="Columns with cosine similarity score above this threshold are grouped together."
        )

    # Cluster columns
    clusters = cluster_similar_columns(cols, sim_matrix, desc_dict, threshold=sim_threshold)

    # Cosine Similarity Heatmap
    st.markdown("#### Pairwise Semantic Cosine Similarity Heatmap:")
    fig_sim = px.imshow(
        sim_matrix,
        x=cols,
        y=cols,
        color_continuous_scale="Viridis",
        zmin=0.0,
        zmax=1.0,
        text_auto=True,
        title="Pairwise Column Cosine Similarity Matrix (Sentence-BERT)"
    )
    fig_sim.update_layout(height=max(380, len(cols) * 35), margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_sim, use_container_width=True)

    # Semantic Grouping Table
    st.markdown(rf"#### Semantic Matches (Threshold $\ge$ {sim_threshold}):")
    cluster_records = []
    for c in clusters:
        if c["matches"]:
            match_str = ", ".join([f"{m['related_column']} ({m['similarity_score']})" for m in c["matches"]])
        else:
            match_str = "None (Distinct semantic feature)"
        cluster_records.append({
            "Column Name": c["column"],
            "Semantic Description": c["description"],
            "Semantic Matches (Similarity Score)": match_str
        })
    st.dataframe(pd.DataFrame(cluster_records), use_container_width=True, hide_index=True)
    st.warning("⚠️ **Academic Notice:** Do not assume similarly named columns always have identical meanings. Inspect domain context.")

# ==============================================================================
# TAB 2: GEMINI MULTIMODAL VISION CHART READER (TASK U3)
# ==============================================================================
with tab_vision:
    st.markdown("### 👁️ Gemini Multimodal Vision Chart Reader")
    st.caption("Converts rendered dataset charts into image buffers and prompts Gemini Vision to identify skewness, modality, and anomalies.")

    col_choice = st.selectbox("Select Column Chart to Visually Interpret:", cols, index=0)

    # Generate static Matplotlib chart bytes
    with st.spinner(f"Rendering high-resolution distribution plot for '{col_choice}'..."):
        image_bytes = create_static_distribution_plot(df, col_choice)

    chart_col, interp_col = st.columns([1, 1])

    with chart_col:
        st.markdown("#### Rendered Dataset Chart:")
        st.image(image_bytes, caption=f"Static distribution of {col_choice}", use_container_width=True)

    with interp_col:
        st.markdown("#### AI Vision Interpretation:")
        if st.button("🚀 Analyze Chart with Vision LLM", type="primary", use_container_width=True):
            with st.spinner("Streaming chart pixels to Gemini Multimodal Vision model..."):
                vision_res = interpret_chart_with_vision(image_bytes, column_name=col_choice, df=df)
            st.session_state[f"vision_res_{col_choice}"] = vision_res

        cached_vision = st.session_state.get(f"vision_res_{col_choice}")
        if cached_vision:
            st.success(f"**Inference Engine:** `{cached_vision['engine']}`")
            st.markdown(cached_vision["interpretation"])
            st.info(f"💡 {cached_vision['warning']}")
        else:
            st.info("Click the button above to run Gemini Vision chart interpretation.")

# ==============================================================================
# TAB 3: UNIT III: GPT VS. BERT ARCHITECTURAL FOUNDATIONS
# ==============================================================================
with tab_models:
    st.markdown("### 📖 Unit III: GPT-Style vs. BERT-Family Architectures")
    st.caption("Deep technical comparison between Causal Autoregressive Decoders and Masked Bidirectional Encoders.")

    gpt_bert_df = get_gpt_vs_bert_architectural_comparison()
    st.dataframe(gpt_bert_df, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("#### 🔬 How Both Paradigms Are Integrated in P10:")
    c_gpt, c_bert = st.columns(2)
    with c_gpt:
        st.markdown(r"""
        **1. GPT-Style Autoregressive Generation (Module U2):**
        - Operates sequentially: $P(w_1, w_2, \dots, w_T) = \prod_{t=1}^T P(w_t \mid w_{<t})$
        - Powers the **AI Data Assistant** by synthesizing executable Pandas code from natural language queries and generating plain-English summaries.
        """)
    with c_bert:
        st.markdown(r"""
        **2. BERT-Style Bidirectional Representation (Module U3):**
        - Operates simultaneously across both left and right context: $h_i = \text{Encoder}(w_1, \dots, w_N)$
        - Powers **Sentence-BERT (`all-MiniLM-L6-v2`)** to create dense 384-dimensional feature representations for semantic column grouping.
        """)
