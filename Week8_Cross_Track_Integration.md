# Week 8: Cross-Track Integration — Data Science

## Integration Matrix

| From Track | To Track | Output | How It Improves the Solution | Evidence |
|------------|----------|--------|------------------------------|----------|
| Data Analytics | Data Science | Validated no-show patterns by age, distance, appointment type, and lead time | Guided feature engineering and model interpretation | `Data_Analytics_to_DataScience_Week6.md`, interaction features in final model |
| Data Science | ML Engineering | Final model (`improved_model_week7.pkl`), 30 selected features, scaler, 0.28 threshold | Enables a reproducible inference pipeline | `DataScience_to_ML_Engineering_Week7.md` |
| ML Engineering | Data Science | Pipeline input/output requirements and constraints | Confirmed model compatibility and scoring format | `DataScience_to_ML_Engineering_Week7.md` |
| Data Science | Project Management | Metrics, limitations, and business value framing | Supports final presentation and risk register | `Week8_Final_Model_Documentation.md` |
| Data Analytics | Project Management | KPIs and business insights | Informs final recommendations | `Week8_Cross_Track_Integration.md` |

## Final Integration Walkthrough Contribution

### 1. The Problem
HealthConnect Clinic needs to reduce missed appointments and make better use of appointment slots.

### 2. The Data
5,000 appointment records with patient, booking, and outcome information.

### 3. The Analytics
Data Analytics identified key patterns: longer lead times, greater distances, and certain age groups increase no-show likelihood.

### 4. The Predictive Component (Data Science)
A Logistic Regression model with ROC-AUC 0.6843 and F1 0.6893 at the 0.28 threshold.

### 5. The ML Engineering Component
ML Engineering will take the saved model and wrap it into an end-to-end inference pipeline.

### 6. The Project Management Layer
PM will coordinate final presentation, risks, and business recommendations.

### 7. Business Value
Clinic staff can flag high-risk appointments and prioritise reminders or rescheduling.

### 8. Limitations
Moderate AUC, limited real-world data, and harder-to-predict age segments require ongoing monitoring.

## Key Dependencies Resolved

- Model trained and tested using patient-level split (no data leakage).
- Threshold chosen through cost simulation aligned to clinic priorities.
- All model artefacts saved and documented for ML Engineering.
