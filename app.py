# app.py

import streamlit as st
import pandas as pd
from datetime import datetime

from adaptive_ml import predict_threat
from zeek_reader import load_zeek_logs
from identity import identify_device
from firewall import block_ip
from geoip_lookup import get_location
from alert_engine import create_alert

st.set_page_config(
    page_title="Afyaguard Enterprise SOC",
    page_icon="🛡️",
    layout="wide"
)

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.sidebar.title("🛡️ AfyaGuard")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Traffic",
        "Threats",
        "Attack Map",
        "Logs"
    ]
)

st.title("🏥 AfyaGuard Enterprise Healthcare SOC")

st.caption(
    "Adaptive AI-Driven Cybersecurity Threat Hunting System for Healthcare Networks"
)

df = load_zeek_logs()

if df.empty:
    df = pd.DataFrame({
        "id.orig_h": [
            "192.168.1.10",
            "8.8.8.8",
            "185.143.223.12"
        ],
        "id.resp_h": [
            "192.168.1.1",
            "192.168.1.20",
            "192.168.1.30"
        ],
        "service": [
            "http",
            "dns",
            "ssh"
        ],
        "duration": [
            20,
            0.3,
            500
        ],
        "orig_bytes": [
            2000,
            0,
            1500000
        ],
        "resp_bytes": [
            5000,
            0,
            2000
        ]
    })

df["prediction"] = df.apply(
    lambda row: predict_threat(row),
    axis=1
)

df["device_type"] = df["id.orig_h"].apply(
    identify_device
)

df["location"] = df["id.orig_h"].apply(
    get_location
)

df["alert"] = df.apply(
    lambda row: create_alert(
        row["id.orig_h"],
        row["prediction"]
    ) if row["prediction"] != "Normal"
    else "No Active Alert",
    axis=1
)

if page == "Overview":
    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Total Security Events",
        len(df)
    )

    c2.metric(
        "Threats Detected",
        len(df[df["prediction"] != "Normal"])
    )

    c3.metric(
        "Monitored Devices",
        df["id.orig_h"].nunique()
    )

    st.subheader("Recent Security Events")
    st.dataframe(df)

elif page == "Traffic":
    st.subheader("Traffic Monitoring")

    st.dataframe(df)

    st.subheader("Top Source IPs")
    st.bar_chart(
        df["id.orig_h"].value_counts()
    )

elif page == "Threats":
    st.subheader("Threat Hunting Engine")

    threats = df[
        df["prediction"] != "Normal"
    ]

    st.dataframe(threats)

    if not threats.empty:
        st.subheader("Active Security Alerts")

        st.dataframe(
            threats[
                [
                    "id.orig_h",
                    "prediction",
                    "location",
                    "alert"
                ]
            ]
        )

        selected_ip = st.selectbox(
            "Select suspicious IP to block",
            threats["id.orig_h"].unique()
        )

        if st.button("Block Selected IP"):
            result = block_ip(selected_ip)
            st.success(result)

elif page == "Attack Map":
    st.subheader("Global Attack Map")

    attack_map = pd.DataFrame({
        "lat": [
            -1.286389,
            40.7128,
            51.5074
        ],
        "lon": [
            36.817223,
            -74.0060,
            -0.1278
        ]
    })

    st.map(attack_map)

    st.subheader("Attack Source Intelligence")

    st.dataframe(
        df[
            [
                "id.orig_h",
                "location",
                "prediction"
            ]
        ]
    )

elif page == "Logs":
    st.subheader("Security Logs")

    st.dataframe(df)

    if st.button("Export Logs"):
        filename = f"alerts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index=False)

        st.success(
            f"Logs exported successfully: {filename}"
          )
