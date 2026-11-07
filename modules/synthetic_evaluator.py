"""
Module: Real vs. Synthetic Statistical Evaluator
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Calculates rigorous statistical similarity metrics comparing real and synthetic data:
- Kolmogorov-Smirnov (KS) test for continuous distributions
- Jensen-Shannon (JS) divergence for discrete categories
- Correlation matrix difference norm
"""

from typing import Dict, Any, List, Tuple, Optional
import numpy as np
import pandas as pd
from scipy import stats
from scipy.spatial.distance import jensenshannon
import plotly.express as px
import plotly.graph_objects as go

def evaluate_numerical_columns(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    num_cols: List[str]
) -> pd.DataFrame:
    """
    Computes Kolmogorov-Smirnov (KS) statistic and descriptive comparisons for numerical columns.
    """
    records = []
    for col in num_cols:
        if col not in real_df.columns or col not in synth_df.columns:
            continue
        
        real_series = pd.to_numeric(real_df[col], errors="coerce").dropna()
        synth_series = pd.to_numeric(synth_df[col], errors="coerce").dropna()

        if len(real_series) < 2 or len(synth_series) < 2:
            continue

        # Two-sample Kolmogorov-Smirnov test
        ks_res = stats.ks_2samp(real_series, synth_series)
        ks_stat = round(float(ks_res.statistic), 3)
        ks_pval = round(float(ks_res.pvalue), 4)

        # Means and Stds
        real_mean = round(float(real_series.mean()), 2)
        synth_mean = round(float(synth_series.mean()), 2)
        real_std = round(float(real_series.std()), 2)
        synth_std = round(float(synth_series.std()), 2)

        # Distribution fidelity rating
        if ks_stat <= 0.15:
            fidelity = "🟢 Excellent (Close Match)"
        elif ks_stat <= 0.30:
            fidelity = "🟡 Moderate (Fair Match)"
        else:
            fidelity = "🔴 Divergent (Distinct)"

        records.append({
            "Column": col,
            "Real Mean": real_mean,
            "Synth Mean": synth_mean,
            "Real Std": real_std,
            "Synth Std": synth_std,
            "KS Statistic": ks_stat,
            "p-value": ks_pval,
            "Distribution Fidelity": fidelity
        })

    return pd.DataFrame(records)

def evaluate_categorical_columns(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    cat_cols: List[str]
) -> pd.DataFrame:
    """
    Computes Jensen-Shannon (JS) divergence comparing real and synthetic categorical proportions.
    """
    records = []
    for col in cat_cols:
        if col not in real_df.columns or col not in synth_df.columns:
            continue

        real_counts = real_df[col].astype(str).value_counts(normalize=True)
        synth_counts = synth_df[col].astype(str).value_counts(normalize=True)

        all_cats = sorted(list(set(real_counts.index).union(set(synth_counts.index))))
        p = np.array([real_counts.get(c, 0.0) for c in all_cats])
        q = np.array([synth_counts.get(c, 0.0) for c in all_cats])

        # Jensen-Shannon distance in [0, 1]
        js_div = round(float(jensenshannon(p, q)), 3)

        if js_div <= 0.15:
            fidelity = "🟢 High Similarity"
        elif js_div <= 0.35:
            fidelity = "🟡 Moderate Similarity"
        else:
            fidelity = "🔴 Low Similarity"

        records.append({
            "Column": col,
            "Unique Categories": len(all_cats),
            "JS Divergence": js_div,
            "Category Fidelity": fidelity
        })

    return pd.DataFrame(records)

def evaluate_correlation_difference(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    num_cols: List[str]
) -> Tuple[float, Optional[pd.DataFrame]]:
    """
    Measures how well synthetic data preserves inter-feature correlations:
    Calculates Mean Absolute Error between Pearson correlation matrices.
    """
    valid_cols = [c for c in num_cols if c in real_df.columns and c in synth_df.columns]
    if len(valid_cols) < 2:
        return 0.0, None

    r_real = real_df[valid_cols].apply(pd.to_numeric, errors="coerce").corr().fillna(0)
    r_synth = synth_df[valid_cols].apply(pd.to_numeric, errors="coerce").corr().fillna(0)

    delta_matrix = (r_real - r_synth).abs().round(3)
    mean_mae = round(float(delta_matrix.values.mean()), 3)
    return mean_mae, delta_matrix

def plot_real_vs_synthetic_overlay(
    real_df: pd.DataFrame,
    synth_df: pd.DataFrame,
    column: str
) -> go.Figure:
    """Plots overlay histogram comparing real vs. synthetic distributions for a column."""
    fig = go.Figure()

    if pd.api.types.is_numeric_dtype(real_df[column]):
        fig.add_trace(go.Histogram(
            x=real_df[column].dropna(),
            name="Real Data",
            opacity=0.6,
            marker_color="#4F46E5",
            histnorm="probability density"
        ))
        fig.add_trace(go.Histogram(
            x=synth_df[column].dropna(),
            name="Synthetic (CTGAN)",
            opacity=0.6,
            marker_color="#10B981",
            histnorm="probability density"
        ))
        fig.update_layout(
            barmode="overlay",
            title=f"Distribution Overlay: Real vs. Synthetic ({column})",
            xaxis_title=column,
            yaxis_title="Probability Density",
            margin=dict(l=20, r=20, t=40, b=20)
        )
    else:
        real_p = real_df[column].astype(str).value_counts(normalize=True).head(8)
        synth_p = synth_df[column].astype(str).value_counts(normalize=True).head(8)
        all_cats = list(dict.fromkeys(list(real_p.index) + list(synth_p.index)))

        fig.add_trace(go.Bar(
            x=all_cats,
            y=[real_p.get(c, 0.0) * 100 for c in all_cats],
            name="Real (%)",
            marker_color="#4F46E5"
        ))
        fig.add_trace(go.Bar(
            x=all_cats,
            y=[synth_p.get(c, 0.0) * 100 for c in all_cats],
            name="Synthetic (%)",
            marker_color="#10B981"
        ))
        fig.update_layout(
            barmode="group",
            title=f"Category Proportions: Real vs. Synthetic ({column})",
            xaxis_title=column,
            yaxis_title="Proportion (%)",
            margin=dict(l=20, r=20, t=40, b=20)
        )

    return fig
