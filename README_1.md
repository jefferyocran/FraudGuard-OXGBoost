# FraudGuard-OXGBoost

**O-XGBoost: An Engineered Focal-Loss XGBoost Model for SMS-Based Mobile Money Fraud Detection in Ghana**

An undergraduate ML research project (CSM 376, KNUST) that engineers a custom focal-loss variant of XGBoost to detect fraudulent mobile money (MoMo) SMS messages targeting individuals in Ghana.

## Overview

Mobile money fraud costs Ghanaians hundreds of millions of cedis each year, largely through deceptive SMS messages that mimic legitimate MTN MoMo notifications. This project trains a machine learning model to classify incoming SMS as **scam** or **legitimate** based on their text content.

The core contribution is **O-XGBoost** — a variant of XGBoost with a fabricated focal-loss objective function that improves detection of the minority (scam) class under class imbalance.

## Research Questions

- **RQ1:** Does O-XGBoost achieve a statistically significant improvement in AUC-PR over standard XGBoost?
- **RQ2:** How does O-XGBoost compare to Random Forest and Logistic Regression baselines?
- **RQ3:** Which textual features are most discriminative of Ghanaian MoMo scam SMS (via SHAP)?

## Method

- **Model:** XGBoost with a custom focal-loss objective (O-XGBoost)
- **Baselines:** Standard XGBoost (log-loss), Random Forest, Logistic Regression
- **Features:** TF-IDF (unigrams + bigrams)
- **Data:** Hybrid — UCI SMS Spam Collection (public) + field-collected Ghanaian MoMo SMS (primary)
- **Evaluation:** Accuracy, Macro F1, AUC-ROC, AUC-PR; 5-fold stratified CV; Wilcoxon signed-rank test

## Repository Structure

```
FraudGuard-OXGBoost/
├── data/                  # Anonymised datasets (no raw screenshots, no PII)
├── notebooks/
│   ├── baseline.ipynb     # Standard XGBoost, RF, LR — locked control
│   ├── o_xgboost.ipynb    # O-XGBoost with focal loss
│   └── comparison.ipynb   # Formal baseline-vs-engineered comparison
├── models/                # Saved model artefacts (.pkl)
├── requirements.txt
└── README.md
```

## Ethics & Data Privacy

Field data was collected with approval from the KNUST Committee on Human Research, Publications and Ethics (CHRPE), College of Humanities and Social Sciences. All SMS data is anonymised — phone numbers, names, and transaction amounts are redacted before analysis. No raw screenshots are stored. This project complies with the Ghana Data Protection Act, 2012 (Act 843).

## Reproducibility

- Random seed fixed at `42` across all notebooks
- Library versions pinned in `requirements.txt`
- Identical data splits used for baseline and engineered model

## Author

**Jeffery Jojo Ocran** — Department of Computer Science, KNUST
Supervisor: Dr. Emmanuel Ahene

## License

MIT License
