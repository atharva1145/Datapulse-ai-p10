"""
Unit tests for modules/ctgan_generator.py, modules/synthetic_evaluator.py, and modules/image_generator.py
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)
"""

import pytest
import numpy as np
import pandas as pd
from modules.ctgan_generator import (
    prepare_data_for_ctgan,
    train_ctgan_synthesizer,
    generate_synthetic_samples
)
from modules.synthetic_evaluator import (
    evaluate_numerical_columns,
    evaluate_categorical_columns,
    evaluate_correlation_difference
)
from modules.image_generator import (
    generate_dataset_infographic_card,
    get_diffusion_model_metadata
)
from modules.data_loader import load_csv
from config.settings import SAMPLE_DATA_DIR

def test_prepare_data_for_ctgan():
    df = pd.DataFrame({
        "num1": [1.0, 2.0, 3.0, 4.0, 5.0],
        "cat1": ["A", "B", "A", "B", "A"],
        "const": [1, 1, 1, 1, 1]  # Constant column should be dropped
    })
    clean_df, disc_cols, num_cols = prepare_data_for_ctgan(df)
    assert "const" not in clean_df.columns
    assert "cat1" in disc_cols
    assert "num1" in num_cols

def test_ctgan_training_and_sampling():
    iris_path = SAMPLE_DATA_DIR / "iris.csv"
    df, _, _ = load_csv(iris_path)
    # Take a 30-row slice for rapid test execution
    sample_df = df.head(30).copy()
    
    clean_df, disc_cols, num_cols = prepare_data_for_ctgan(sample_df)
    # Train for 2 epochs in test
    model, train_time, err = train_ctgan_synthesizer(clean_df, discrete_columns=disc_cols, epochs=2, batch_size=10)
    assert err is None
    assert model is not None
    assert train_time >= 0.0

    synth_df, samp_err = generate_synthetic_samples(model, num_rows=15, reference_df=clean_df)
    assert samp_err is None
    assert synth_df is not None
    assert len(synth_df) == 15
    assert list(synth_df.columns) == list(clean_df.columns)

def test_synthetic_evaluation_metrics():
    # Real vs synthetic test DataFrames
    np.random.seed(42)
    real_df = pd.DataFrame({
        "feature1": np.random.normal(10, 2, 50),
        "feature2": np.random.normal(50, 10, 50),
        "category": np.random.choice(["X", "Y"], 50)
    })
    synth_df = pd.DataFrame({
        "feature1": np.random.normal(10.2, 2.1, 50),
        "feature2": np.random.normal(49.5, 9.8, 50),
        "category": np.random.choice(["X", "Y"], 50)
    })

    # KS evaluation
    ks_df = evaluate_numerical_columns(real_df, synth_df, ["feature1", "feature2"])
    assert len(ks_df) == 2
    for stat in ks_df["KS Statistic"]:
        assert 0.0 <= stat <= 1.0
    for pval in ks_df["p-value"]:
        assert 0.0 <= pval <= 1.0

    # JS evaluation
    js_df = evaluate_categorical_columns(real_df, synth_df, ["category"])
    assert len(js_df) == 1
    assert 0.0 <= js_df["JS Divergence"].iloc[0] <= 1.0

    # Correlation MAE
    mae, delta = evaluate_correlation_difference(real_df, synth_df, ["feature1", "feature2"])
    assert mae >= 0.0
    assert delta is not None

def test_infographic_card_generation():
    png_bytes = generate_dataset_infographic_card(
        dataset_name="Test Dataset",
        total_rows=500,
        total_cols=8,
        quality_score=92.5,
        recommended_task="Binary Classification",
        top_insight="The dataset exhibits balanced characteristics suitable for gradient boosted trees."
    )
    assert len(png_bytes) > 1000, "Should generate valid non-empty PNG bytes buffer"
    # Verify PNG magic number
    assert png_bytes[:8] == b"\x89PNG\r\n\x1a\n"

def test_diffusion_metadata():
    meta = get_diffusion_model_metadata()
    assert "model_name" in meta
    assert "license" in meta
    assert len(meta["limitations"]) > 0
