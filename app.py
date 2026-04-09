import streamlit as st
import pandas as pd
import time

from utils.elastic import connect_elasticsearch, fetch_logs
from utils.ai_model import run_ai_detection
from utils.detection import detect_anomalies
from utils.classifier import apply_classification
from utils.alerts import send_alert

st.set_page_config(page_title="AfyaGuard AI", layout="wide")

# ================= CYBERPUNK STYLE =================
st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#020617,#0f172a);color:#e5e7eb;}
h1,h2,h3 {color:#00f5ff;text-shadow:0 0 10px #00f5ff;}
[data-testid="stMetric"] {
    background: rgba(255,0,255,0.05);
    border:1px solid #ff00ff;
    border-radius:10px;
    padding:10px;
    box-shadow:0 0 10px #ff00ff;
}
section[data-testid="stSidebar"] {
    background:#020617;
    border-right:2px solid #00f5ff;
}
section[data-testid="stSidebar"] * {color:#00f5ff;}
</style>
""", unsafe_allow_html=True)

# ================= LOGIN =================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("🔐 AfyaGuard Secure Access")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "afyaguard" and pwd == "afya2026":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials")

if not st.session_state.logged_in:
    login()
    st.stop()

# ================= SIDEBAR =================
st.sidebar.title("🛡️ AfyaGuard")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

page = st.sidebar.radio("Navigation",
    ["📊 Overview","📈 Traffic","🚨 Threats","🌍 Attack Map","🖥️ Logs"])

# ================= HEADER =================
st.title("🛡️ AfyaGuard AI — Cyber Threat Command Center")

# ================= DATA =================
es = connect_elasticsearch()
df = fetch_logs(es)

if df.empty:
    st.warning("⚠️ No logs found")
else:
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")

    df = run_ai_detection(df)
    df = apply_classification(df)

    if page == "📊 Overview":
        col1,col2,col3 = st.columns(3)
        col1.metric("Logs", len(df))

        if "packets" in df.columns:
            col2.metric("Packets", int(df["packets"].sum()))
        if "bytes" in df.columns:
            col3.metric("Bytes", int(df["bytes"].sum()))

    elif page == "📈 Traffic":
        if "timestamp" in df.columns and "packets" in df.columns:
            st.line_chart(df.set_index("timestamp")["packets"])

    elif page == "🚨 Threats":
        threats,count = detect_anomalies(df)

        if count>0:
            st.error(f"{count} threats detected")
            st.dataframe(threats)

            send_alert(f"🚨 AfyaGuard ALERT: {count} threats detected")

        if "alert.signature" in df.columns:
            alerts = df[df["alert.signature"].notna()]
            if len(alerts)>0:
                st.subheader("Suricata Alerts")
                st.dataframe(alerts[[
                    "src_ip","dest_ip",
                    "alert.signature","attack_type","severity"
                ]])

        if "attack_type" in df.columns:
            st.bar_chart(df["attack_type"].value_counts())

    elif page == "🌍 Attack Map":
        if "src_ip" in df.columns:
            st.bar_chart(df["src_ip"].value_counts().head(10))
        if "attack_type" in df.columns:
            st.bar_chart(df["attack_type"].value_counts())

    elif page == "🖥️ Logs":
        st.dataframe(df)

# ================= FOOTER =================
st.markdown("""
<hr>
<center style="color:#00f5ff;text-shadow:0 0 10px #00f5ff;">
© 2026 Joachim Kioko (@kakajoes) — AfyaGuard AI
</center>
""", unsafe_allow_html=True)

time.sleep(3)
st.rerun()
