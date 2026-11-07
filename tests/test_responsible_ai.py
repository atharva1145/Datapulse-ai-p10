"""
Unit tests for modules/responsible_ai.py
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)
"""

import pytest
import pandas as pd
import numpy as np
from modules.responsible_ai import (
    scan_sensitive_columns,
    analyze_class_imbalance,
    run_empirical_hallucination_benchmark
)
from modules.data_loader import load_csv
from config.settings import SAMPLE_DATA_DIR

def test_scan_sensitive_columns_detected():
    df_pii = pd.DataFrame({
        "customer_email": ["john@example.com", "jane@company.org"],
        "full_name": ["John Doe", "Jane Smith"],
        "contact_phone": ["+1234567890", "+9876543210"],
        "annual_salary": [75000, 92000],
        "feature_score": [1.5, 2.8]
    })
    findings = scan_sensitive_columns(df_pii)
    detected_cols = [f["column"] for f in findings]
    
    assert "customer_email" in detected_cols
    assert "full_name" in detected_cols
    assert "contact_phone" in detected_cols
    assert "annual_salary" in detected_cols
    assert "feature_score" not in detected_cols

def test_scan_sensitive_columns_clean_iris():
    iris_path = SAMPLE_DATA_DIR / "iris.csv"
    df, _, _ = load_csv(iris_path)
    findings = scan_sensitive_columns(df)
    # Botanical measurements contain zero PII
    assert len(findings) == 0

def test_analyze_class_imbalance_imbalanced():
    df_imbalanced = pd.DataFrame({
        "target": ["Negative"] * 900 + ["Positive"] * 100
    })
    res = analyze_class_imbalance(df_imbalanced, "target")
    assert res is not None
    assert res["is_applicable"] is True
    assert res["imbalance_ratio"] == 9.0
    assert "Moderate" in res["severity"]
    assert "Accuracy Paradox" in res["metric_guidance"]

def test_analyze_class_imbalance_balanced_iris():
    iris_path = SAMPLE_DATA_DIR / "iris.csv"
    df, _, _ = load_csv(iris_path)
    res = analyze_class_imbalance(df, "species")
    assert res is not None
    assert res["is_applicable"] is True
    assert res["imbalance_ratio"] == 1.0  # 50 per species
    assert "Balanced" in res["severity"]

def test_analyze_class_imbalance_continuous():
    df_continuous = pd.DataFrame({
        "price": np.random.normal(100, 15, 200)
    })
    res = analyze_class_imbalance(df_continuous, "price")
    assert res is not None
    assert res["is_applicable"] is False
    assert "continuous numerical" in res["reason"]

def test_hallucination_benchmark_structure():
    df = pd.DataFrame({
        "feature_a": [10, 20, 30, 40, 50],
        "feature_b": [1.1, 2.2, 3.3, 4.4, 5.5]
    })
    bench = run_empirical_hallucination_benchmark(df)
    assert "results_table" in bench
    assert bench["total_tests"] == 6
    assert bench["accuracy_pct"] >= 80.0
    assert len(bench["results_table"]) == 6
