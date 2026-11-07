"""
Page: 4_AI_Data_Assistant
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Module U2: LLM + Pandas Data Assistant with AST validation and sandboxed execution.
Unit I: Prompt engineering comparison (Zero-shot vs Few-shot vs Structured).
Unit II: Transformer self-attention architecture and fine-tuning comparison.
"""

import sys
import os
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from modules.llm_assistant import (
    generate_pandas_code,
    explain_execution_output,
    run_prompt_comparison_benchmark,
    generate_transformer_attention_matrix,
    get_fine_tuning_vs_prompting_matrix
)
from modules.code_validator import validate_python_code
from modules.safe_executor import execute_code_safely
from modules.ui_components import render_page_header, render_empty_state_warning
from config.settings import GEMINI_API_KEY

st.set_page_config(page_title="AI Data Assistant - CSV INSIGHT AI", page_icon="💬", layout="wide")

# Load CSS
css_path = ROOT_DIR / "assets" / "styles.css"
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

render_page_header(
    page_title="AI Data Assistant & LLM Studio",
    module_tag="MODULE U2 & UNIT II",
    subtitle="Natural Language Query Synthesis, Strict AST Code Allowlist & Sandboxed Execution"
)

if "df" not in st.session_state or st.session_state["df"] is None:
    render_empty_state_warning()
    st.stop()

df = st.session_state["df"]
dataset_name = st.session_state.get("dataset_name", "Uploaded Dataset")

tab_assistant, tab_prompting, tab_transformer = st.tabs([
    "💬 Natural Language Query Assistant",
    "🧪 Prompt Engineering Comparison (Unit I)",
    "🧠 Transformer Attention & Fine-Tuning (Unit II)"
])

# ==============================================================================
# TAB 1: NATURAL LANGUAGE QUERY ASSISTANT (TASK U2)
# ==============================================================================
with tab_assistant:
    st.markdown(f"### 🤖 Ask Questions about `{dataset_name}`")
    st.caption("The LLM translates your question into Pandas code, validates it against security rules, executes it safely, and explains the output.")

    # API Key Configuration Expander
    with st.expander("🔑 Configure Gemini API Key (Optional)", expanded=False):
        user_key_input = st.text_input(
            "Gemini API Key:",
            value=os.getenv("GEMINI_API_KEY", ""),
            type="password",
            help="Enter your Google Gemini API key to use live cloud inference. If blank, local rule-based reasoning is used."
        )
        if user_key_input:
            os.environ["GEMINI_API_KEY"] = user_key_input
            st.success("API Key updated in session environment!")

    # Quick query buttons
    st.markdown("##### ⚡ Quick Example Questions:")
    q_col1, q_col2, q_col3, q_col4 = st.columns(4)
    preset_query = None
    with q_col1:
        if st.button("📊 Average of all columns", use_container_width=True):
            preset_query = "What is the average value of each numerical column?"
    with q_col2:
        if st.button("🏆 Top 5 records", use_container_width=True):
            preset_query = f"Show the top 5 records sorted by {df.columns[0]}"
    with q_col3:
        if st.button("❓ Column missingness", use_container_width=True):
            preset_query = "Which columns have missing values and how many?"
    with q_col4:
        if st.button("🔗 Feature correlations", use_container_width=True):
            preset_query = "Calculate the correlation matrix between numerical attributes"

    # User query input form
    user_query = st.text_input(
        "Enter your query in plain English:",
        value=preset_query if preset_query else "",
        placeholder="e.g., Which column has the highest variance? Or: Show summary statistics."
    )

    col_btn, col_technique = st.columns([1, 2])
    with col_btn:
        run_query = st.button("🚀 Run AI Query", type="primary", use_container_width=True)
    with col_technique:
        technique = st.selectbox("Prompting Strategy:", ["zero-shot", "few-shot", "structured"], index=0)

    if run_query and user_query:
        with st.spinner("1. Synthesizing Pandas code with LLM..."):
            code, latency, notice = generate_pandas_code(user_query, df, prompt_technique=technique)

        if notice:
            st.info(notice)

        st.markdown("#### 1. Generated Pandas Code:")
        st.code(code, language="python")

        # 2. AST Validation
        with st.spinner("2. Validating code through AST Security Guardrail..."):
            is_valid, violations, _ = validate_python_code(code)

        if not is_valid:
            st.error("❌ **Security Rejection: Code execution blocked by AST validator!**")
            for v in violations:
                st.warning(f"⚠️ {v}")
            st.stop()
        else:
            st.success(f"✅ **AST Security Check Passed** (Zero unauthorized imports or system calls. Synthesis latency: {latency}s)")

        # 3. Controlled Execution
        with st.spinner("3. Executing in isolated sandbox..."):
            exec_ok, raw_res, output_text, exec_err = execute_code_safely(code, df)

        st.markdown("#### 2. Execution Output:")
        if not exec_ok:
            st.error(f"❌ Execution Error: {exec_err}")
        else:
            if isinstance(raw_res, (pd.DataFrame, pd.Series)):
                st.dataframe(raw_res, use_container_width=True)
            else:
                st.markdown(f"```\n{output_text}\n```")

        # 4. Plain-English Explanation
        with st.spinner("4. Synthesizing plain-English explanation..."):
            explanation = explain_execution_output(user_query, code, output_text)

        st.markdown("#### 3. Plain-English AI Explanation:")
        st.info(f"💡 {explanation}")

        # Store in session state chat history
        st.session_state["chat_history"].append({
            "query": user_query,
            "code": code,
            "output": output_text,
            "explanation": explanation
        })

# ==============================================================================
# TAB 2: PROMPT ENGINEERING COMPARISON (UNIT I)
# ==============================================================================
with tab_prompting:
    st.markdown("### 🧪 Unit I: Prompt Engineering Comparison")
    st.caption("Empirical evaluation comparing Zero-Shot, Few-Shot, and Structured prompting on fixed dataset questions.")

    if st.button("▶️ Run Prompt Engineering Benchmark Battery", type="primary"):
        with st.spinner("Running automated prompt comparison battery on active dataset..."):
            benchmark_df = run_prompt_comparison_benchmark(df)
        st.session_state["benchmark_results"] = benchmark_df

    if "benchmark_results" in st.session_state:
        st.markdown("#### Benchmark Results Table:")
        st.dataframe(st.session_state["benchmark_results"], use_container_width=True)

        st.markdown("#### 📊 Architectural Analysis of Prompting Techniques:")
        st.markdown("""
        - **Zero-Shot Prompting:** Sends only the schema context and user question directly. Very low prompt token overhead, but occasionally generates imports or omits assigning to the standard `result` variable.
        - **Few-Shot Prompting:** Supplies 2-3 in-context input-output demonstration pairs. Guarantees higher adherence to assigning `result = ...` and strictly adhering to the allowlist, with a slight increase in latency.
        - **Structured Prompting:** Employs explicit structural constraints (schema contracts, function signatures). Delivers highest AST compliance and deterministic execution outcomes.
        """)

# ==============================================================================
# TAB 3: TRANSFORMER ATTENTION & FINE-TUNING (UNIT II)
# ==============================================================================
with tab_transformer:
    st.markdown("### 🧠 Unit II: Transformer Attention & Learning Paradigms")

    st.markdown("#### 1. Educational Self-Attention Mechanism")
    st.latex(r"\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V")
    st.markdown(r"""
    In a Transformer-based LLM (such as Gemini or GPT), self-attention computes how much every token in the 
    dataset prompt attends to every other token. The dot product $Q K^T$ measures raw semantic similarity, 
    scaled by $\sqrt{d_k}$ to prevent gradient saturation, followed by a row-wise Softmax to form probability weights.
    """)

    sample_tokens = ["What", "is", "the", "average", "value", "of", "Age", "?"]
    attn_weights = generate_transformer_attention_matrix(sample_tokens)

    fig_attn = px.imshow(
        attn_weights,
        x=sample_tokens,
        y=sample_tokens,
        color_continuous_scale="Viridis",
        title="Simulated Multi-Head Self-Attention Weight Matrix (Softmax Probabilities)",
        text_auto=True
    )
    fig_attn.update_layout(height=450, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_attn, use_container_width=True)

    st.markdown("---")
    st.markdown("#### 2. Prompting vs. Fine-Tuning vs. Synthetic Data Generation")
    ft_matrix = get_fine_tuning_vs_prompting_matrix()
    st.dataframe(ft_matrix, use_container_width=True, hide_index=True)
