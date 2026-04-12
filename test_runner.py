import pandas as pd
from adaptive_ml import train, detect
from identity import enrich

def run(file):
    print(f"\nTesting {file}")

    df = pd.read_csv(file)

    train(df)
    df = detect(df)

    identity = df["src_ip"].apply(enrich).apply(pd.Series)
    df = pd.concat([df, identity], axis=1)

    anomalies = (df["anomaly"]=="Anomaly").sum()

    print("Anomalies:", anomalies)

    if "normal" in file:
        assert anomalies == 0
        print("PASS: Normal OK")

    else:
        assert anomalies > 0
        print("PASS: Attack detected")

run("test_data/normal.csv")
run("test_data/scan_attack.csv")
run("test_data/ddos_attack.csv")

print("\nALL TESTS PASSED")
