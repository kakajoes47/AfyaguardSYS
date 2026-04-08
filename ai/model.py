from sklearn.ensemble import IsolationForest
import joblib

def train_model(data):
    model = IsolationForest(contamination=0.05)
    model.fit(data)
    joblib.dump(model, "ai/ai_model.pkl")
    return model
