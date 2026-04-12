import streamlit as st
import pandas as pd

from zeek_reader import read_logs
from adaptive_ml import train, detect
from identity import enrich
from firewall import block_ip, blocked_ips
from test_mode import generate

st.set_page_config(layout="wide")

# STYLE
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("🛡 AfyaGuard AI — Healthcare Cyber Defense")

# NAV
page = st.sidebar.radio("Navigation", [
    "Overview","Traffic","Threats","Identity Monitoring","Logs"
])

# LOAD DATA
df = read_logs()

# FALLBACK IF NO ZEEK
if df.empty:
    df = generate()
    st.warning("Running in demo mode (no Zeek data)")

# ML
train(df)
df = detect(df)

# IDENTITY
identity = df["src_ip"].apply(enrich).apply(pd.Series)
df = pd.concat([df, identity], axis=1)

# OVERVIEW
if page == "Overview":
    c1,c2,c3 = st.columns(3)
    c1.metric("Logs", len(df))
    c2.metric("Threats", (df["anomaly"]=="Anomaly").sum())
    c3.metric("Devices", df["device"].nunique())

# TRAFFIC
elif page == "Traffic":
    if "ts" in df.columns:
        df["ts"] = pd.to_datetime(df["ts"], errors="coerce")
        st.line_chart(df.groupby(df["ts"].dt.floor("min")).size())

# THREATS
elif page == "Threats":
    threats = df[df["anomaly"]=="Anomaly"]

    if not threats.empty:
        st.error(f"{len(threats)} threats detected")

        for i,row in threats.iterrows():
            st.markdown(f"""
            <div style="border-left:5px solid red;
            padding:10px;margin:5px;
            background:rgba(255,0,0,0.08);
            border-radius:10px;">
            👤 {row['user']} ({row['device']})<br>
            🏥 {row['department']}<br>
            🌐 {row['src_ip']} → {row['dest_ip']}
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Block {row['src_ip']}", key=i):
                block_ip(row["src_ip"])
                st.success(f"{row['src_ip']} blocked")

    else:
        st.success("No threats")

# IDENTITY
elif page == "Identity Monitoring":
    st.dataframe(df[[
        "user","device","department","src_ip","dest_ip","anomaly"
    ]])
    st.bar_chart(df["user"].value_counts())

# LOGS
elif page == "Logs":
    st.dataframe(df)

# FOOTER
st.markdown("---")
st.caption("AfyaGuard AI — Adaptive Healthcare Cyber Defense System")
