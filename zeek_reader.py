import pandas as pd

def read_logs():
    try:
        df = pd.read_csv(
            "/opt/zeek/logs/current/conn.log",
            sep="\t",
            comment="#"
        )

        df = df.rename(columns={
            "id.orig_h": "src_ip",
            "id.resp_h": "dest_ip",
            "orig_bytes": "bytes"
        })

        df["packets"] = df["bytes"].fillna(0)
        return df

    except:
        return pd.DataFrame()
