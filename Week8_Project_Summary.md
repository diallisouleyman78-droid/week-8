# Week 8 Project Summary — HealthConnect Final Model & Data Science Package

**Track:** Data Science  
**Project:** HealthConnect — Improving Patient Appointment Attendance and Healthcare Support Using Data and AI  
**Date:** 27 September 2026  

## 1. Planned Deliverables

Complete the HealthConnect no-show prediction work by:

1. Confirming the final candidate model.
2. Evaluating the final model on the held-out test set.
3. Comparing final performance against the Week 5 baseline.
4. Documenting model decisions, business value, limitations, and risks.
5. Describing cross-track integration and how the model connects to the broader solution.
6. Preparing presentation talking points for a non-technical audience.

## 2. Completed

- Created `Week8_Final_Model_Package.py` which generates the final comparison tables, plot, and summary.
- Produced `week8_baseline_vs_final_metrics.csv`, `week8_threshold_0.28_metrics.csv`, `week8_baseline_vs_final_performance.png`, `week8_final_predictions.csv`, `week8_final_model_summary.json`.
- Wrote `Week8_Final_Model_Documentation.md` covering model selection, evaluation, baseline comparison, error analysis, business interpretation, limitations, and cross-track contribution.
- Wrote `Week8_Presentation_Talking_Points.md` for the 5–10 minute individual video.
- Wrote `Week8_Cross_Track_Integration.md` documenting dependencies and the final walkthrough.
- Wrote `README.md`, `requirements.txt`, and social-media posts.

## 3. Final Model

| Attribute | Value |
|-----------|-------|
| Model | Logistic Regression |
| Selected features | 30 |
| Test ROC-AUC | 0.6843 |
| F1 at 0.28 threshold | 0.6893 |
| Brier score | 0.2247 |
| Operational threshold | 0.28 |

## 4. Baseline vs Final

| Stage | ROC-AUC | F1 (default) | Brier |
|-------|---------|--------------|-------|
| Week 5 Baseline | 0.652 | 0.600 | — |
| **Week 7 Final** | **0.6843** | **0.6292** | **0.2247** |

The final model improves AUC by 0.032 and F1 at the operational threshold by 0.089 over the baseline at 0.5.

## 5. Key Decisions

- Selected the simpler Week 6 Logistic Regression over the Week 7 refined interaction model because the refined model did not improve AUC.
- Used a cost-optimised 0.28 threshold to reflect the higher cost of missing a no-show.
- Maintained a patient-level train/test split to prevent leakage across appointments of the same patient.

## 6. Limitations

- AUC of 0.68 is moderate; the model should be used for risk tiering, not fully automated decisions.
- Age 45-54 and 65+ segments are harder to predict.
- The dataset is synthetic and limited to 5,000 appointments.

## 7. Cross-Track Outputs

- **To ML Engineering:** final model, scaler, feature list, and threshold (`DataScience_to_ML_Engineering_Week7.md`).
- **To Project Management:** metrics, limitations, and business value framing.
- **From Data Analytics:** validated patient-segment insights that guided feature engineering.
