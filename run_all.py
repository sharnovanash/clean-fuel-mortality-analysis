"""Run the full pipeline in order: merge -> EDA -> models.

Usage:  python run_all.py
"""
import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent / "src"
STEPS = [
    "01_merge_data.py",
    "check_continent_mapping.py",
    "02_eda_boxplot.py",
    "03_linear_regression.py",
    "04_log_regression.py",
    "05_model_comparison.py",
    "06_multiple_regression.py",
]

for step in STEPS:
    print(f"\n{'=' * 60}\n>>> {step}\n{'=' * 60}")
    subprocess.run([sys.executable, str(SRC / step)], cwd=SRC, check=True)

print("\nDone. Figures are in figures/, model summaries are the .txt files in the main folder.")
