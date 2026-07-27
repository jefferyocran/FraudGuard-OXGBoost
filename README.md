# FraudGuard: Detecting Ghanaian Mobile Money Fraud SMS

**Do Western-Trained SMS Fraud Detectors Protect Ghanaian Mobile Money Users? A Gap Analysis and the Case for Local Data**

An undergraduate ML research project (CSM 376, KNUST) investigating whether SMS fraud-detection models generalise across regions, how much locally-collected Ghanaian data improves detection of mobile money (MoMo) scams, and how decision-threshold choice affects real-world performance.

## Research Questions

- **RQ1 — The transfer gap:** How well does a model trained only on Western SMS data detect Ghanaian MoMo scams?
- **RQ2 — The local-data effect:** Does adding locally-collected field data improve detection of Ghanaian scams?
- **RQ3 — The engineering question:** Does a focal-loss-engineered XGBoost variant (O-XGBoost) improve detection over the standard model?

## Key Findings

| # | Finding | Result |
|---|---|---|
| 1 | Western-trained model on Ghanaian scams | 23.5% recall; 28 of 67 legitimate messages wrongly flagged |
| 2 | After adding local data | Recall to 29.4%; false positives cut from 28 to 4 (7x fewer) |
| 3 | O-XGBoost vs standard XGBoost | Inconclusive at current scale — baseline unstable under imbalance |
| 4 | Decision-threshold tuning | Recall rises from 35.3% (default) to 88.2% at a lower threshold, no new data |

**Headline:** A fraud detector trained only on foreign data misses most Ghanaian MoMo scams and over-flags genuine messages. Adding local data improves detection and dramatically reduces false alarms. Performance is driven by local data and threshold choice, not model architecture alone.

## Method

- **Features:** TF-IDF (unigrams + bigrams, max 1000 features)
- **Models:** Logistic Regression, Random Forest, standard XGBoost, and O-XGBoost (custom focal-loss objective, γ=2.0, α=0.25)
- **Imbalance handling:** cost-sensitive weighting (scale_pos_weight = legitimate/scam ratio); decision-threshold analysis
- **Data:** Hybrid — UCI SMS Spam Collection (5,574 messages, public) + field-collected Ghanaian MoMo SMS (208 messages, primary; 42 scam / 166 legitimate)
- **Evaluation:** Scam recall and precision on a held-out Ghanaian test set; fixed random seed (42)

## Files in This Repository

| File | Description |
|---|---|
| `baseline.ipynb` | Baseline models (Logistic Regression, Random Forest, standard XGBoost) |
| `o_xgboost.ipynb` | O-XGBoost focal-loss variant |
| `experiment2.ipynb` | Local-data effect (RQ2) — headline result |
| `experiment3.ipynb` | Engineering comparison (RQ3) + threshold analysis |
| `ghana_momo_field_v6.csv` | Current anonymised Ghanaian MoMo SMS dataset (208 messages, leakage-controlled) |
| `requirements.txt` | Python dependencies |
| `README.md` | This file |

Earlier dataset versions (v3–v5) were intermediate collection stages; v6 is the current, leakage-controlled dataset used for the reported results.

## Dataset Notes

The Ghanaian field dataset was collected under **KNUST CHRPE ethics approval** and complies with the **Ghana Data Protection Act, 2012 (Act 843)**. All messages are anonymised — phone numbers, transaction IDs, and links are redacted (`<PHONE>`, `<TXID>`, `<URL>`). Personal names were removed entirely to prevent label leakage. Messages are otherwise preserved verbatim, including original spelling and formatting, as these are characteristic features of the fraud class. No raw screenshots are stored.

The natural class imbalance (about 1 scam to 4 legitimate) reflects the real-world condition, in which fraudulent messages are infrequent relative to genuine ones.

## Reproducibility

- Fixed random seed: `42`
- Data splits and preprocessing documented in each notebook
- Run in Google Colab (CPU is sufficient; XGBoost trains in under a minute)

## Author

**Jeffery Jojo Ocran** — Department of Computer Science, KNUST
Supervisor: Dr. Emmanuel Ahene

## Status

Active research. Current priority: expanding the scam sample to lift recall and enable a conclusive engineering comparison (RQ3).

## License

MIT License
