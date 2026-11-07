"""
Module: Data Profiler & Quality Scorer
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Calculates comprehensive dataset statistics, column categorization,
missingness metrics, duplicate detection, and a deterministic Dataset Quality Score.
"""

from typing import Dict, Any, List, Optional
import numpy as np
import pandas as pd

def calculate_quality_score(
    total_cells: int,
    missing_cells: int,
    total_rows: int,
    duplicate_rows: int,
    total_cols: int,
    constant_cols_count: int,
    outlier_cells: int,
    numerical_cells: int
) -> Dict[str, Any]:
    """
    Computes a transparent, reproducible Dataset Quality Score between 0 and 100.
    
    Formula:
      Health Score = 100 - (P_missing + P_duplicates + P_constant + P_outliers)
      
    Penalties:
      1. Missing Value Penalty: max 40 points
         P_missing = min(40, (missing_cells / total_cells) * 100 * 1.0)
      2. Duplicate Rows Penalty: max 20 points
         P_duplicates = min(20, (duplicate_rows / total_rows) * 100 * 1.0)
      3. Constant Column Penalty: max 20 points
         P_constant = min(20, (constant_cols_count / total_cols) * 100 * 2.0)
      4. Outlier Cells Penalty: max 20 points
         P_outliers = min(20, (outlier_cells / max(1, numerical_cells)) * 100 * 0.5)
    """
    if total_cells == 0 or total_rows == 0:
        return {
            "score": 0.0,
            "rating": "Invalid",
            "penalties": {"missing": 0, "duplicates": 0, "constant": 0, "outliers": 0},
            "formula_explanation": "Empty or zero-cell dataset."
        }

    p_missing = min(40.0, (missing_cells / total_cells) * 100.0 * 1.0)
    p_duplicates = min(20.0, (duplicate_rows / total_rows) * 100.0 * 1.0)
    p_constant = min(20.0, (constant_cols_count / max(1, total_cols)) * 100.0 * 2.0)
    p_outliers = min(20.0, (outlier_cells / max(1, numerical_cells)) * 100.0 * 0.5)

    total_penalty = p_missing + p_duplicates + p_constant + p_outliers
    score = max(0.0, min(100.0, round(100.0 - total_penalty, 1)))

    if score >= 90:
        rating = "Excellent"
        badge_class = "badge-excellent"
    elif score >= 75:
        rating = "Good"
        badge_class = "badge-good"
    elif score >= 55:
        rating = "Fair"
        badge_class = "badge-fair"
    else:
        rating = "Poor"
        badge_class = "badge-poor"

    return {
        "score": score,
        "rating": rating,
        "badge_class": badge_class,
        "penalties": {
            "missing_penalty": round(p_missing, 1),
            "duplicate_penalty": round(p_duplicates, 1),
            "constant_penalty": round(p_constant, 1),
            "outlier_penalty": round(p_outliers, 1)
        },
        "formula": "100 - (P_missing[max 40] + P_duplicates[max 20] + P_constant[max 20] + P_outliers[max 20])"
    }

def count_iqr_outliers(series: pd.Series) -> int:
    """Calculates number of outliers using 1.5 * IQR rule for numerical series."""
    clean = series.dropna()
    if len(clean) < 4:
        return 0
    q1 = clean.quantile(0.25)
    q3 = clean.quantile(0.75)
    iqr = q3 - q1
    if iqr == 0:
        return 0
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return int(((clean < lower_bound) | (clean > upper_bound)).sum())

def profile_dataset(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Performs complete automated profiling of a Pandas DataFrame.
    """
    if df is None or df.empty:
        raise ValueError("Cannot profile an empty or None DataFrame.")

    total_rows = len(df)
    total_cols = len(df.columns)
    total_cells = total_rows * total_cols

    # Missing values
    missing_series = df.isnull().sum()
    missing_cells = int(missing_series.sum())
    missing_pct = round((missing_cells / total_cells) * 100, 2) if total_cells > 0 else 0.0

    missing_by_col = {}
    for col, count in missing_series.items():
        missing_by_col[col] = {
            "count": int(count),
            "percentage": round((count / total_rows) * 100, 2)
        }

    # Duplicates
    duplicate_rows = int(df.duplicated().sum())
    duplicate_pct = round((duplicate_rows / total_rows) * 100, 2) if total_rows > 0 else 0.0

    # Categorize Columns
    numerical_cols = []
    categorical_cols = []
    datetime_cols = []
    constant_cols = []
    id_like_cols = []

    column_profiles = {}
    outlier_cells_total = 0
    numerical_cells_total = 0

    for col in df.columns:
        series = df[col]
        dtype_str = str(series.dtype)
        nunique = int(series.nunique(dropna=True))

        col_info: Dict[str, Any] = {
            "name": col,
            "dtype": dtype_str,
            "missing_count": int(series.isnull().sum()),
            "missing_pct": round((series.isnull().sum() / total_rows) * 100, 2),
            "unique_count": nunique,
            "unique_ratio": round(nunique / total_rows, 4) if total_rows > 0 else 0.0
        }

        # Check constant
        if nunique <= 1:
            constant_cols.append(col)
            col_info["type_category"] = "Constant"
        # Check datetime
        elif "datetime" in dtype_str:
            datetime_cols.append(col)
            col_info["type_category"] = "Datetime"
        # Check numerical
        elif pd.api.types.is_numeric_dtype(series):
            numerical_cols.append(col)
            col_info["type_category"] = "Numerical"
            clean_s = series.dropna()
            if len(clean_s) > 0:
                col_info["mean"] = float(round(clean_s.mean(), 3))
                col_info["std"] = float(round(clean_s.std(), 3)) if len(clean_s) > 1 else 0.0
                col_info["min"] = float(round(clean_s.min(), 3))
                col_info["p25"] = float(round(clean_s.quantile(0.25), 3))
                col_info["median"] = float(round(clean_s.median(), 3))
                col_info["p75"] = float(round(clean_s.quantile(0.75), 3))
                col_info["max"] = float(round(clean_s.max(), 3))
                outliers = count_iqr_outliers(series)
                col_info["outlier_count"] = outliers
                outlier_cells_total += outliers
                numerical_cells_total += len(clean_s)
        # Check categorical / text
        else:
            col_info["type_category"] = "Categorical"
            # High cardinality ID check
            if nunique / total_rows > 0.85 and total_rows > 20:
                id_like_cols.append(col)
            categorical_cols.append(col)
            clean_s = series.dropna().astype(str)
            if len(clean_s) > 0:
                top_counts = clean_s.value_counts().head(5).to_dict()
                col_info["top_values"] = top_counts

        column_profiles[col] = col_info

    # Quality score
    quality_score = calculate_quality_score(
        total_cells=total_cells,
        missing_cells=missing_cells,
        total_rows=total_rows,
        duplicate_rows=duplicate_rows,
        total_cols=total_cols,
        constant_cols_count=len(constant_cols),
        outlier_cells=outlier_cells_total,
        numerical_cells=numerical_cells_total
    )

    # Descriptive statistics summary dataframe
    numeric_summary = df.describe().T if len(numerical_cols) > 0 else pd.DataFrame()

    return {
        "total_rows": total_rows,
        "total_cols": total_cols,
        "total_cells": total_cells,
        "missing_cells": missing_cells,
        "missing_pct": missing_pct,
        "missing_by_col": missing_by_col,
        "duplicate_rows": duplicate_rows,
        "duplicate_pct": duplicate_pct,
        "numerical_cols": numerical_cols,
        "categorical_cols": categorical_cols,
        "datetime_cols": datetime_cols,
        "constant_cols": constant_cols,
        "id_like_cols": id_like_cols,
        "column_profiles": column_profiles,
        "quality_score": quality_score,
        "numeric_summary": numeric_summary
    }
