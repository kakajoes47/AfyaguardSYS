from sklearn.ensemble import IsolationForest

def run_ai_detection(df):
    if "packets" not in df.columns or "bytes" not in df.columns:
        df["anomaly"]=1
        df["severity"]="LOW"
        return df

    X=df[["packets","bytes"]]

    model=IsolationForest(contamination=0.05,random_state=42)
    model.fit(X)

    df["anomaly"]=model.predict(X)

    mean=df["packets"].mean()
    df["severity"]=df["packets"].apply(
        lambda x:"HIGH" if x>mean*3 else
        "MEDIUM" if x>mean*2 else "LOW"
    )

    return df
