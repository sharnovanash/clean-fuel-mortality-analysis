"""Shared data loading and cleaning helpers."""
import numpy as np
import pandas as pd

import config


def extract_primary_value(val):
    """Pull the point estimate out of a WHO string such as '95.12 [85.12-104.3]'.

    Returns NaN when no number can be parsed. Symbols such as '>' or '<'
    (e.g. '>95') are stripped, so '>95' becomes 95.0.
    """
    if pd.isna(val):
        return np.nan
    first_part = str(val).split()[0] if str(val).split() else ""
    clean_val = "".join(c for c in first_part if c.isdigit() or c == ".")
    try:
        return float(clean_val)
    except ValueError:
        return np.nan


def load_analysis_data(totals_only=config.TOTALS_ONLY):
    """Load the merged dataset and add numeric Death_Rate / Fuel_Access columns.

    Parameters
    ----------
    totals_only : bool
        If True (default), keep one row per country (all causes, both sexes,
        one death-rate indicator - see config.py). If False, keep every
        indicator x sex x cause row, as in the original analysis.
    """
    if not config.MERGED_CSV.exists():
        raise FileNotFoundError(
            f"{config.MERGED_CSV} not found. Run `python src/01_merge_data.py` first."
        )

    df = pd.read_csv(config.MERGED_CSV)

    if totals_only:
        df = df[
            (df["Dim1"] == config.SEX_FILTER)
            & (df["Dim2"] == config.CAUSE_FILTER)
            & (df["Indicator_x"] == config.INDICATOR_FILTER)
        ]
        assert df["Location"].is_unique, "Expected one row per country after filtering"

    df = df.copy()
    df["Death_Rate"] = df["First Tooltip_x"].apply(extract_primary_value)
    df["Fuel_Access"] = df["First Tooltip_y"].apply(extract_primary_value)
    return df


def remove_iqr_outliers(df, column="Death_Rate", k=1.5):
    """Drop rows whose `column` falls outside [Q1 - k*IQR, Q3 + k*IQR].

    Returns (filtered_df, lower_bound, upper_bound).
    """
    q1, q3 = df[column].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - k * iqr, q3 + k * iqr
    return df[df[column].between(lower, upper)].copy(), lower, upper


def save_figure(fig, name):
    """Save a matplotlib figure to figures/<name>.png and return the path."""
    path = config.FIGURES_DIR / f"{name}.png"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"Saved figure -> {path.relative_to(config.ROOT)}")
    return path


def save_text(text, name):
    """Save text output (e.g. a regression summary) to <name>.txt in the main folder."""
    path = config.RESULTS_DIR / f"{name}.txt"
    path.write_text(str(text))
    print(f"Saved results -> {path.relative_to(config.ROOT)}")
    return path
