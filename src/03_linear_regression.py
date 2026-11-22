"""Step 3: simple linear regression of death rate on clean-fuel access."""
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

from data_utils import load_analysis_data, save_figure, save_text


def main():
    df = load_analysis_data()
    df_model = df[["Fuel_Access", "Death_Rate"]].dropna()

    # OLS: Death_Rate = b0 + b1 * Fuel_Access
    X = sm.add_constant(df_model["Fuel_Access"])
    model = sm.OLS(df_model["Death_Rate"], X).fit()
    print(model.summary())
    save_text(model.summary(), "linear_regression_summary")

    plt.style.use("seaborn-v0_8-whitegrid")

    # Figure 1: LOWESS-smoothed relationship
    fig = plt.figure(figsize=(8, 6))
    sns.regplot(
        x="Fuel_Access", y="Death_Rate", data=df_model,
        scatter=False, lowess=True,
        line_kws={"color": "#050B5F", "linewidth": 3},
    )
    plt.title("Smoothed Relationship Between Clean Fuel Access and Mortality")
    plt.xlabel("Clean Fuel Access (%)")
    plt.ylabel("Death Rate (per 100k)")
    plt.tight_layout()
    save_figure(fig, "02_lowess_fuel_vs_death_rate")
    plt.close(fig)

    # Figure 2: scatter by continent with the linear fit
    fig = plt.figure(figsize=(12, 7))
    sns.scatterplot(data=df, x="Fuel_Access", y="Death_Rate", hue="Continent", alpha=0.7)
    sns.regplot(
        data=df_model, x="Fuel_Access", y="Death_Rate", scatter=False,
        line_kws={"color": "black", "linewidth": 2},
    )
    plt.grid(False)
    plt.title("Fuel Access vs Air Pollution Death Rate by Continent")
    plt.xlabel("Access to Clean Fuel (%)")
    plt.ylabel("Death Rate (per 100k)")
    plt.legend(title="Continent", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    save_figure(fig, "03_linear_fit_by_continent")
    plt.close(fig)


if __name__ == "__main__":
    main()
