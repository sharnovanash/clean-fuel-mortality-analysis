# Clean Cooking Fuel Access and Air Pollution Mortality

Does access to clean cooking fuels and technologies go with lower death rates from air pollution? Merged two World Health Organization (WHO) datasets for **179 countries (2016)**. Tests that relationship with linear, logarithmic and multiple regression models.

![Linear vs logarithmic fit](figures/06_linear_vs_log_fit.png)

## Key findings

| Model | R² | AIC | Key coefficient |
|---|---|---|---|
| Linear: `Death_Rate ~ Fuel_Access` | 0.732 | 1809 | −1.69 deaths per 100k per +1 pt of access (p < 0.001) |
| Log-linear: `Death_Rate ~ log(1 + Fuel_Access)` | 0.651 | 1856 | −56.1 per unit of log access (p < 0.001) |
| Multiple: `Death_Rate ~ Fuel_Access + Continent` | 0.791 | 1775 | −1.50 per +1 pt of access, controlling for continent (p < 0.001) |

- **Strong negative association.** Each extra percentage point of the population relying on clean fuels goes with about **1.7 fewer air-pollution deaths per 100,000 people**. Clean-fuel access alone explains about 73% of the variation between countries.
- **The linear model fits better than the logarithmic one.** It has a higher R² and a lower AIC and BIC. The data do not strongly support a "diminishing returns" curve: the benefit continues across the whole 0–100% range.
- **Region still matters.** With fuel access held constant, Europe, the Americas and Oceania have significantly lower death rates than Africa. Asia does not differ significantly from Africa. Adding continent raises R² to 0.79, so other regional factors also play a part, such as outdoor air pollution and access to health care.

*These are cross-sectional correlations. They do not prove that clean fuel causes lower mortality.*

## Project structure

```
.
├── data/
│   ├── raw/                         # Original WHO exports (unchanged)
│   │   ├── airPollutionDeathRate.csv
│   │   └── cleanFuelAndTech.csv
│   └── processed/
│       └── merged_data_by_continent.csv   # Created by 01_merge_data.py
├── src/
│   ├── config.py                    # Paths and analysis settings
│   ├── data_utils.py                # Shared loading/cleaning helpers
│   ├── continents.py                # Country -> continent lookup
│   ├── 01_merge_data.py             # Merge datasets and add continent
│   ├── 02_eda_boxplot.py            # Death-rate distribution by continent
│   ├── 03_linear_regression.py      # Simple OLS + LOWESS smoother
│   ├── 04_log_regression.py         # Log-linear model (outliers removed)
│   ├── 05_model_comparison.py       # Linear vs log: metrics, fit, residuals
│   ├── 06_multiple_regression.py    # OLS with continent controls
│   └── check_continent_mapping.py   # Lists any unmapped countries
├── sql/
│   └── merge_tables.sql             # Same merge written in SQL
├── figures/                         # All generated charts (PNG)
├── results/                         # Regression summaries (TXT)
├── run_all.py                       # Runs the whole pipeline
└── requirements.txt
```

## Getting started

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python run_all.py                # or run any script in src/ on its own
```

The charts are saved to `figures/` and the model summaries to `results/`.

## Data

| File | Source | Description |
|---|---|---|
| `airPollutionDeathRate.csv` | WHO Global Health Observatory | Deaths per 100,000 people attributed to outdoor and household air pollution, 2016. Includes crude and age-standardized rates, by sex and cause. |
| `cleanFuelAndTech.csv` | WHO Global Health Observatory | Share of the population that relies mainly on clean fuels and technologies for cooking (%), multiple years. |

The two files are joined on country and year. Only 2016 appears in both, so the analysis covers a single year.

### Cleaning decisions

- **One row per country.** The death-rate file has 36 rows for each country: 2 indicators × 3 sex groups × 6 causes. The analysis keeps the **age-standardized, both-sexes, all-causes** rate. Age standardization lets countries with different age structures be compared fairly. You can change this in `src/config.py`: set `INDICATOR_FILTER = CRUDE` to use the crude rate, or `TOTALS_ONLY = False` to pool every row.
- **Point estimates.** WHO values such as `95.12 [85.12-104.3]` are reduced to the point estimate (`95.12`). The uncertainty interval is dropped.
- **Outliers.** The box plot uses a 1.0 × IQR filter for display, and the log model uses a 1.5 × IQR filter. The other models use every country.

## Limitations

- **Single year (2016), cross-sectional.** The results show association, not causation.
- **Capped values.** WHO caps fuel access at 95% and 5%: countries above or below those levels are recorded as exactly 95 or 5. This creates the vertical clusters at both ends of the scatter plots and hides differences among high-access countries.
- **Confounders not modeled.** Income, urbanization, outdoor PM2.5 levels and health-care access all affect mortality. Continent dummies capture only part of this.
