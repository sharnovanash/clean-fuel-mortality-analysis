"""Step 1: merge the WHO death-rate and clean-fuel datasets and add continents.

Inputs : data/raw/airPollutionDeathRate.csv, data/raw/cleanFuelAndTech.csv
Output : data/processed/merged_data_by_continent.csv
"""
import pandas as pd

import config
from continents import CONTINENT_MAP


def main():
    # 1. Load (utf-8-sig strips the byte-order mark in the WHO exports)
    air = pd.read_csv(config.DEATH_RATE_CSV, encoding="utf-8-sig")
    fuel = pd.read_csv(config.CLEAN_FUEL_CSV, encoding="utf-8-sig")

    # 2. Drop rows missing merge keys and align Period types
    air = air.dropna(subset=["Location", "Period"])
    fuel = fuel.dropna(subset=["Location", "Period"])
    air["Period"] = air["Period"].astype(int)
    fuel["Period"] = fuel["Period"].astype(int)

    # 3. Inner join on country + year
    merged = pd.merge(air, fuel, on=["Location", "Period"], how="inner")

    # 4. Add continent
    merged["Continent"] = merged["Location"].map(CONTINENT_MAP)

    unmapped = merged.loc[merged["Continent"].isna(), "Location"].unique()
    if len(unmapped):
        print(f"WARNING: {len(unmapped)} countries have no continent: {list(unmapped)}")

    # 5. Save
    merged.to_csv(config.MERGED_CSV, index=False)
    print(f"Merged rows: {len(merged)} | countries: {merged['Location'].nunique()} "
          f"| years: {sorted(merged['Period'].unique())}")
    print(f"Saved -> {config.MERGED_CSV.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
