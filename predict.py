"""
predict.py - Ghanaian MoMo SMS fraud detector (O-XGBoost)

Usage:
    from predict import check_sms
    print(check_sms("Your MoMo wallet is blocked. Send your PIN."))

Requires: o_xgboost_model.pkl (produced by save_model.ipynb) in the same folder.
"""
import pickle
import numpy as np
import xgboost as xgb

_DETECTOR = None

def _load(path="o_xgboost_model.pkl"):
    global _DETECTOR
    if _DETECTOR is None:
        with open(path, "rb") as f:
            _DETECTOR = pickle.load(f)
    return _DETECTOR

def check_sms(text, path="o_xgboost_model.pkl"):
    """Classify a single SMS message as SCAM or LIKELY LEGITIMATE."""
    det = _load(path)
    feats = det["vectorizer"].transform([text])
    d = xgb.DMatrix(feats)
    prob = 1.0 / (1.0 + np.exp(-det["model"].predict(d)[0]))
    is_scam = prob >= det["threshold"]
    return {
        "verdict": "SCAM" if is_scam else "LIKELY LEGITIMATE",
        "scam_probability": round(float(prob) * 100, 1),
    }

if __name__ == "__main__":
    samples = [
        "Your MoMo wallet is blocked. Send your PIN now to unlock it.",
        "Cash In received for GHS 500.00 from KWAME. Balance GHS 500.00.",
        "Congratulations! You won GHS 5000. Pay GHS 50 to claim.",
    ]
    for s in samples:
        r = check_sms(s)
        print(f"{r['verdict']:20s} ({r['scam_probability']}%)  {s[:50]}")
