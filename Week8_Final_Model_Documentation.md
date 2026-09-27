# Week 8: HealthConnect Final Model & Data Science Package

**Internship Track:** Data Science  
**Project:** HealthConnect — Improving Patient Appointment Attendance and Healthcare Support Using Data and AI  
**Final Model:** Logistic Regression (`improved_model_week7.pkl`)  

---

## 1. Week 7 → Week 8 Transition

| Item | Summary |
|------|---------|
| Main Week 7 output | A validated Logistic Regression no-show model, calibrated and tested for fairness across patient segments. |
| Most important testing result | The final pipeline reproduces the Week 6 candidate predictions exactly (max probability difference = 0.0). |
| Major issue discovered | A refined model with age-specific interactions performed slightly worse (ROC-AUC 0.678) than the simpler Week 6 candidate (0.6843), so the simpler candidate was kept. |
| What was refined | Threshold cost simulation confirmed 0.28 as the operational threshold; calibration was verified. |
| Component ready | The final Logistic Regression model is ready for the ML Engineering track. |
| Still to integrate | Packaging into a reusable inference pipeline (ML Engineering) and dashboard/reporting layer (Data Analytics). |
| Tracks involved | Data Science, ML Engineering, Data Analytics, Project Management. |
| Presentation intent | Show how the no-show model reduces missed-appointment risk and connects to clinic operations. |

---

## 2. Final Integration Readiness

| Requirement | Response |
|-------------|----------|
| What is my final component? | A validated binary no-show classification model for HealthConnect. |
| What problem does it address? | Predicting which appointments are likely to be missed so the clinic can target reminders, rescheduling, or overbooking. |
| What is its current status? | Final candidate selected, tested, and documented. |
| What did I improve during Week 7? | Threshold optimisation, calibration, fairness, and reproducibility. |
| Which tracks does it depend on? | Data Analytics (segment findings), ML Engineering (pipeline integration). |
| Which tracks depend on my output? | ML Engineering (inference workflow), Project Management (final presentation). |
| What output will I provide? | Saved model, selected features, evaluation metrics, threshold rationale, and final documentation. |
| What output do I need from another track? | Data Analytics validated patient-segment insights and ML Engineering requirements. |
| What evidence demonstrates readiness? | Same test-set ROC-AUC 0.6843, F1@0.28 = 0.6893, and exact reproduction of Week 7 probabilities. |
| What limitations remain? | Moderate AUC, limited by the data; age 45-54 and 65+ segments have lower F1. |

---

## 3. Final Candidate Model

- **Model:** Logistic Regression with `class_weight='balanced'`, `C=1.0`, `max_iter=2000`, `random_state=42`.
- **Features:** 30 selected features (from Recursive Feature Elimination and testing in Weeks 6/7).
- **Threshold for intervention:** 0.28 (cost-optimised, false-negative cost = 3 × false-positive cost).
- **Key hyperparameters / decisions:**
  - Patient-level `GroupShuffleSplit` prevents data leakage.
  - StandardScaler fit on training data only.
  - RFE reduced the feature set to the most stable 30 inputs.

## 4. Model Evaluation

### 4.1 Test-set metrics (default 0.5 threshold)

| Metric | Value |
|--------|-------|
| Accuracy | 0.6315 |
| Precision | 0.6331 |
| Recall | 0.6253 |
| F1 | 0.6292 |
| ROC-AUC | **0.6843** |
| Brier score | 0.2247 |

### 4.2 Cost-optimised threshold (0.28)

| Metric | Value |
|--------|-------|
| Accuracy | 0.5642 |
| Precision | 0.5356 |
| Recall | 0.9669 |
| F1 | **0.6893** |
| ROC-AUC | 0.6843 |
| Brier | 0.2247 |

*Why 0.28?* A missed appointment costs more than an unnecessary intervention. The 0.28 threshold minimises total expected cost while keeping recall very high (≈97%).

## 5. Baseline vs Final Comparison

| Stage | ROC-AUC | F1 (default) | Brier |
|-------|---------|--------------|-------|
| Week 5 Baseline | 0.652 | 0.600 | — |
| Week 6 Candidate | 0.6843 | 0.6292 | 0.2247 |
| **Week 7 Final** | **0.6843** | **0.6292** | **0.2247** |

- **AUC improvement vs baseline:** +0.032 (≈ 4.9% relative).
- **F1 at 0.28:** 0.6893 vs the baseline's F1 0.600 at 0.5.
- The final model retains the Week 6 candidate exactly; Week 7 only validated and refined the surrounding workflow.

## 6. Error Analysis Summary

- The model is **well calibrated** — predicted probabilities align with observed no-show rates across bins.
- **Segment F1 at 0.28** is lowest for age group **45-54** and **65+**, indicating these groups need different intervention strategies or additional features.
- **Random Forest and XGBoost** reached similar AUC but were less stable, so Logistic Regression was selected for interpretability and operational simplicity.

## 7. Feature & Model Decisions

1. Kept the **Week 6 Logistic Regression** as the final because the Week 7 refinement did not improve AUC.
2. Selected 30 features via **RFE** to reduce noise while keeping the strongest predictors.
3. Engineered **interaction terms** (`age_x_distance`, `age_x_lead`, `lead_x_no_show_rate`) and **non-linear terms** (`log_distance`, `lead_days_squared`, `distance_squared`) based on Data Analytics findings.
4. Used **patient-level split** to prevent leakage across appointments of the same patient.

## 8. Business Interpretation

- The model can **flag high-risk appointments** at the 0.28 threshold for proactive outreach.
- The most predictive features (`no_show_rate`, `booking_lead_days`, `distance_to_clinic_km`, `age`) match business intuition: past behaviour, long lead times, and distance increase no-show risk.
- Expected value: fewer unfilled slots, better resource planning, and more targeted patient support.

## 9. Limitations and Risks

- **AUC 0.68 is moderate.** The model is best used for risk tiering, not as a sole automated decision maker.
- **Data limitations:** Synthetic data with a fixed set of 5,000 appointments; real-world patterns may differ.
- **Age segments 45-54 and 65+ are harder to predict** — these groups may need tailored follow-up.
- The model does **not explain causality** and should be monitored for drift in `booking_lead_days` and `distance_to_clinic_km`.

## 10. Cross-Track Contribution

| Track | Output Received | How It Influenced the Model |
|-------|-----------------|-----------------------------|
| Data Analytics | Validated no-show patterns by age, distance, and appointment type | Guided feature engineering and segment analysis. |
| ML Engineering | Pipeline constraints and input/output requirements | Ensured the final model can be integrated cleanly. |
| Data Science → ML Engineering | Final model, selected features, threshold, and scaler | ML Engineering can build the production inference pipeline. |
| Data Science → PM | Model metrics, limitations, and business interpretation | PM can include risk and value framing in the final presentation. |

## 11. Files Provided

| File | Description |
|------|-------------|
| `improved_model_week7.pkl` | Final Logistic Regression model. |
| `scaler_week7.pkl` | StandardScaler fit on the training set. |
| `improved_model_features_week7.pkl` | 30 selected features in model order. |
| `week8_baseline_vs_final_metrics.csv` | Quantitative baseline-to-final comparison. |
| `week8_threshold_0.28_metrics.csv` | Performance at the operational threshold. |
| `week8_baseline_vs_final_performance.png` | Visual comparison. |
| `week8_final_predictions.csv` | Candidate test-set predictions. |
| `week8_final_model_summary.json` | Machine-readable final package summary. |
