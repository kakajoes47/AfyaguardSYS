import pandas as pd
import os
import streamlit as st

def load_zeek_logs(file_path="data/zeek_conn_log.csv", sample_size=8000):
    try:
        if os.path.exists(file_path):
            df = pd.read_csv(file_path, low_memory=False)
            rename_dict = {'orig_h': 'id.orig_h', 'resp_h': 'id.resp_h'}
            df = df.rename(columns=rename_dict)
            
            cols = ['id.orig_h', 'id.resp_h', 'service', 'duration', 'orig_bytes', 'resp_bytes']
            available = [c for c in cols if c in df.columns]
            df = df[available].copy()
            
            for col in ['duration', 'orig_bytes', 'resp_bytes']:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            
            if len(df) > sample_size:
                df = df.sample(sample_size, random_state=42)
            return df.reset_index(drop=True)
    except Exception:
        st.warning("Using demo dataset.")

    # Demo Data
    return pd.DataFrame({
        "id.orig_h": ["192.168.1.10", "8.8.8.8", "185.143.223.12", "10.0.0.45", "172.16.5.20", "45.77.12.89"],
        "id.resp_h": ["192.168.1.1", "192.168.1.20", "192.168.1.30", "192.168.1.50", "192.168.1.100", "192.168.1.200"],
        "service": ["http", "dns", "ssh", "http", "rdp", "ftp"],
        "duration": [25, 0.4, 620, 180, 45, 1200],
        "orig_bytes": [2500, 120, 2500000, 890000, 4500, 3200000],
        "resp_bytes": [12000, 450, 1800, 560000, 32000, 1500]
    })
