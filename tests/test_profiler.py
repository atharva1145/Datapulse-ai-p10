"""
Unit tests for modules/data_profiler.py
Student: Atharva Shelar (Roll No: 10)
"""

import pytest
import pandas as pd
import numpy as np
from modules.data_profiler import profile_dataset, calculate_quality_score, count_iqr_outliers
from modules.data_loader import load_csv
from config.settings import SAMPLE_DATA_DIR

def test_quality_score_calculation():
    # Test perfect dataset (0 missing, 0 dupes, 0 constant, 0 outliers)
    res_perfect = calculate_quality_score(
        total_cells=1000,
        missing_cells=0,
        total_rows=100,
        duplicate_rows=0,
        total_cols=10,
        constant_cols_count=0,
        outlier_cells=0,
        numerical_cells=1000
    )
    assert res_perfect["score"] == 100.0
    assert res_perfect["rating"] == "Excellent"

    # Test dataset with 50% missing values (should penalize 40 points max)
    res_bad = calculate_quality_score(
        total_cells=1000,
        missing_cells=500,
        total_rows=100,
        duplicate_rows=20,
        total_cols=10,
        constant_cols_count=2,
        outlier_cells=0,
        numerical_cells=500
    )
    # missing penalty = 40, dupe penalty = 20, constant penalty = (2/10)*100*2 = 40 (capped at 20)
    # total penalty = 40 + 20 + 20 = 80 -> score = 20
    assert res_bad["score"] == 20.0
    assert res_bad["rating"] == "Poor"

def test_count_iqr_outliers():
    # Normal distribution with 2 artificial outliers
    data = pd.Series([10.0, 10.2, 10.1, 9.9, 10.0, 10.3, 10.1, 10.0, 100.0, -50.0])
    outliers = count_iqr_outliers(data)
    assert outliers == 2

def test_profile_dataset_iris():
    iris_path = SAMPLE_DATA_DIR / "iris.csv"
    df, _, _ = load_csv(iris_path)
    profile = profile_dataset(df)

    assert profile["total_rows"] == 150
    assert profile["total_cols"] == 5
    assert profile["missing_cells"] == 0
    assert len(profile["numerical_cols"]) == 4
    assert len(profile["categorical_cols"]) == 1
    assert "species" in profile["categorical_cols"]
    assert profile["quality_score"]["score"] >= 95.0

def test_profile_dataset_titanic():
    titanic_path = SAMPLE_DATA_DIR / "titanic.csv"
    df, _, _ = load_csv(titanic_path)
    profile = profile_dataset(df)

    assert profile["total_rows"] == 891
    assert profile["total_cols"] == 12
    # Titanic has missing values in Age
    assert profile["missing_cells"] > 0
    assert "Age" in profile["missing_by_col"]
    assert profile["quality_score"]["score"] < 100.0

def test_profile_empty_dataframe():
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        profile_dataset(empty_df)
