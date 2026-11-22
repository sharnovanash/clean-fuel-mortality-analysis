"""Step 2: exploratory analysis - death-rate distribution by continent."""
import matplotlib.pyplot as plt
import seaborn as sns

from data_utils import load_analysis_data, remove_iqr_outliers, save_figure


def main():
    df = load_analysis_data().dropna(subset=["Death_Rate", "Continent"])

    print("Death rate by continent (per 100k):")
    print(df.groupby("Continent")["Death_Rate"].describe().round(1), "\n")

    # Outlier filter (1.0 x IQR on Death_Rate)
    filtered, lo, hi = remove_iqr_outliers(df, "Death_Rate", k=1.0)
    print(f"Rows kept after 1.0xIQR filter: {len(filtered)}/{len(df)} "
          f"(bounds {lo:.1f} to {hi:.1f})")

    order = filtered.groupby("Continent")["Death_Rate"].median().sort_values().index

    fig = plt.figure(figsize=(12, 7))
    sns.boxplot(
        data=filtered, x="Continent", y="Death_Rate", order=order,
        hue="Continent", palette="Greys_r", legend=False, showfliers=False,
    )
    plt.title("Air Pollution Death Rates by Continent")
    plt.xlabel("")
    plt.ylabel("Deaths per 100,000 population")
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_figure(fig, "01_death_rate_by_continent")
    plt.close(fig)


if __name__ == "__main__":
    main()
