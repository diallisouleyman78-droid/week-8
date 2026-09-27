# Week 8: Individual Presentation Talking Points (Data Science)

**Target length:** 5–10 minutes  
**Track:** Data Science  
**Project:** HealthConnect — Predicting and Reducing Patient No-Shows

---

## 1. Introduction (30–60 seconds)

- Hello, my name is [Your Name].
- I am a Data Science intern on the HealthConnect project.
- The problem: HealthConnect Clinic wants to reduce missed appointments and use its slots more effectively.
- My focus: building and validating a no-show prediction model that the clinic can use to flag high-risk appointments.

## 2. My Track Contribution (2–3 minutes)

- In Weeks 5 and 6 I developed and improved baseline and candidate models.
- In Week 7 I tested the candidate for reproducibility, calibration, and fairness.
- My final deliverable is a **Logistic Regression** no-show model:
  - 30 selected features.
  - **ROC-AUC = 0.6843** on the held-out patient-level test set.
  - **F1 = 0.6893** at the operational threshold of **0.28**.
- Tools used: Python, pandas, scikit-learn, XGBoost (for comparison), and matplotlib.
- Key decision: after comparing several models, Logistic Regression was chosen for its balance of performance, stability, and interpretability.

## 3. Cross-Track Collaboration (1–2 minutes)

- I received validated patient-segment findings from the **Data Analytics** track.
  - These informed interaction features such as `age_x_distance` and `lead_x_no_show_rate`.
- I provided my final model, feature list, scaler, and threshold to the **ML Engineering** track.
  - This is what they need to build a reproducible inference pipeline.
- I shared model limitations and business interpretation with the **Project Management** track.
  - They can explain value and risks to stakeholders.

## 4. Testing, Refinement & Final Outcome (1–2 minutes)

- I tested on a **patient-level held-out test set** to avoid data leakage.
- I compared the final model to the **Week 5 baseline**:
  - ROC-AUC improved from **0.652 to 0.6843**.
  - F1 at the cost-optimised threshold reached **0.6893**.
- I ran threshold cost simulation and found **0.28** is the best intervention point.
- I verified the model is **calibrated** and that the pipeline produces **exactly the same** probabilities on every run.

## 5. Overall HealthConnect Solution (1–2 minutes)

- The Data Science model is the predictive engine of the solution.
- It connects to:
  - **Data Analytics** — dashboards and segment insights.
  - **ML Engineering** — the operational scoring pipeline.
  - **GenAI / Project Management** — patient communication and project coordination.
- Business value: the clinic can now prioritise reminders or overbooking for appointments with a no-show probability ≥ 0.28.

## 6. Closing (30–60 seconds)

- Key takeaway: a simple, validated, and well-documented model is more useful than a complex black box in a healthcare setting.
- What I learned: the importance of reproducibility, threshold optimisation, and cross-track communication.
- Future improvement: collect more granular patient history, transport-barrier data, and SMS response behaviour to push AUC beyond 0.68.
