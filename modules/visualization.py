"""
Module: Visualization Engine
Student: Atharva Shelar (Roll No: 10)
Subject: Generative AI (P10)

Generates interactive Plotly figures and static Matplotlib charts
for distributions, correlations, class probabilities, and Gemini Vision payloads.
Styled with Enterprise Dark SaaS aesthetics (Linear / Datadog).
"""

import io
from typing import Optional, List, Dict, Any
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

# Set clean styling for static charts
sns.set_theme(style="darkgrid", palette="muted")


def apply_plotly_enterprise_theme(fig: go.Figure) -> go.Figure:
    """Applies theme-aware (Light or Dark) styling to any Plotly figure."""
    theme_choice = "Dark (Enterprise)"
    try:
        import streamlit as st
        if hasattr(st, "session_state") and "app_theme" in st.session_state:
            theme_choice = st.session_state["app_theme"]
    except Exception:
        pass

    if theme_choice == "Light (Clean)":
        fig.update_layout(
            template="plotly_white",
            paper_bgcolor="rgba(255, 255, 255, 0.9)",
            plot_bgcolor="rgba(248, 250, 252, 0.8)",
            font=dict(family="Inter, -apple-system, sans-serif", color="#0F172A", size=12),
            title_font=dict(family="Inter, -apple-system, sans-serif", color="#0F172A", size=14),
            margin=dict(l=24, r=24, t=46, b=24),
            hoverlabel=dict(
                bgcolor="#FFFFFF",
                font_size=12,
                font_family="Inter, sans-serif",
                font_color="#0F172A"
            )
        )
        fig.update_xaxes(gridcolor="#E2E8F0", zerolinecolor="#CBD5E1")
        fig.update_yaxes(gridcolor="#E2E8F0", zerolinecolor="#CBD5E1")
    else:
        fig.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(15, 23, 42, 0.6)",
            plot_bgcolor="rgba(15, 23, 42, 0.4)",
            font=dict(family="Inter, -apple-system, sans-serif", color="#CBD5E1", size=12),
            title_font=dict(family="Inter, -apple-system, sans-serif", color="#F8FAFC", size=14),
            margin=dict(l=24, r=24, t=46, b=24),
            hoverlabel=dict(
                bgcolor="#1E293B",
                font_size=12,
                font_family="Inter, sans-serif"
            )
        )
        fig.update_xaxes(gridcolor="#1E293B", zerolinecolor="#334155")
        fig.update_yaxes(gridcolor="#1E293B", zerolinecolor="#334155")
    return fig


def plot_missing_values(missing_dict: Dict[str, Dict[str, Any]]) -> go.Figure:
    """Creates a horizontal bar chart of missing value percentages per column."""
    cols = []
    pcts = []
    counts = []
    for col, data in missing_dict.items():
        if data["count"] > 0:
            cols.append(col)
            pcts.append(data["percentage"])
            counts.append(data["count"])

    if not cols:
        # Return empty placeholder showing 100% clean data
        fig = go.Figure()
        fig.add_annotation(
            text="✨ No Missing Values Detected (100% Complete Data)",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=15, color="#10B981")
        )
        fig.update_layout(height=180, margin=dict(l=20, r=20, t=30, b=20))
        return apply_plotly_enterprise_theme(fig)

    # Sort descending
    sorted_indices = np.argsort(pcts)
    cols = [cols[i] for i in sorted_indices]
    pcts = [pcts[i] for i in sorted_indices]
    counts = [counts[i] for i in sorted_indices]

    fig = go.Figure(go.Bar(
        x=pcts,
        y=cols,
        orientation='h',
        marker=dict(color=pcts, colorscale='Reds'),
        text=[f"{p}% ({c} rows)" for p, c in zip(pcts, counts)],
        textposition="auto"
    ))
    fig.update_layout(
        title="Missing Values by Column (%)",
        xaxis_title="Missing Percentage (%)",
        yaxis_title="Column",
        height=max(260, len(cols) * 38)
    )
    return apply_plotly_enterprise_theme(fig)


def plot_numerical_distribution(df: pd.DataFrame, col: str) -> go.Figure:
    """Plots histogram with marginal box plot for a numerical column."""
    fig = px.histogram(
        df,
        x=col,
        marginal="box",
        nbins=35,
        title=f"Distribution & Outlier Analysis: {col}",
        color_discrete_sequence=["#6366F1"]
    )
    fig.update_layout(
        xaxis_title=col,
        yaxis_title="Record Count",
        bargap=0.05
    )
    return apply_plotly_enterprise_theme(fig)


def plot_categorical_distribution(df: pd.DataFrame, col: str, max_categories: int = 15) -> go.Figure:
    """Plots frequency bar chart for a categorical column."""
    counts = df[col].astype(str).value_counts().head(max_categories).reset_index()
    counts.columns = [col, "Count"]
    total = counts["Count"].sum()
    counts["Percentage"] = (counts["Count"] / total * 100).round(1)

    fig = px.bar(
        counts,
        x=col,
        y="Count",
        text=counts["Percentage"].apply(lambda p: f"{p}%"),
        title=f"Category Frequencies: {col} (Top {len(counts)})",
        color="Count",
        color_continuous_scale="Purples"
    )
    fig.update_layout(
        xaxis_title=col,
        yaxis_title="Frequency"
    )
    return apply_plotly_enterprise_theme(fig)


def plot_correlation_heatmap(df: pd.DataFrame, numerical_cols: List[str]) -> Optional[go.Figure]:
    """Generates an interactive correlation matrix heatmap for numerical columns."""
    if len(numerical_cols) < 2:
        return None
    corr = df[numerical_cols].corr().round(2)
    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Viridis",
        zmin=-1,
        zmax=1,
        title="Feature Correlation Matrix (Pearson)"
    )
    fig.update_layout(
        height=max(420, len(numerical_cols) * 44)
    )
    return apply_plotly_enterprise_theme(fig)


def plot_scatter_relationship(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    color_col: Optional[str] = None
) -> go.Figure:
    """Plots a bivariate scatter plot between two numerical variables."""
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        color=color_col if color_col in df.columns else None,
        title=f"Bivariate Analysis: {x_col} vs {y_col}" + (f" (Grouped by {color_col})" if color_col else ""),
        opacity=0.8,
        trendline="ols" if not color_col else None,
        color_discrete_sequence=["#6366F1", "#38BDF8", "#10B981", "#F59E0B"]
    )
    return apply_plotly_enterprise_theme(fig)


def plot_class_probability_distribution(df: pd.DataFrame, target_col: str) -> go.Figure:
    """
    Unit I Syllabus Visualization:
    Visualizes empirical prior class probabilities P(C_k) = Count(C_k) / N
    based on actual dataset occurrences (NOT fabricated confidence).
    """
    clean_s = df[target_col].dropna().astype(str)
    counts = clean_s.value_counts()
    total_n = len(clean_s)
    probs = (counts / total_n).round(4)
    prob_df = pd.DataFrame({
        "Class": counts.index,
        "Count": counts.values,
        "Prior_Probability": probs.values
    })

    fig = px.bar(
        prob_df,
        x="Class",
        y="Prior_Probability",
        text=prob_df["Prior_Probability"].apply(lambda p: f"{p*100:.1f}%"),
        title=f"Unit I: Empirical Class Probability Distribution: P({target_col})",
        color="Prior_Probability",
        color_continuous_scale="Purples"
    )
    fig.update_layout(
        yaxis_title="Empirical Prior Probability P(C_k)",
        xaxis_title=f"Target Class ({target_col})",
        yaxis_range=[0, min(1.0, max(probs.values) * 1.25)]
    )
    return apply_plotly_enterprise_theme(fig)


def render_matplotlib_to_bytes(fig: plt.Figure) -> bytes:
    """
    Renders a Matplotlib figure directly into an in-memory PNG bytes buffer
    suitable for sending to the Gemini Multimodal Vision API.
    """
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=130, bbox_inches="tight", facecolor="#0F172A")
    buf.seek(0)
    image_bytes = buf.getvalue()
    buf.close()
    plt.close(fig)
    return image_bytes


def create_static_distribution_plot(df: pd.DataFrame, col: str) -> bytes:
    """Generates a static Matplotlib figure for a column and returns PNG bytes."""
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(7, 4), facecolor="#0F172A")
    ax.set_facecolor("#1E293B")
    
    if pd.api.types.is_numeric_dtype(df[col]):
        sns.histplot(df[col].dropna(), kde=True, ax=ax, color="#818CF8", edgecolor="#334155")
        ax.set_title(f"Distribution of {col}", fontsize=13, weight="bold", color="#F8FAFC")
    else:
        top_cats = df[col].astype(str).value_counts().head(8)
        sns.barplot(x=top_cats.values, y=top_cats.index, ax=ax, palette="mako")
        ax.set_title(f"Category Counts: {col}", fontsize=13, weight="bold", color="#F8FAFC")
        
    ax.set_xlabel(col, color="#CBD5E1")
    ax.tick_params(colors="#94A3B8")
    for spine in ax.spines.values():
        spine.set_color("#334155")
        
    return render_matplotlib_to_bytes(fig)
