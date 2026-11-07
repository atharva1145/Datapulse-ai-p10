"""
Module: PyTorch CTGAN Tabular Synthesizer
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Trains Conditional Generative Adversarial Networks (CTGAN) on tabular data
using PyTorch, handles mixed continuous/discrete columns with mode-specific normalization,
and samples synthetic records.
"""

from typing import Tuple, Dict, Any, List, Optional
import time
import numpy as np
import pandas as pd
from ctgan import CTGAN
from config.settings import DEFAULT_CTGAN_EPOCHS, MAX_CTGAN_TRAINING_ROWS

def prepare_data_for_ctgan(
    df: pd.DataFrame,
    selected_columns: Optional[List[str]] = None,
    max_training_rows: int = MAX_CTGAN_TRAINING_ROWS
) -> Tuple[pd.DataFrame, List[str], List[str]]:
    """
    Sanitizes DataFrame for CTGAN training:
    - Filters to user-selected columns
    - Drops constant or entirely-null columns
    - Samples up to max_training_rows for fast interactive CPU training
    - Identifies discrete/categorical columns
    """
    cols_to_use = selected_columns if selected_columns else list(df.columns)
    clean_df = df[cols_to_use].copy()

    # Drop constant columns (0 variance)
    dropped_cols = []
    for c in clean_df.columns:
        if clean_df[c].nunique(dropna=True) <= 1:
            dropped_cols.append(c)
    if dropped_cols:
        clean_df.drop(columns=dropped_cols, inplace=True)

    # Simple imputation for training stability
    for c in clean_df.columns:
        if clean_df[c].isnull().sum() > 0:
            if pd.api.types.is_numeric_dtype(clean_df[c]):
                clean_df[c].fillna(clean_df[c].median(), inplace=True)
            else:
                clean_df[c].fillna(clean_df[c].mode()[0] if not clean_df[c].mode().empty else "Missing", inplace=True)

    # Sample rows if dataset exceeds CPU threshold
    if len(clean_df) > max_training_rows:
        clean_df = clean_df.sample(n=max_training_rows, random_state=42)

    # Identify discrete columns (categorical or low-cardinality discrete integers)
    discrete_cols = []
    numerical_cols = []
    for c in clean_df.columns:
        is_num = pd.api.types.is_numeric_dtype(clean_df[c])
        is_float = pd.api.types.is_float_dtype(clean_df[c])
        nunique = clean_df[c].nunique()

        # Float columns with > 2 unique values are continuous numerical
        if is_float and nunique > 2:
            clean_df[c] = pd.to_numeric(clean_df[c], errors="coerce")
            numerical_cols.append(c)
        elif not is_num or (nunique <= 10 and nunique < len(clean_df) * 0.3):
            clean_df[c] = clean_df[c].astype(str)
            discrete_cols.append(c)
        else:
            clean_df[c] = pd.to_numeric(clean_df[c], errors="coerce")
            numerical_cols.append(c)

    return clean_df, discrete_cols, numerical_cols

def train_ctgan_synthesizer(
    df: pd.DataFrame,
    discrete_columns: List[str],
    epochs: int = DEFAULT_CTGAN_EPOCHS,
    batch_size: int = 100
) -> Tuple[Optional[CTGAN], float, Optional[str]]:
    """
    Configures and trains PyTorch CTGAN on eligible tabular data.
    Returns: (trained_model, training_time_seconds, error_message)
    """
    start_time = time.time()
    try:
        # Enforce batch size constraint (batch_size must be divisible by pac or <= sample size)
        eff_batch_size = min(batch_size, max(10, len(df) // 2))
        # CTGAN requires batch_size to be a multiple of pac (default pac=10)
        eff_batch_size = max(10, (eff_batch_size // 10) * 10)

        ctgan_model = CTGAN(
            epochs=epochs,
            batch_size=eff_batch_size,
            generator_dim=(128, 128),
            discriminator_dim=(128, 128),
            generator_lr=2e-4,
            discriminator_lr=2e-4,
            verbose=False,
            cuda=False  # CPU-compatible
        )

        ctgan_model.fit(df, discrete_columns=discrete_columns)
        training_time = round(time.time() - start_time, 2)
        return ctgan_model, training_time, None

    except Exception as ex:
        training_time = round(time.time() - start_time, 2)
        return None, training_time, f"CTGAN training error: {str(ex)}"

def generate_synthetic_samples(
    model: CTGAN,
    num_rows: int = 100,
    reference_df: Optional[pd.DataFrame] = None
) -> Tuple[Optional[pd.DataFrame], Optional[str]]:
    """
    Samples synthetic records from the trained CTGAN generator.
    """
    if model is None:
        return None, "Error: CTGAN model is not trained."

    try:
        synth_df = model.sample(num_rows)
        # Cast data types to match reference DataFrame where appropriate
        if reference_df is not None:
            for c in synth_df.columns:
                if c in reference_df.columns:
                    target_dtype = reference_df[c].dtype
                    if pd.api.types.is_numeric_dtype(target_dtype):
                        synth_df[c] = pd.to_numeric(synth_df[c], errors="coerce")
                        if "int" in str(target_dtype):
                            synth_df[c] = synth_df[c].round().astype(target_dtype, errors="ignore")
        return synth_df, None
    except Exception as ex:
        return None, f"CTGAN sampling error: {str(ex)}"
