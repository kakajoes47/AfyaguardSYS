import pandas as pd
import os
import streamlit as st
import glob

def load_zeek_logs(sample_size=8000):
    """Smart loader - works with one conn file"""
    data_folder = "data"
    
    try:
        # Find any conn-related file
        if os.path.exists(data_folder):
            conn_files = glob.glob(f"{data_folder}/*conn*.csv") + glob.glob(f"{data_folder}/*.csv")
            if conn_files:
                file_path = conn_files[0]
                st.success(f"✅ Loaded dataset: {os.path.basename(file_path)}")
                df = pd.read_csv(file_path, low_memory=False)
            else:
                raise FileNotFoundError
        else:
            raise FileNotFoundError

        # Standardize columns
        rename_dict = {'orig_h': 'id.orig_h', 'resp_h': 'id.resp_h'}
        df = df.rename(columns=rename_dict)

        # Keep relevant columns
        cols = ['id.orig_h', 'id.resp_h', 'service', 'duration', 'orig_bytes', 'resp_bytes']
        available_cols = [col for col in cols if col in df.columns]
        df = df[available_cols].copy()

        # Fix data types
        for col in ['duration', 'orig_bytes', 'resp_bytes']:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

        # Limit rows for smooth dashboard
        if len(df) > sample_size:
            df = df.sample(sample_size, random_state=42)

        return df.reset_index(drop=True)

    except Exception:
        st.info("📊 Using built-in demo data (no real file found)")

    # Fallback demo data
    return pd.DataFrame({
        "id.orig_h": ["192.168.1.10", "8.8.8.8", "185.143.223.12", "10.0.0.45", "172.16.5.20", "45.77.12.89"],
        "id.resp_h": ["192.168.1.1", "192.168.1.20", "192.168.1.30", "192.168.1.50", "192.168.1.100", "192.168.1.200"],
        "service": ["http", "dns", "ssh", "http", "rdp", "ftp"],
        "duration": [25, 0.4, 620, 180, 45, 1200],
        "orig_bytes": [2500, 120, 2500000, 890000, 4500, 3200000],
        "resp_bytes": [12000, 450, 1800, 560000, 32000, 1500]
    })
