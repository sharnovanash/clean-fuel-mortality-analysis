"""Step 6: multiple regression controlling for continent.

Death_Rate ~ Fuel_Access + Continent dummies (Africa = reference group).
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

from data_utils import load_analysis_data, save_figure, save_text


def main():
    df = load_analysis_data().dropna(subset=["Fuel_Access", "Death_Rate", "Continent"])

    # drop_first=True makes Africa (first alphabetically) the reference group
    df_multi = pd.get_dummies(
        df[["Fuel_Access", "Death_Rate", "Continent"]],
        columns=["Continent"], drop_first=True,
    )
    X = sm.add_constant(df_multi.drop(columns=["Death_Rate"])).astype(float)
    y = df_multi["Death_Rate"]

    model = sm.OLS(y, X).fit()
    print("===== MULTIPLE REGRESSION SUMMARY =====")
    print(model.summary())
    save_text(model.summary(), "multiple_regression_summary")

    # --- Coefficient chart ---
    coefs = model.params.drop("const").sort_values()
    coefs.index = [
        "Clean fuel access (per +1 pt)" if c == "Fuel_Access" else c.replace("Continent_", "")
        for c in coefs.index
    ]
    fig = plt.figure(figsize=(12, 8))
    coefs.plot(kind="barh", color="#003366", width=0.8)
    plt.axvline(0, color="black", linestyle="--", linewidth=1)
    plt.title("Effect on Death Rate: Fuel Access vs Continent (ref. = Africa)", fontsize=15)
    plt.xlabel("Coefficient (deaths per 100k)", fontsize=12)
    plt.grid(False)
    plt.tight_layout()
    save_figure(fig, "09_multiple_regression_coefficients")
    plt.close(fig)

    # --- Scatter by continent with overall trend ---
    fig = plt.figure(figsize=(12, 7))
    sns.scatterplot(data=df, x="Fuel_Access", y="Death_Rate", hue="Continent",
                    palette="viridis", s=70, alpha=0.8, edgecolor="w")
    sns.regplot(data=df, x="Fuel_Access", y="Death_Rate", scatter=False, color="black",
                line_kws={"linestyle": "--", "linewidth": 2})
    plt.title("Clean Fuel Access and Death Rate by Continent", fontsize=14)
    plt.xlabel("Clean Fuel Access (%)", fontsize=12)
    plt.ylabel("Death Rate (per 100k)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend(title="Continent", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    save_figure(fig, "10_scatter_by_continent_trend")
    plt.close(fig)


if __name__ == "__main__":
    main()
