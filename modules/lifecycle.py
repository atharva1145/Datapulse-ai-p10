"""
Module: Machine Learning Lifecycle & Unit I Foundations
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Provides the 10-stage ML lifecycle guide with dataset-specific steps,
and theoretical comparisons (Generative AI vs Discriminative AI).
"""

from typing import Dict, Any, List
import pandas as pd

def get_ml_lifecycle_stages(df: pd.DataFrame, target_col: str, ml_task_info: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Returns the 10-stage ML lifecycle mapped directly to the uploaded dataset's characteristics.
    """
    total_rows = len(df)
    total_cols = len(df.columns)
    missing_cells = int(df.isnull().sum().sum())
    dup_rows = int(df.duplicated().sum())
    suggested_task = ml_task_info.get("suggested_task", "Supervised/Unsupervised Analysis")

    stages = [
        {
            "step": 1,
            "name": "Problem Definition",
            "icon": "🎯",
            "objective": f"Formulate the business or research objective based on target '{target_col}'.",
            "dataset_action": (
                f"Predicted task is **{suggested_task}**. Clearly define success criteria "
                f"(e.g., achieving F1 > 0.85 or RMSE < 10% of target range) before data manipulation."
            )
        },
        {
            "step": 2,
            "name": "Data Collection",
            "icon": "📥",
            "objective": "Gather representative data samples while verifying integrity and provenance.",
            "dataset_action": (
                f"Currently ingested {total_rows:,} records across {total_cols} columns. "
                "Verify sampling integrity: are all real-world customer or operational segments represented?"
            )
        },
        {
            "step": 3,
            "name": "Data Understanding (EDA)",
            "icon": "🔍",
            "objective": "Profile statistical distributions, anomalies, correlations, and quality scores.",
            "dataset_action": (
                f"Identified {missing_cells} missing cells and {dup_rows} duplicate rows. "
                "Examine feature skewness, outlier counts, and correlation heatmaps in the Visual Analytics tab."
            )
        },
        {
            "step": 4,
            "name": "Data Preprocessing",
            "icon": "🧹",
            "objective": "Clean missing values, deduplicate, encode categoricals, and remove corrupted entries.",
            "dataset_action": (
                f"{'Impute missing cells using median/mode strategy. ' if missing_cells > 0 else 'Zero missing values; '}"
                f"{'Drop duplicate rows to prevent data leakage. ' if dup_rows > 0 else 'No duplicates found; '}"
                "Apply One-Hot or Target Encoding for categorical variables."
            )
        },
        {
            "step": 5,
            "name": "Feature Engineering",
            "icon": "⚙️",
            "objective": "Derive informative signals, normalize scales, and reduce collinearity.",
            "dataset_action": (
                "Scale numerical attributes via StandardScaler / RobustScaler. "
                "Compute interaction terms or polynomial terms if non-linear dependencies are present."
            )
        },
        {
            "step": 6,
            "name": "Model Selection",
            "icon": "🤖",
            "objective": "Select candidate algorithms matching the task complexity and interpretability constraints.",
            "dataset_action": (
                f"Recommended algorithms: {', '.join([a['name'] for a in ml_task_info.get('candidate_algorithms', [])])}. "
                "Establish a simple baseline (e.g. Logistic Regression or Mean Predictor) before complex ensembling."
            )
        },
        {
            "step": 7,
            "name": "Model Training & Tuning",
            "icon": "🏋️",
            "objective": "Train parameters with stratified K-Fold cross-validation and hyperparameter search.",
            "dataset_action": (
                f"Partition {total_rows} records into Train (80%) and Test (20%). "
                "Use StratifiedKFold (k=5) to preserve target class ratios across folds."
            )
        },
        {
            "step": 8,
            "name": "Evaluation & Validation",
            "icon": "📊",
            "objective": "Evaluate on held-out test split with metrics robust to dataset imbalances.",
            "dataset_action": (
                "Avoid raw accuracy on imbalanced targets. Prioritize Precision, Recall, PR-AUC, Macro-F1, "
                "and inspect confusion matrices for systematic false-positive clusters."
            )
        },
        {
            "step": 9,
            "name": "Deployment",
            "icon": "🚀",
            "objective": "Package trained pipeline into an API endpoint or interactive Streamlit application.",
            "dataset_action": (
                "Export scikit-learn pipeline (.joblib) with preprocessing steps included. "
                "Deploy on Streamlit / Hugging Face Spaces with input schema validation."
            )
        },
        {
            "step": 10,
            "name": "Monitoring & Drift Detection",
            "icon": "📡",
            "objective": "Track concept drift, data drift, and performance degradation in production.",
            "dataset_action": (
                "Monitor distribution divergence using Kolmogorov-Smirnov (KS) tests between inference inputs "
                "and training baseline. Retrain when drift p-value < 0.05."
            )
        }
    ]
    return stages

def get_genai_vs_discriminative_comparison() -> pd.DataFrame:
    """
    Unit I Syllabus Requirement:
    Generative AI vs. Discriminative AI Theoretical Comparison Table.
    """
    data = {
        "Attribute": [
            "Mathematical Objective",
            "Core Question",
            "Data Modeling",
            "Output Type",
            "Primary Model Architectures",
            "Typical Tasks",
            "Sample Complexity",
            "Role in this Project (P10)"
        ],
        "Generative AI": [
            "Models joint probability distribution P(X, Y) or latent P(X)",
            "'How was this data generated? Can I produce another sample?'",
            "Captures the underlying probabilistic data generation mechanism",
            "New synthetic records, tokens, images, or embeddings",
            "Transformers (GPT, Gemini), GANs (CTGAN), VAEs, Diffusion",
            "Synthetic data generation, Text/Code generation, Multimodal interpretation",
            "High (requires large diverse datasets to learn full distribution)",
            "CTGAN creates synthetic rows; Gemini writes code and explains charts"
        ],
        "Discriminative AI": [
            "Models conditional probability distribution P(Y | X) directly",
            "'Given these features X, which class boundary separates them?'",
            "Focuses purely on the decision boundary between classes",
            "Class label, continuous score, or bounding box coordinates",
            "Logistic Regression, SVM, Random Forest, XGBoost, CNN classifiers",
            "Binary classification, regression, sentiment analysis, anomaly detection",
            "Moderate (only needs to discern differences between classes)",
            "Recommended ML tasks in U1 (e.g. predicting survival or wine quality)"
        ]
    }
    return pd.DataFrame(data)
