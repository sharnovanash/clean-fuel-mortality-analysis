"""Step 4: log-linear model, Death_Rate ~ log(1 + Fuel_Access), outliers removed.

Tests the "diminishing returns" hypothesis: the first gains in clean-fuel
access are associated with the largest drops in mortality.
"""
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

from data_utils import load_analysis_data, remove_iqr_outliers, save_figure, save_text


def main():
    df_model = load_analysis_data()[["Fuel_Access", "Death_Rate"]].dropna()

    # Remove extreme Death_Rate values (1.5 x IQR)
    df_clean, _, upper = remove_iqr_outliers(df_model, "Death_Rate", k=1.5)
    print(f"Original rows: {len(df_model)} | after outlier removal: {len(df_clean)} "
          f"(removed {len(df_model) - len(df_clean)})")

    # log1p handles 0% access safely
    df_clean["Log_Fuel_Access"] = np.log1p(df_clean["Fuel_Access"])
    X_log = sm.add_constant(df_clean["Log_Fuel_Access"])
    log_model = sm.OLS(df_clean["Death_Rate"], X_log).fit()

    print("\n===== LOG REGRESSION SUMMARY (outliers removed) =====")
    print(log_model.summary())
    save_text(log_model.summary(), "log_regression_summary")

    # Fitted curve across 0-100%
    fuel_range = np.linspace(0, 100, 500)
    predicted = log_model.predict(sm.add_constant(np.log1p(fuel_range)))

    for name, xmax in [("04_log_fit_full_range", 100), ("05_log_fit_0_50_zoom", 50)]:
        fig = plt.figure(figsize=(10, 6))
        plt.scatter(df_clean["Fuel_Access"], df_clean["Death_Rate"], alpha=0.5,
                    color="#003366", label="Countries (outliers removed)")
        plt.plot(fuel_range, predicted, color="#d9534f", linewidth=3, label="Logarithmic fit")
        plt.xlim(0, xmax)
        plt.ylim(0, upper + 10)
        suffix = "" if xmax == 100 else f" (0-{xmax}% Zoom)"
        plt.title(f"Logarithmic Regression: Fuel Access vs Mortality{suffix}", fontsize=14)
        plt.xlabel("Clean Fuel Access (%)", fontsize=12)
        plt.ylabel("Death Rate (per 100k)", fontsize=12)
        plt.legend()
        plt.tight_layout()
        save_figure(fig, name)
        plt.close(fig)


if __name__ == "__main__":
    main()
