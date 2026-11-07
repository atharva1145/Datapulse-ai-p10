"""
Unit tests for modules/embeddings.py and modules/vision_analyzer.py
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)
"""

import pytest
import numpy as np
import pandas as pd
from modules.embeddings import (
    generate_column_semantic_description,
    compute_column_embeddings,
    compute_similarity_matrix,
    cluster_similar_columns,
    get_gpt_vs_bert_architectural_comparison
)
from modules.vision_analyzer import generate_statistical_chart_interpretation
from modules.data_loader import load_csv
from config.settings import SAMPLE_DATA_DIR

def test_column_semantic_description():
    df = pd.DataFrame({
        "annual_salary": [50000, 65000, 72000, 90000],
        "department_name": ["HR", "Engineering", "Marketing", "Sales"]
    })
    desc = generate_column_semantic_description(df, "annual_salary")
    assert "annual salary" in desc.lower()
    assert "int" in desc.lower()
    assert "50000" in desc

def test_embeddings_dimensions_and_similarity():
    iris_path = SAMPLE_DATA_DIR / "iris.csv"
    df, _, _ = load_csv(iris_path)
    
    cols, emb_matrix, desc_dict = compute_column_embeddings(df)
    assert len(cols) == 5
    assert emb_matrix.shape == (5, 384), "Sentence-BERT all-MiniLM-L6-v2 produces 384-dim vectors"
    
    sim_matrix = compute_similarity_matrix(emb_matrix)
    assert sim_matrix.shape == (5, 5)
    # Diagonal must be 1.0 (self-similarity)
    for i in range(5):
        assert abs(sim_matrix[i, i] - 1.0) < 1e-3
    # Symmetry check: sim(A, B) == sim(B, A)
    assert np.allclose(sim_matrix, sim_matrix.T, atol=1e-3)
    # Bound check
    assert np.all(sim_matrix >= -1.0) and np.all(sim_matrix <= 1.0)

def test_cluster_similar_columns():
    cols = ["sepal_length", "sepal_width", "petal_length"]
    # Simulated similarity matrix where sepal_length and sepal_width are similar (0.85)
    sim = np.array([
        [1.0, 0.85, 0.40],
        [0.85, 1.0, 0.35],
        [0.40, 0.35, 1.0]
    ])
    descs = {c: f"Description of {c}" for c in cols}
    
    clusters = cluster_similar_columns(cols, sim, descs, threshold=0.70)
    assert len(clusters) == 3
    # sepal_length should have sepal_width as related match
    matches_0 = clusters[0]["matches"]
    assert len(matches_0) == 1
    assert matches_0[0]["related_column"] == "sepal_width"
    assert matches_0[0]["similarity_score"] == 0.85

def test_gpt_vs_bert_comparison_table():
    comp_df = get_gpt_vs_bert_architectural_comparison()
    assert len(comp_df) >= 6
    assert "GPT-Style (Autoregressive Decoder-Only)" in comp_df.columns
    assert "BERT-Family (Bidirectional Encoder-Only)" in comp_df.columns

def test_statistical_chart_interpretation():
    df = pd.DataFrame({
        "num_feature": [1, 2, 2, 3, 3, 3, 4, 4, 5, 100],  # Right-skewed with outlier
        "cat_feature": ["A", "A", "A", "B", "B", "C", "A", "A", "B", "C"]
    })
    res_num = generate_statistical_chart_interpretation(df, "num_feature")
    assert res_num["grounded"] is True
    assert "skewed" in res_num["interpretation"].lower()
    assert "outlier" in res_num["interpretation"].lower()

    res_cat = generate_statistical_chart_interpretation(df, "cat_feature")
    assert res_cat["grounded"] is True
    assert "Cardinality" in res_cat["interpretation"]
