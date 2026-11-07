"""
Module: Machine Learning Task Recommender Engine
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Analyzes target column properties, data cardinality, distributions,
and structural characteristics to deterministically recommend appropriate ML tasks.
"""

from typing import Dict, Any, List, Optional
import pandas as pd
import numpy as np

def recommend_ml_task(
    df: pd.DataFrame,
    target_column: Optional[str] = None,
    user_problem_desc: Optional[str] = None
) -> Dict[str, Any]:
    """
    Evaluates dataset schema and target column to recommend learning type and candidate algorithms.
    """
    if df is None or df.empty:
        raise ValueError("Cannot recommend ML task on an empty DataFrame.")

    total_rows = len(df)
    total_cols = len(df.columns)

    # 1. If NO target column selected -> Unsupervised Learning
    if not target_column or target_column == "None" or target_column not in df.columns:
        return {
            "learning_type": "Unsupervised Learning",
            "suggested_task": "Clustering & Dimensionality Reduction / Anomaly Detection",
            "confidence": "High",
            "reason": (
                "No target variable was specified. The dataset is structured as unlabeled "
                "feature vectors, making it suitable for finding intrinsic data clusters, latent representations, "
                "or detecting outliers without ground-truth supervisory signals."
            ),
            "candidate_algorithms": [
                {"name": "K-Means / HDBSCAN", "purpose": "Partition data into homogeneous clusters based on feature distances."},
                {"name": "PCA (Principal Component Analysis)", "purpose": "Reduce dimensionality while preserving maximum variance."},
                {"name": "Isolation Forest", "purpose": "Detect anomalous records and data corruption without labels."}
            ],
            "assumptions": [
                "Features can be appropriately scaled (e.g., StandardScaler or MinMaxScaler).",
                "Distance metrics (Euclidean, Cosine) are meaningful across numerical attributes."
            ],
            "limitations": [
                "Clustering quality heavily depends on hyperparameter choice (e.g., number of clusters k).",
                "Without ground-truth labels, objective validation requires silhouette or Davies-Bouldin scores."
            ],
            "rl_note": (
                "Reinforcement Learning (RL) is NOT applicable here. RL is designed for sequential "
                "decision-making processes with dynamic state-action-reward loops in interactive environments, "
                "not static tabular snapshots."
            )
        }

    # 2. Analyze Target Column
    target_series = df[target_column].dropna()
    nunique = target_series.nunique()
    is_numeric = pd.api.types.is_numeric_dtype(target_series)
    unique_ratio = nunique / total_rows if total_rows > 0 else 0.0

    # Case A: Binary Classification
    if nunique == 2:
        class_names = [str(c) for c in target_series.unique()]
        return {
            "learning_type": "Supervised Learning",
            "suggested_task": "Binary Classification",
            "target_column": target_column,
            "target_classes": class_names,
            "confidence": "Very High",
            "reason": (
                f"The target column '{target_column}' contains exactly two distinct discrete classes "
                f"({class_names[0]} vs {class_names[1]}), which is the canonical formulation for binary classification."
            ),
            "candidate_algorithms": [
                {"name": "XGBoost / LightGBM", "purpose": "High-performance gradient-boosted decision trees handling mixed features."},
                {"name": "Random Forest Classifier", "purpose": "Robust ensemble less prone to overfitting with built-in feature importance."},
                {"name": "Logistic Regression (with L1/L2 penalty)", "purpose": "Interpretable linear probabilistic baseline."}
            ],
            "assumptions": [
                "Training data representative of real-world class distributions.",
                "Observations are independent and identically distributed (i.i.d.)."
            ],
            "limitations": [
                "Class imbalance can heavily distort raw accuracy; requires PR-AUC and F1 evaluation.",
                "Potential target leakage if features correlate artificially with the outcome."
            ],
            "rl_note": "A static binary target does not fulfill the Markov Decision Process (MDP) required for RL."
        }

    # Case B: Multiclass Classification
    elif (not is_numeric and nunique <= 25) or (is_numeric and nunique <= 15 and unique_ratio < 0.05):
        class_names = [str(c) for c in target_series.unique()[:10]]
        return {
            "learning_type": "Supervised Learning",
            "suggested_task": "Multiclass Classification",
            "target_column": target_column,
            "target_classes": class_names,
            "class_count": nunique,
            "confidence": "High",
            "reason": (
                f"The target column '{target_column}' contains {nunique} discrete discrete categories. "
                "Each sample belongs to one mutually exclusive class."
            ),
            "candidate_algorithms": [
                {"name": "Random Forest / Extra Trees", "purpose": "Multi-class ensemble modeling non-linear decision boundaries."},
                {"name": "CatBoost / LightGBM", "purpose": "Handles categorical encodings natively with fast gradient boosting."},
                {"name": "Multinomial Logistic Regression", "purpose": "Fast probabilistic baseline predicting softmax distribution."}
            ],
            "assumptions": [
                "Each sample belongs to exactly one category (mutually exclusive).",
                "Sufficient support (samples per class) exists for all {nunique} classes."
            ],
            "limitations": [
                "Classes with very low sample counts (< 10 rows) may require class weighting or SMOTE.",
                "Metrics like Macro-F1 should be preferred over Micro-F1."
            ],
            "rl_note": "Not an RL problem: decisions do not affect future environment states."
        }

    # Case C: Continuous Numerical -> Regression
    elif is_numeric and nunique > 15:
        return {
            "learning_type": "Supervised Learning",
            "suggested_task": "Regression (Continuous Target)",
            "target_column": target_column,
            "target_range": [float(round(target_series.min(), 3)), float(round(target_series.max(), 3))],
            "confidence": "High",
            "reason": (
                f"The target column '{target_column}' is numeric with high cardinality ({nunique} distinct values) "
                f"ranging from {round(target_series.min(), 2)} to {round(target_series.max(), 2)}, characteristic of continuous real-valued prediction."
            ),
            "candidate_algorithms": [
                {"name": "Ridge / ElasticNet Regression", "purpose": "Regularized linear models preventing multicollinearity blowup."},
                {"name": "XGBoost Regressor", "purpose": "Non-linear gradient boosting optimizing MSE or Huber loss."},
                {"name": "Support Vector Regression (SVR)", "purpose": "Effective in high-dimensional feature spaces."}
            ],
            "assumptions": [
                "Target variable possesses continuous properties without extreme unclipped outliers.",
                "Linear or piecewise relationship exists between explanatory features and the response."
            ],
            "limitations": [
                "Sensitive to extreme target outliers and skewed distributions; log-transform may be required.",
                "RMSE penalizes large errors heavily; MAE or MAPE should be reported in parallel."
            ],
            "rl_note": "RL is not suitable for static continuous curve fitting."
        }

    # Case D: High Cardinality Categorical / ID-like target
    else:
        return {
            "learning_type": "Data Preprocessing Required",
            "suggested_task": "Re-evaluate Target Selection",
            "target_column": target_column,
            "confidence": "Low",
            "reason": (
                f"The selected column '{target_column}' has {nunique} unique values out of {total_rows} rows "
                f"({round(unique_ratio * 100, 1)}% unique). It appears to be an identifier, text field, or timestamp rather than a valid prediction target."
            ),
            "candidate_algorithms": [
                {"name": "Feature Engineering / Binning", "purpose": "Group high-cardinality values into broader clusters."},
                {"name": "Unsupervised Clustering", "purpose": "Deselect the identifier and cluster remaining features."}
            ],
            "assumptions": ["Identifiers should be excluded from model training to prevent target leakage."],
            "limitations": ["Training directly on near-unique ID keys will lead to 100% memorization and zero generalization."],
            "rl_note": "Unsuitable for supervised or reinforcement learning."
        }
