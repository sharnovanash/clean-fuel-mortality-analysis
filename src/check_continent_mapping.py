"""Utility: list any countries in the merged data that have no continent."""
import pandas as pd

import config


def main():
    df = pd.read_csv(config.MERGED_CSV)
    print(f"Total rows: {len(df)}")
    missing = df["Continent"].isna().sum()
    print(f"Rows with missing Continent: {missing}")
    if missing:
        print("Countries that failed to map:")
        for c in sorted(df.loc[df["Continent"].isna(), "Location"].unique()):
            print(f"  - {c}")
    else:
        print("All countries mapped to a continent.")


if __name__ == "__main__":
    main()
