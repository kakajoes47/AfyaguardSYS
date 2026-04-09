def detect_anomalies(df):
    if "anomaly" not in df.columns:
        return df,0
    threats=df[df["anomaly"]==-1]
    return threats,len(threats)
