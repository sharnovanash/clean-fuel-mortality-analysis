"""Step 5: compare the linear and log-linear models.

Both models are fit on the same rows (no outlier removal) so their
R-squared, AIC and BIC are directly comparable. Also produces a
side-by-side fit plot, a residual plot and a binned-average trend.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

from data_utils import load_analysis_data, save_figure, save_text


def main():
    df = load_analysis_data()[["Fuel_Access", "Death_Rate"]].dropna().copy()
    df["Log_Fuel_Access"] = np.log1p(df["Fuel_Access"])
    y = df["Death_Rate"]

    linear = sm.OLS(y, sm.add_constant(df["Fuel_Access"])).fit()
    log = sm.OLS(y, sm.add_constant(df["Log_Fuel_Access"])).fit()

    comparison = pd.DataFrame({
        "Metric": ["R-squared", "AIC", "BIC", "Residual skew", "Residual kurtosis"],
        "Linear": [linear.rsquared, linear.aic, linear.bic,
                   linear.resid.skew(), linear.resid.kurtosis()],
        "Log-linear": [log.rsquared, log.aic, log.bic,
                       log.resid.skew(), log.resid.kurtosis()],
    })
    comparison["Change"] = comparison["Log-linear"] - comparison["Linear"]
    comparison = comparison.round(4)

    print("\n===== MODEL METRIC COMPARISON =====")
    print(comparison.to_string(index=False))
    save_text(comparison.to_string(index=False), "model_comparison")

    # --- Fit comparison plot ---
    order = df["Fuel_Access"].argsort().values
    xs = df["Fuel_Access"].values[order]
    fig = plt.figure(figsize=(10, 6))
    plt.scatter(df["Fuel_Access"], y, alpha=0.4, color="gray", label="Countries")
    plt.plot(xs, linear.fittedvalues.values[order], color="blue",
             label=f"Linear fit (R²={linear.rsquared:.3f})")
    plt.plot(xs, log.fittedvalues.values[order], color="red", linewidth=3,
             label=f"Logarithmic fit (R²={log.rsquared:.3f})")
    plt.title("Model Comparison: Linear vs. Logarithmic")
    plt.xlabel("Clean Fuel Access (%)")
    plt.ylabel("Death Rate (per 100k)")
    plt.legend()
    plt.tight_layout()
    save_figure(fig, "06_linear_vs_log_fit")
    plt.close(fig)

    # --- Residual plot for the log model ---
    fig = plt.figure(figsize=(10, 5))
    plt.scatter(log.fittedvalues, log.resid, alpha=0.5, color="green")
    plt.axhline(0, color="black", linestyle="--")
    plt.title("Residual Plot: Logarithmic Model")
    plt.xlabel("Predicted Death Rate")
    plt.ylabel("Residual (prediction error)")
    plt.tight_layout()
    save_figure(fig, "07_log_model_residuals")
    plt.close(fig)

    # --- Binned average trend ---
    bins = pd.cut(df["Fuel_Access"], bins=10)
    binned = df.groupby(bins, observed=False)["Death_Rate"].mean()
    fig = plt.figure(figsize=(10, 6))
    plt.plot([f"{int(b.left)}-{int(b.right)}" for b in binned.index],
             binned.values, marker="o")
    plt.title("Average Death Rate by Clean Fuel Access Bin")
    plt.xlabel("Clean Fuel Access (%)")
    plt.ylabel("Average Death Rate (per 100k)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_figure(fig, "08_binned_average_trend")
    plt.close(fig)


if __name__ == "__main__":
    main()
