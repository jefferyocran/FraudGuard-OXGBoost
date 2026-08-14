# FraudGuard: Detecting Ghanaian Mobile Money Fraud SMS

**Do Western-Trained SMS Fraud Detectors Protect Ghanaian Mobile Money Users? A Gap Analysis and the Case for Local Data**

An ML research project investigating whether SMS fraud-detection models generalise across regions, how much locally-collected Ghanaian data improves detection of mobile money (MoMo) scams, and how model tuning and decision-threshold choice affect real-world performance.

## Research Questions

- **RQ1 — The transfer gap:** How well does a model trained only on Western SMS data detect Ghanaian MoMo scams?
- **RQ2 — The local-data effect:** Does adding locally-collected field data improve detection of Ghanaian scams?
- **RQ3 — The engineering question:** Does a focal-loss-engineered XGBoost variant (O-XGBoost) improve detection over the standard model, and under what conditions?

## Key Findings

| # | Finding | Result |
|---|---|---|
| 1 | Western-trained model on Ghanaian scams | 23.5% recall; 28 of 67 legitimate messages wrongly flagged |
| 2 | After adding local data | Recall to 29.4%; false positives cut from 28 to 4 (7x fewer) |
| 3 | O-XGBoost with tuned focal loss (γ=5) | Scam recall rises to 94.1% (16 of 17), at the cost of lower precision |
| 4 | Decision-threshold tuning | Recall rises from 35.3% (default) to 88.2% at a lower threshold, no new data |

**Headline:** A fraud detector trained only on foreign data misses most Ghanaian MoMo scams and over-flags genuine messages. Adding local data improves detection and dramatically reduces false alarms. Once the focal-loss parameter and decision threshold are tuned, scam recall rises substantially. Performance is driven by local data and operating-point choice, not model architecture alone.

## Method

- **Features:** TF-IDF (unigrams + bigrams, max 1000 features)
- **Models:** Logistic Regression, Random Forest, standard XGBoost, and O-XGBoost (custom focal-loss objective)
- **Imbalance handling:** cost-sensitive weighting; focal-loss focusing parameter (γ) tuning; decision-threshold analysis
- **Data:** Hybrid — UCI SMS Spam Collection (5,574 messages, public) + field-collected Ghanaian MoMo SMS (208 messages, primary; 42 scam / 166 legitimate)
- **Evaluation:** Scam recall and precision on a held-out Ghanaian test set; fixed random seed (42)

## Files in This Repository

| File | Description |
|---|---|
| `baseline.ipynb` | Baseline models (Logistic Regression, Random Forest, standard XGBoost) |
| `experiment2.ipynb` | Local-data effect (RQ2) |
| `experiment3.ipynb` | Engineering comparison + focal-loss γ tuning (RQ3) |
| `experiment4.ipynb` | Decision-threshold analysis |
| `save_model.ipynb` | Trains and saves the deployable O-XGBoost model (γ=5) |
| `predict.py` | Loads the saved model and classifies a single SMS message |
| `o_xgboost_model.pkl` | Trained model + TF-IDF vectorizer, ready for use |
| `ghana_momo_field.csv` | Anonymised Ghanaian MoMo SMS dataset (208 messages, leakage-controlled) |
| `requirements.txt` | Python dependencies |
| `README.md` | This file |

## Using the Model

A trained O-XGBoost model is provided as `o_xgboost_model.pkl` (built by `save_model.ipynb`). It bundles the classifier and its TF-IDF vectorizer together, so no separate preprocessing is needed.

```python
from predict import check_sms

print(check_sms("Your MoMo wallet is blocked. Send your PIN now to unlock it."))
# {'verdict': 'SCAM', 'scam_probability': ...}

print(check_sms("Cash In received for GHS 500.00 from KWAME. Balance GHS 500.00."))
# {'verdict': 'LIKELY LEGITIMATE', 'scam_probability': ...}
```

The model uses a focal-loss objective (γ=5) and a decision threshold of 0.30, an operating point chosen to prioritise catching scams. It favours recall over precision: it catches most scams but will occasionally flag a legitimate message. This is the safer error type for fraud protection. To make the model more conservative, raise the threshold or retrain at a lower γ. This is a research prototype, not a production fraud-prevention system.

## Dataset Notes

All messages are anonymised — phone numbers, transaction IDs, and links are redacted (`<PHONE>`, `<TXID>`, `<URL>`). Personal names were removed entirely to prevent label leakage. Messages are otherwise preserved verbatim, including original spelling and formatting, as these are characteristic features of the fraud class. No raw screenshots are stored.

The natural class imbalance (about 1 scam to 4 legitimate) reflects the real-world condition, in which fraudulent messages are infrequent relative to genuine ones.

## Reproducibility

- Fixed random seed: `42`
- Data splits and preprocessing documented in each notebook
- Run in Google Colab (CPU is sufficient; XGBoost trains in under a minute)

## Author

**Jeffery Jojo Ocran** — Department of Computer Science, KNUST
Supervisor: Dr. Emmanuel Ahene

## Status

Active research. Current priority: expanding the scam sample to further lift recall and firm up the engineering comparison (RQ3).

## License

MIT License
