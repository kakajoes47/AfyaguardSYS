# zeek_reader.py

import pandas as pd
import os


def load_zeek_logs():
    """
    Loads Zeek connection logs from:
    zeek/logs/conn.log

    If logs are missing or unreadable,
    returns an empty DataFrame safely.
    """

    file_path = "zeek/logs/conn.log"

    # Check if file exists
    if not os.path.exists(file_path):
        return pd.DataFrame()

    try:
        # Zeek logs are tab-separated
        df = pd.read_csv(
            file_path,
            sep="\t",
            comment="#",
            low_memory=False
        )

        # Ensure required columns exist
        required_columns = [
            "id.orig_h",
            "id.resp_h",
            "service",
            "duration",
            "orig_bytes",
            "resp_bytes"
        ]

        for col in required_columns:
            if col not in df.columns:
                df[col] = ""

        return df

    except Exception:
        return pd.DataFrame()
