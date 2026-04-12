from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
model = IsolationForest(contamination=0.08, random_state=42)

def train(df):
    X = df[["bytes","packets"]].fillna(0)
    X = scaler.fit_transform(X)
    model.fit(X)

def detect(df):
    X = df[["bytes","packets"]].fillna(0)
    X = scaler.transform(X)
    preds = model.predict(X)

    df["anomaly"] = ["Anomaly" if p==-1 else "Normal" for p in preds]
    return df
