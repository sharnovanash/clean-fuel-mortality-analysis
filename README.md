# Clean Fuel, Cleaner Air, Fewer Deaths

## Project Description

Measured how access to clean cooking fuel relates to air-pollution death rates across 179 countries using World Health Organization (WHO) data. The question was simple: do countries where more people cook with clean fuel see fewer deaths from air pollution?

The short answer is yes. Each extra percentage point of clean-fuel access goes with 1.7 fewer deaths per 100,000 people, and fuel access alone explains 73% of the variation between countries.

![Clean fuel access vs death rate](figures/03_linear_fit_by_continent.png)

## Process

| Step | Process |
|---|---|
| Defined | Asked how a country's clean-fuel access relates to its air-pollution death rate. |
| Merged | Joined two [WHO datasets](https://www.kaggle.com/datasets/utkarshxy/who-worldhealth-statistics-2020-complete) on country + year in [Python](src/01_merge_data.py) and [SQL](merge_tables.sql). Mapped each country to a continent. |
| Parsed | Extracted numbers from WHO text values like `"95.12 [85.12-104.3]"`. |
| Deduplicated | Found 36 rows per country (2 measures × 3 sexes × 6 causes). Kept one age-standardized total per country. Raised R² from 0.14 to 0.73. |
| Explored | Compared death rates by continent. Africa's median (162) is 7× Europe's (24). |
| Modeled | Tested linear, logarithmic and multiple regression. |

## Models

| Model | R² | AIC | Fuel effect |
|---|---|---|---|
| Linear | 0.73 | 1809 | −1.69 per point |
| Logarithmic | 0.65 | 1856 | −56.1 per log unit |
| Linear + continent (best) | 0.79 | 1775 | −1.50 per point |

All fuel effects are significant (p < 0.001).

![Linear vs logarithmic fit](figures/06_linear_vs_log_fit.png)

## Findings

- Higher clean-fuel access means significantly lower mortality, so I rejected the null hypothesis.
- The log model fit worse, which rules out diminishing returns. Gains hold at every level of access.
- After controlling for region, fuel stays the strongest driver. Oceania, the Americas and Europe still show lower death rates than Africa at the same access level.
- The key lesson: checking the data's structure mattered more than model choice. Removing duplicate rows changed which model won.

![Regression coefficients](figures/09_multiple_regression_coefficients.png)

## Limitations

- The data covers one year (2016) and shows correlation only, not causation.
- WHO caps reported access at 5% and 95%.
- Income and outdoor pollution are not modeled.

## Code

- `run_all.py` runs the full pipeline. It produces the charts in `figures/` and the regression summaries as `.txt` files in the main folder.
- `src/01_merge_data.py` merges and cleans the WHO data.
- `merge_tables.sql` performs the same merge in SQL.
- `requirements.txt` lists the Python packages used: pandas, statsmodels and seaborn.

## Run It

    git clone https://github.com/<your-username>/<repo-name>.git
    cd <repo-name>
    pip install -r requirements.txt
    python run_all.py
