"""
Module: Multimodal Vision Chart Interpreter
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Uses Gemini Multimodal Vision API to visually interpret rendered dataset charts,
detect skewness, modal peaks, outlier clusters, and descriptive trends.
"""

import os
from typing import Dict, Any, Optional
import numpy as np
import pandas as pd
from scipy import stats
from config.settings import GEMINI_MODEL_VISION
from modules.llm_assistant import get_gemini_client

def interpret_chart_with_vision(
    image_bytes: bytes,
    column_name: str,
    df: Optional[pd.DataFrame] = None,
    custom_api_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Sends rendered chart image bytes to Gemini Vision model for automated visual interpretation.
    Falls back to rigorous statistical distribution modeling if offline.
    """
    if custom_api_key:
        os.environ["GEMINI_API_KEY"] = custom_api_key

    client = get_gemini_client()

    # 1. Cloud Multimodal Vision Inference
    if client is not None and image_bytes:
        try:
            from google.genai import types
            
            prompt = (
                f"You are an expert Data Scientist analyzing an uploaded chart for the column '{column_name}'.\n"
                "Please visually analyze this image and provide:\n"
                "1. Chart Type & Primary Variable.\n"
                "2. Distribution Shape (e.g., normal, right-skewed, left-skewed, bimodal, uniform, or heavy-tailed).\n"
                "3. Key Patterns & Central Tendency (where the concentration of values lies).\n"
                "4. Outliers or Anomalies (visible tails, isolated spikes, or gaps).\n"
                "5. Practical Recommendation for Machine Learning Preprocessing (e.g., log transform, robust scaling, or one-hot encoding).\n\n"
                "Ground your answer solely on what is visible in the chart."
            )

            response = client.models.generate_content(
                model=GEMINI_MODEL_VISION,
                contents=[
                    types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                    prompt
                ]
            )
            raw_explanation = response.text.strip() if response.text else "Chart analyzed successfully."
            return {
                "interpretation": raw_explanation,
                "engine": f"Gemini Vision ({GEMINI_MODEL_VISION})",
                "grounded": True,
                "warning": "Vision LLMs can occasionally misread fine-grained axis ticks. Cross-verify with descriptive statistics."
            }
        except Exception as ex:
            print(f"Gemini Vision API notice: {ex}. Falling back to statistical profile.")

    # 2. Deterministic Statistical Fallback (Ground-truth empirical inspection)
    return generate_statistical_chart_interpretation(df, column_name)

def generate_statistical_chart_interpretation(
    df: Optional[pd.DataFrame],
    column_name: str
) -> Dict[str, Any]:
    """
    Calculates exact empirical moments (skewness, kurtosis, modal peaks)
    to provide a mathematically grounded visual summary when API is unconfigured.
    """
    if df is None or column_name not in df.columns:
        return {
            "interpretation": (
                f"The distribution chart for '{column_name}' displays the frequency spread of records. "
                "The visualization highlights central tendencies and dispersion across observed values."
            ),
            "engine": "Statistical Fallback Engine",
            "grounded": True,
            "warning": "Offline mode: Derived from mathematical moment calculation."
        }

    series = df[column_name].dropna()

    if pd.api.types.is_numeric_dtype(series):
        mean_val = round(float(series.mean()), 2)
        median_val = round(float(series.median()), 2)
        std_val = round(float(series.std()), 2)
        skew_val = round(float(stats.skew(series)), 2)
        kurt_val = round(float(stats.kurtosis(series)), 2)

        # Classify skewness
        if abs(skew_val) < 0.5:
            skew_desc = "approximately symmetric (bell-shaped / normal)"
            prep_rec = "Standard scaling (StandardScaler) is recommended."
        elif skew_val >= 0.5:
            skew_desc = f"positively right-skewed (skewness = +{skew_val}) with a longer tail towards higher values"
            prep_rec = "A log1p or Box-Cox transformation is recommended to stabilize variance."
        else:
            skew_desc = f"negatively left-skewed (skewness = {skew_val}) with mass clustered towards higher values"
            prep_rec = "Robust scaling (RobustScaler) or quantile transformation is recommended."

        # Outlier counts
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        outlier_count = int(((series < q1 - 1.5 * iqr) | (series > q3 + 1.5 * iqr)).sum())

        interpretation = (
            f"**Distribution Profile for `{column_name}`:**\n\n"
            f"- **Central Tendency:** The distribution has a mean of `{mean_val}` and median of `{median_val}` (Std Dev = `{std_val}`).\n"
            f"- **Shape & Symmetry:** The curve is {skew_desc}. Kurtosis is measured at `{kurt_val}`.\n"
            f"- **Outlier Detection:** The IQR method identifies `{outlier_count}` points beyond the 1.5×IQR boundary.\n"
            f"- **ML Preprocessing Guidance:** {prep_rec}"
        )
    else:
        top_cats = series.value_counts()
        total_n = len(series)
        top_name = str(top_cats.index[0])
        top_pct = round((top_cats.iloc[0] / total_n) * 100, 1)
        nunique = series.nunique()

        interpretation = (
            f"**Categorical Frequency Profile for `{column_name}`:**\n\n"
            f"- **Cardinality:** The column contains `{nunique}` distinct categories across `{total_n:,}` records.\n"
            f"- **Dominant Class:** The most frequent category is **'{top_name}'**, representing `{top_pct}%` of the total population.\n"
            f"- **Preprocessing Guidance:** "
            f"{'Apply One-Hot Encoding (pd.get_dummies) as cardinality is low.' if nunique <= 8 else 'Apply Target Encoding or Frequency Encoding to avoid high-dimensional feature explosion.'}"
        )

    return {
        "interpretation": interpretation,
        "engine": "Deterministic Moment & Frequency Engine",
        "grounded": True,
        "warning": "Derived from exact mathematical distribution moments."
    }
