import joblib
import pandas as pd

print("predict.py loaded")

model = joblib.load("models/fraud_pipeline.pkl")

FEATURE_ORDER = [
"Time","V1","V2","V3","V4","V5","V6","V7","V8","V9","V10",
"V11","V12","V13","V14","V15","V16","V17","V18","V19",
"V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"
]

def predict_transaction(input_dict):

    if model is None:
        raise Exception("Model not loaded")

    data = pd.DataFrame([input_dict])

    # add missing columns automatically
    for col in FEATURE_ORDER:
        if col not in data.columns:
            data[col] = 0

    # reorder columns
    data = data[FEATURE_ORDER]

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return prediction, probability