"""
Unit tests for modules/ml_recommender.py & modules/lifecycle.py
Student: Atharva Shelar (Roll No: 10)
"""

import pytest
import pandas as pd
from modules.ml_recommender import recommend_ml_task
from modules.lifecycle import get_ml_lifecycle_stages, get_genai_vs_discriminative_comparison
from modules.data_loader import load_csv
from config.settings import SAMPLE_DATA_DIR

def test_recommend_unsupervised_when_no_target():
    iris_path = SAMPLE_DATA_DIR / "iris.csv"
    df, _, _ = load_csv(iris_path)
    
    rec = recommend_ml_task(df, target_column=None)
    assert rec["learning_type"] == "Unsupervised Learning"
    assert "Clustering" in rec["suggested_task"]
    assert "NOT applicable" in rec["rl_note"]

def test_recommend_binary_classification_titanic():
    titanic_path = SAMPLE_DATA_DIR / "titanic.csv"
    df, _, _ = load_csv(titanic_path)
    
    rec = recommend_ml_task(df, target_column="Survived")
    assert rec["learning_type"] == "Supervised Learning"
    assert rec["suggested_task"] == "Binary Classification"
    assert len(rec["candidate_algorithms"]) >= 3

def test_recommend_multiclass_classification_iris():
    iris_path = SAMPLE_DATA_DIR / "iris.csv"
    df, _, _ = load_csv(iris_path)
    
    rec = recommend_ml_task(df, target_column="species")
    assert rec["learning_type"] == "Supervised Learning"
    assert rec["suggested_task"] == "Multiclass Classification"
    assert rec["class_count"] == 3

def test_recommend_regression_wine():
    wine_path = SAMPLE_DATA_DIR / "winequality_red.csv"
    df, _, _ = load_csv(wine_path)
    
    # alcohol has continuous values
    rec = recommend_ml_task(df, target_column="alcohol")
    assert rec["learning_type"] == "Supervised Learning"
    assert "Regression" in rec["suggested_task"]

def test_lifecycle_stages():
    iris_path = SAMPLE_DATA_DIR / "iris.csv"
    df, _, _ = load_csv(iris_path)
    rec = recommend_ml_task(df, target_column="species")
    
    stages = get_ml_lifecycle_stages(df, target_col="species", ml_task_info=rec)
    assert len(stages) == 10
    assert stages[0]["name"] == "Problem Definition"
    assert stages[-1]["name"] == "Monitoring & Drift Detection"

def test_genai_vs_discriminative_table():
    df_comp = get_genai_vs_discriminative_comparison()
    assert len(df_comp) >= 5
    assert "Generative AI" in df_comp.columns
    assert "Discriminative AI" in df_comp.columns
