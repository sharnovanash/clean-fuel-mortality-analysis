"""Project paths and shared settings.

All paths are relative to the repository root, so the project runs on any
machine without editing hard-coded paths.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
FIGURES_DIR = ROOT / "figures"
RESULTS_DIR = ROOT  # summaries are saved in the main folder

DEATH_RATE_CSV = RAW_DIR / "airPollutionDeathRate.csv"
CLEAN_FUEL_CSV = RAW_DIR / "cleanFuelAndTech.csv"
MERGED_CSV = PROCESSED_DIR / "merged_data_by_continent.csv"

# The WHO death-rate file has, for every country, one row per
#   indicator (crude vs age-standardized) x sex (Dim1) x cause (Dim2)
# = 36 rows per country. For country-level analysis we keep exactly one row
# per country. Set TOTALS_ONLY = False to reproduce the original analysis
# that pooled every row together.
TOTALS_ONLY = True
SEX_FILTER = "Both sexes"
CAUSE_FILTER = "Total"

# Age-standardized rates adjust for differences in population age structure,
# which is the standard choice for comparing countries. Switch to CRUDE to
# use the raw (non-adjusted) death rate instead.
AGE_STANDARDIZED = (
    "Ambient and household air pollution attributable death rate "
    "(per 100 000 population, age-standardized)"
)
CRUDE = "Ambient and household air pollution attributable death rate (per 100 000 population)"
INDICATOR_FILTER = AGE_STANDARDIZED

for _d in (PROCESSED_DIR, FIGURES_DIR):
    _d.mkdir(parents=True, exist_ok=True)
