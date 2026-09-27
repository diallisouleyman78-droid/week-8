# Week 8: HealthConnect Final Model & Data Science Package

**Track:** Data Science  
**Project:** HealthConnect — Improving Patient Appointment Attendance and Healthcare Support Using Data and AI  

## What Week 8 Delivers

This folder contains the final Data Science package for the HealthConnect project. It documents and packages the final no-show prediction model, compares it to the Week 5 baseline, and provides presentation and cross-track integration materials.

## Repository Contents

| File | Description |
|------|-------------|
| `Week8_Final_Model_Package.py` | Script that generates the final comparison tables, plot, and model summary. |
| `Week8_Final_Model_Documentation.md` | Complete model documentation: selection, evaluation, baseline comparison, limitations, business value. |
| `Week8_Presentation_Talking_Points.md` | 5–10 minute individual video script. |
| `Week8_Cross_Track_Integration.md` | Cross-track dependencies and final walkthrough. |
| `Week8_Project_Summary.md` | Week 8 progress and key outputs. |
| `requirements.txt` | Python dependencies. |

## Generated Outputs

| File | Description |
|------|-------------|
| `week8_baseline_vs_final_metrics.csv` | Metrics for baseline, Week 6 candidate, and Week 7 final. |
| `week8_threshold_0.28_metrics.csv` | Performance at the cost-optimised 0.28 threshold. |
| `week8_baseline_vs_final_performance.png` | Visual comparison of ROC-AUC and F1. |
| `week8_final_predictions.csv` | Final candidate test-set predictions. |
| `week8_final_model_summary.json` | Machine-readable model package summary. |
| `week8_final_model_selected.txt` | Short final-model selection statement. |

## Installation

```bash
cd "week 8"
pip install -r requirements.txt
```

## Build the Package

```bash
python3 Week8_Final_Model_Package.py
```

This will regenerate the comparison CSVs, the plot, and the summary files.

## Final Model

- **Model:** Logistic Regression (`improved_model_week7.pkl`)
- **Test ROC-AUC:** 0.6843
- **F1 at 0.28 threshold:** 0.6893
- **Operational threshold:** 0.28
- **Selected features:** 30

## Presentation

Use `Week8_Presentation_Talking_Points.md` to prepare your 5–10 minute individual video.
# week-8
