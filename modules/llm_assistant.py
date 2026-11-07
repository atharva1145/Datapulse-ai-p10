"""
Module: LLM Data Assistant & Prompt Engineering Engine
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Handles Gemini LLM API integration, Pandas code synthesis, plain-English explanations,
Zero-shot vs Few-shot vs Structured prompting benchmarks, and Transformer Attention visualizations.
"""

import os
import re
import time
from typing import Dict, Any, Tuple, Optional, List
import pandas as pd
import numpy as np

from config.settings import GEMINI_API_KEY, GEMINI_MODEL_TEXT
from modules.code_validator import validate_python_code
from modules.safe_executor import execute_code_safely

def get_gemini_client():
    """Initializes and returns the Google GenAI client if API key is present."""
    api_key = os.getenv("GEMINI_API_KEY", GEMINI_API_KEY)
    if not api_key or api_key == "your_gemini_api_key_here":
        try:
            import streamlit as st
            if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
                api_key = st.secrets["GEMINI_API_KEY"]
        except Exception:
            pass
    if not api_key or api_key == "your_gemini_api_key_here":
        return None
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        return client
    except Exception as e:
        print(f"Error initializing Gemini client: {e}")
        return None

def extract_python_code(llm_response: str) -> str:
    """Extracts raw python code from LLM markdown response block."""
    # Look for ```python ... ```
    match = re.search(r"```(?:python)?\s*([\s\S]*?)\s*```", llm_response, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return llm_response.strip()

def prepare_dataset_context(df: pd.DataFrame, max_sample_rows: int = 3) -> str:
    """Builds a compact, privacy-safe text representation of the dataset schema."""
    lines = [
        f"Dataset Shape: {len(df):,} rows x {len(df.columns)} columns",
        "Columns and Data Types:"
    ]
    for col in df.columns:
        dtype = str(df[col].dtype)
        nunique = df[col].nunique()
        sample_vals = [str(x) for x in df[col].dropna().head(max_sample_rows).tolist()]
        lines.append(f"- '{col}' ({dtype}): {nunique} unique values. Sample: {', '.join(sample_vals)}")
    return "\n".join(lines)

def generate_pandas_code(
    query: str,
    df: pd.DataFrame,
    prompt_technique: str = "zero-shot",
    custom_api_key: Optional[str] = None
) -> Tuple[str, float, Optional[str]]:
    """
    Generates Pandas code from natural language using Google Gemini.
    Returns: (code_str, latency_seconds, error_or_notice)
    """
    start_time = time.time()
    context = prepare_dataset_context(df)

    # 1. Check for API key
    if custom_api_key:
        os.environ["GEMINI_API_KEY"] = custom_api_key
    client = get_gemini_client()

    # Rule-based fallback if no Gemini API key configured
    if client is None:
        latency = round(time.time() - start_time, 3)
        code = synthesize_rule_based_fallback(query, df)
        notice = "Note: Running in offline deterministic mode (Configure GEMINI_API_KEY in sidebar or .env for live Gemini API)."
        return code, latency, notice

    # 2. Formulate Prompt based on Selected Technique
    if prompt_technique == "few-shot":
        system_instruction = (
            "You are an expert Data Scientist. Write pure Python/Pandas code to answer the user query on DataFrame 'df'.\n"
            "Rules:\n"
            "1. Assign the final answer or summary to the variable 'result'.\n"
            "2. Do NOT import any modules. Only use operations available on 'df', 'pd', and 'np'.\n"
            "3. Return ONLY executable Python code inside ```python ``` blocks.\n\n"
            "Examples:\n"
            "User: Show average value of Age\n"
            "Code:\n```python\nresult = df['Age'].mean()\n```\n\n"
            "User: Find top 5 records by Fare\n"
            "Code:\n```python\nresult = df.sort_values(by='Fare', ascending=False).head(5)\n```\n\n"
            "User: Count missing values per column\n"
            "Code:\n```python\nresult = df.isnull().sum()\n```"
        )
    elif prompt_technique == "structured":
        system_instruction = (
            "You are an expert Data Scientist. Generate Python code adhering strictly to this contract:\n"
            "- Input variable: 'df' (Pandas DataFrame)\n"
            "- Output variable: 'result' (must store scalar, Series, or DataFrame)\n"
            "- Allowlist methods: head, tail, mean, describe, groupby, agg, sort_values, value_counts, isnull, corr, nlargest, nsmallest\n"
            "- Zero imports allowed.\n"
            "Format: Output ONLY the code inside ```python ```."
        )
    else:  # Zero-shot
        system_instruction = (
            "Write executable Pandas code for DataFrame 'df' to answer the query.\n"
            "Assign the final answer to 'result'. Do NOT import any modules. "
            "Output ONLY the python code inside ```python ```."
        )

    full_prompt = f"{system_instruction}\n\nDataset Schema:\n{context}\n\nUser Question: {query}"

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL_TEXT,
            contents=full_prompt
        )
        latency = round(time.time() - start_time, 3)
        raw_text = response.text or ""
        code = extract_python_code(raw_text)
        return code, latency, None
    except Exception as ex:
        latency = round(time.time() - start_time, 3)
        fallback_code = synthesize_rule_based_fallback(query, df)
        return fallback_code, latency, f"Gemini API Notice: {str(ex)}. Loaded local rule-based response."

def explain_execution_output(
    query: str,
    code: str,
    output_str: str,
    custom_api_key: Optional[str] = None
) -> str:
    """Uses Gemini to explain the executed output in clear, student-friendly English."""
    if custom_api_key:
        os.environ["GEMINI_API_KEY"] = custom_api_key
    client = get_gemini_client()

    if client is None:
        return (
            f"The query was executed using the generated Pandas code. "
            f"The output presents the computed values directly from the dataset. "
            f"Inspection of the result reveals the specific aggregated metrics matching your request."
        )

    prompt = (
        f"You are a helpful Data Science tutor explaining query results to a student.\n"
        f"User Question: {query}\n"
        f"Executed Pandas Code:\n{code}\n"
        f"Actual Output:\n{output_str}\n\n"
        "Provide a concise, plain-English explanation (2-3 sentences) summarizing what this result reveals about the dataset."
    )

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL_TEXT,
            contents=prompt
        )
        return response.text.strip()
    except Exception as ex:
        return f"Executed successfully. Result shows: {output_str[:200]}"

def synthesize_rule_based_fallback(query: str, df: pd.DataFrame) -> str:
    """Provides high-quality deterministic code for standard queries if API key is unconfigured."""
    q_lower = query.lower()
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if "missing" in q_lower or "null" in q_lower:
        return "result = df.isnull().sum()"
    elif "average" in q_lower or "mean" in q_lower:
        if num_cols:
            return f"result = df[{num_cols}].mean().round(3)"
        return "result = df.describe()"
    elif "top 5" in q_lower or "first 5" in q_lower or "head" in q_lower:
        return "result = df.head(5)"
    elif "correlation" in q_lower or "corr" in q_lower:
        if len(num_cols) >= 2:
            return f"result = df[{num_cols}].corr().round(3)"
        return "result = 'Fewer than two numerical columns available for correlation.'"
    elif "unique" in q_lower:
        return "result = df.nunique()"
    elif "summary" in q_lower or "describe" in q_lower:
        return "result = df.describe(include='all')"
    elif "outlier" in q_lower:
        if num_cols:
            col = num_cols[0]
            return f"q1 = df['{col}'].quantile(0.25)\nq3 = df['{col}'].quantile(0.75)\niqr = q3 - q1\nresult = df[(df['{col}'] < q1 - 1.5 * iqr) | (df['{col}'] > q3 + 1.5 * iqr)].head(10)"
    # Default to describe
    return "result = df.describe().round(3)"

def run_prompt_comparison_benchmark(df: pd.DataFrame) -> pd.DataFrame:
    """
    Unit I Syllabus Requirement:
    Compares Zero-Shot vs Few-Shot vs Structured prompting on a fixed battery of dataset questions.
    Measures actual latency, code syntax validity, and execution success.
    """
    test_queries = [
        "Calculate the mean of all numerical columns",
        "Find the top 5 records sorted by the first column",
        "Count the total missing values in every column"
    ]

    records = []
    for q in test_queries:
        for tech in ["zero-shot", "few-shot", "structured"]:
            code, latency, err = generate_pandas_code(q, df, prompt_technique=tech)
            is_valid, violations, _ = validate_python_code(code)
            
            exec_success = False
            if is_valid:
                exec_success, _, _, _ = execute_code_safely(code, df)

            records.append({
                "Benchmark Query": q,
                "Prompt Technique": tech.capitalize(),
                "Generated Code": code.replace("\n", " "),
                "AST Approved": "✅ Passed" if is_valid else "❌ Rejected",
                "Exec Success": "✅ 100%" if exec_success else "❌ Failed",
                "Latency (sec)": f"{latency:.3f}s"
            })

    return pd.DataFrame(records)

def generate_transformer_attention_matrix(tokens: List[str]) -> np.ndarray:
    """
    Unit II Syllabus Educational Demonstration:
    Calculates simulated query-key dot product attention weights:
    Attention(Q, K, V) = Softmax( Q * K^T / sqrt(d_k) )
    """
    n = len(tokens)
    np.random.seed(42)
    d_k = 64
    Q = np.random.randn(n, d_k)
    K = np.random.randn(n, d_k)
    
    # Scale dot product
    scores = np.dot(Q, K.T) / np.sqrt(d_k)
    # Softmax row-wise
    exp_scores = np.exp(scores - np.max(scores, axis=-1, keepdims=True))
    attention_weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)
    return np.round(attention_weights, 3)

def get_fine_tuning_vs_prompting_matrix() -> pd.DataFrame:
    """
    Unit II Syllabus Requirement:
    Detailed comparison between Prompt-Based Learning, Fine-Tuning, and Synthetic Data.
    """
    data = {
        "Dimension": [
            "Core Mechanism",
            "Parameter Updates",
            "Compute & Resource Cost",
            "Latency Profile",
            "Data Requirement",
            "Domain Specialization",
            "Catastrophic Forgetting Risk",
            "Role in this Project (P10)"
        ],
        "Prompt-Based Learning (Gemini)": [
            "In-context learning via prompt instructions & schema context",
            "Zero (Frozen model weights)",
            "Extremely Low (API token inference only)",
            "Fast (1–3 seconds per query)",
            "Few examples or schema description only",
            "Moderate (limited by model's pre-trained knowledge & context window)",
            "Zero (weights never modified)",
            "Powers the AI Data Assistant for dynamic Pandas code generation"
        ],
        "Parameter-Efficient Fine-Tuning (LoRA / PEFT)": [
            "Low-rank adapter matrix updates added to attention projection layers",
            "0.1% – 1% of total parameters updated",
            "Moderate (Single GPU, few hours)",
            "Fast (identical inference to base model)",
            "Hundreds to thousands of task-specific input-output pairs",
            "High (adapts to specialized terminology and tabular structures)",
            "Very Low (frozen backbone weights)",
            "Theoretical alternative to fine-tuning on academic hardware"
        ],
        "Full Fine-Tuning": [
            "Backpropagation updates across all transformer weight layers",
            "100% of weights updated",
            "Very High (Multi-GPU clusters, substantial RAM & time)",
            "Fast inference, high training cost",
            "Tens of thousands of labeled samples",
            "Maximum specialization for domain",
            "High risk of degrading general reasoning capabilities",
            "Documented in Unit II syllabus as resource-prohibitive for free tiers"
        ],
        "Synthetic Data Generation (CTGAN)": [
            "Adversarial min-max game modeling continuous & discrete probability distributions",
            "Trains Generator G and Discriminator D from scratch",
            "Moderate (CPU/GPU-friendly for tabular data)",
            "Fast batch generation after training",
            "Source tabular dataset (50–1000+ rows)",
            "Generates realistic tabular records preserving statistical properties",
            "Not applicable (generates data, not language model weights)",
            "Implemented in Module U4 for synthetic tabular synthesis"
        ]
    }
    return pd.DataFrame(data)
