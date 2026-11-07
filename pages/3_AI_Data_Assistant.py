"""
Page: 4_AI_Data_Assistant
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Module U2: LLM + Pandas Data Assistant with AST validation and sandboxed execution.
Allows querying any dataset in natural language with guaranteed security guardrails.
"""

import sys
import os
from pathlib import Path
import streamlit as st
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from modules.llm_assistant import (
    generate_pandas_code,
    explain_execution_output
)
from modules.code_validator import validate_python_code
from modules.safe_executor import execute_code_safely
from modules.ui_components import render_page_header, render_empty_state_warning

try:
    st.set_page_config(page_title="AI Data Assistant - DataPulse AI", page_icon="💬", layout="wide")
except Exception:
    pass

render_page_header(
    page_title="AI Data Assistant & LLM Studio",
    module_tag="MODULE U2",
    subtitle="Natural Language Query Synthesis, Strict AST Code Allowlist & Sandboxed Execution"
)

if "df" not in st.session_state or st.session_state["df"] is None:
    render_empty_state_warning()
    st.stop()

df = st.session_state["df"]
dataset_name = st.session_state.get("dataset_name", "Uploaded Dataset")

# API Key Configuration Expander
with st.expander("🔑 Configure Gemini API Key (Optional)", expanded=False):
    user_key_input = st.text_input(
        "Gemini API Key:",
        value=os.getenv("GEMINI_API_KEY", ""),
        type="password",
        help="Enter your Google Gemini API key for live LLM inference. If blank, local rule-based reasoning is used."
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
        st.success(f"✅ **AST Security Check Passed** (Allowlist verified: zero dangerous imports or disk writes. Latency: {latency}s)")

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

# Chat History Expander
if st.session_state.get("chat_history"):
    with st.expander(f"📜 Query History ({len(st.session_state['chat_history'])} queries executed)", expanded=False):
        for i, h in enumerate(reversed(st.session_state["chat_history"])):
            st.markdown(f"**Query {len(st.session_state['chat_history']) - i}:** `{h['query']}`")
            st.markdown(f"> {h['explanation']}")
            st.markdown("---")
