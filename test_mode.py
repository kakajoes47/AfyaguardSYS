import pandas as pd
import numpy as np

def generate():
    df = pd.DataFrame({
        "ts": pd.date_range("2026-04-12", periods=50, freq="min"),
        "src_ip": np.random.choice([
            "192.168.1.50",
            "192.168.1.60",
            "192.168.1.70",
            "8.8.8.8",
            "185.143.223.12"
        ], 50),
        "dest_ip": np.random.choice([
            "192.168.1.10",
            "192.168.1.20",
            "192.168.1.30"
        ], 50),
        "bytes": np.random.randint(1000, 500000, 50),
        "packets": np.random.randint(10, 2000, 50)
    })

    return df
