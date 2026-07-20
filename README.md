# FraudGuard: Detecting Ghanaian Mobile Money Fraud SMS

**Do Western-Trained SMS Fraud Detectors Protect Ghanaian Mobile Money Users? A Gap Analysis and the Case for Local Data**

A ML research project investigating whether SMS fraud-detection models generalise across regions, and how much locally-collected Ghanaian data improves detection of mobile money (MoMo) scams.

## Research Questions

- **RQ1 — The transfer gap:** How well does a model trained only on Western SMS data detect Ghanaian MoMo scams?
- **RQ2 — The local-data effect:** Does adding locally-collected field data improve detection of Ghanaian scams?
- **RQ3 — The engineering question:** Does a focal-loss-engineered XGBoost variant (O-XGBoost) improve detection over the standard model, and under what conditions?

## Key Findings (preliminary)

|Finding                                |Result                                                    |
|---------------------------------------|----------------------------------------------------------|
|Western-trained model on Ghanaian scams|**29.4%** scam recall (caught 5 of 17)                    |
|After adding weighted local data       |**52.9%** scam recall (caught 9 of 17), **+23.5 pp**      |
|O-XGBoost vs standard XGBoost          |Inconclusive at current data scale — needs more field data|

**Headline:** A fraud detector trained only on foreign data misses roughly 7 in 10 Ghanaian MoMo scams. Adding locally-collected data nearly doubles detection. The main determinant of performance is the presence of local data, not model choice alone.

## Method

- **Features:** TF-IDF (unigrams + bigrams, max 1000 features)
- **Models:** Logistic Regression, Random Forest, standard XGBoost, and O-XGBoost (custom focal-loss objective, γ=2.0, α=0.25)
- **Data:** Hybrid — UCI SMS Spam Collection (5,574 messages, public) + field-collected Ghanaian MoMo SMS (67 messages, primary)
- **Evaluation:** Scam recall on a held-out Ghanaian test set; fixed random seed (42)

## Files in This Repository

|File                     |Description                                                           |
|-------------------------|----------------------------------------------------------------------|
|`baseline.ipynb`         |Baseline models (Logistic Regression, Random Forest, standard XGBoost)|
|`o_xgboost.ipynb`        |O-XGBoost focal-loss variant                                          |
|`experiment2.ipynb`      |Local-data effect — the headline result (RQ2)                         |
|`experiment3.ipynb`      |Engineering comparison — preliminary (RQ3)                            |
|`ghana_momo_field_v3.csv`|Current anonymised Ghanaian MoMo SMS dataset (67 messages)            |
|`ghana_momo_sms.csv`     |Earlier field dataset (30 messages) — superseded by v3                |
|`requirements.txt`       |Python dependencies                                                   |
|`README.md`              |This file                                                             |

## Dataset Notes

The Ghanaian field dataset was collected under **KNUST CHRPE ethics approval** and complies with the **Ghana Data Protection Act, 2012 (Act 843)**. All messages are anonymised — phone numbers, names, transaction IDs, and links are redacted (`<PHONE>`, `<TXID>`, `<URL>`). Messages are otherwise preserved verbatim, including original spelling and formatting, as these are characteristic features of the fraud class. No raw screenshots are stored.

## Reproducibility

- Fixed random seed: `42`
- Data splits and preprocessing documented in each notebook
- Run in Google Colab (CPU is sufficient; XGBoost trains in under a minute)

## Author

**Jeffery Jojo Ocran** — Department of Computer Science, KNUST
Supervisor: Dr. Emmanuel Ahene

## Status

Active research. Current priority: expanding the field dataset to strengthen RQ2 and enable a conclusive RQ3 evaluation.

## License

MIT License
