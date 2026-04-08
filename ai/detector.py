import joblib
import pandas as pd

model = joblib.load("ai/ai_model.pkl")

def detect_batch(logs):
    df = pd.json_normalize(logs)
    df = df.select_dtypes(include=['number']).fillna(0)

    if df.empty:
        return []

    predictions = model.predict(df)

    results = []
    for i, pred in enumerate(predictions):
        results.append({
            "log": logs[i],
            "result": "Anomaly 🚨" if pred == -1 else "Normal ✅"
        })

    return results
