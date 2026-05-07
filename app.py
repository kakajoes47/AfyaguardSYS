import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import warnings

warnings.filterwarnings("ignore")

# Import modules
from zeek_reader import load_zeek_logs
from adaptive_ml import predict_threat
from identity import identify_device
from geoip_lookup import get_location
from firewall import block_ip
from alert_engine import create_alert

# ====================== LOGIN SYSTEM ======================
def login_page():
    st.set_page_config(
        page_title="Afyaguard Enterprise SOC",
        page_icon="🛡️",
        layout="centered"
    )

    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("🔐 AfyaGuard Login")
        st.markdown("**Healthcare SOC Platform**")

        username = st.text_input("Username", placeholder="Enter username")
        password = st.text_input("Password", placeholder="Enter password", type="password")

        if st.button("Login", use_container_width=True, type="primary"):
            if username == "admin" and password == "admin123":
                st.session_state.logged_in = True
                st.session_state.role = "admin"
                st.success("Login successful as **Administrator**")
                st.rerun()
            elif username == "user" and password == "user123":
                st.session_state.logged_in = True
                st.session_state.role = "user"
                st.success("Login successful as **Viewer**")
                st.rerun()
            else:
                st.error("Invalid credentials")

        st.caption("Demo Credentials:\n\n**Admin**: `admin` / `admin123`\n**User**: `user` / `user123`")


# Check login status
if "logged_in" not in st.session_state:
    login_page()
    st.stop()

# ====================== MAIN APPLICATION ======================
st.set_page_config(
    page_title="Afyaguard Enterprise SOC",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🛡️ AfyaGuard")
st.sidebar.markdown(f"**Role:** {'🛡️ Administrator' if st.session_state.role == 'admin' else '👁️ Viewer'}")
st.sidebar.caption("Adaptive AI Healthcare SOC")

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Traffic", "Threats", "Attack Map", "Logs", "Dataset Explorer"]
)

if st.sidebar.button("Logout"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

st.title("🏥 AfyaGuard Enterprise Healthcare SOC")
st.markdown("**Adaptive AI-Driven Cybersecurity Threat Hunting System**")

# Load and Enrich Data
df = load_zeek_logs()

df["prediction"] = df.apply(lambda row: predict_threat(row), axis=1)
df["device_type"] = df["id.orig_h"].apply(identify_device)
df["location"] = df["id.orig_h"].apply(get_location)
df["alert"] = df.apply(
    lambda row: create_alert(row["id.orig_h"], row["prediction"]) 
    if row["prediction"] != "Normal" else "No Active Alert", axis=1
)

# ====================== PAGES ======================
if page == "Overview":
    st.header("📊 Command Center Overview")
    
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Events", f"{len(df):,}")
    c2.metric("Threats Detected", len(df[df["prediction"] != "Normal"]), "🔴")
    c3.metric("Monitored Devices", df["id.orig_h"].nunique())
    c4.metric("Active Locations", df["location"].nunique())

    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("Recent Security Events")
        display_cols = ["id.orig_h", "service", "duration", "prediction", "location", "device_type"]
        st.dataframe(df.head(15)[display_cols], use_container_width=True, hide_index=True)
    
    with col2:
        st.subheader("Threat Distribution")
        fig = px.pie(df, names="prediction", color="prediction",
                     color_discrete_map={
                         "Normal": "#22c55e", "Reconnaissance": "#eab308",
                         "Port Scan": "#f59e0b", "Credential Attack": "#ef4444",
                         "Possible Data Exfiltration": "#b91c1c"
                     })
        st.plotly_chart(fig, use_container_width=True)

elif page == "Traffic":
    st.header("🌐 Network Traffic Monitoring")
    st.dataframe(df, use_container_width=True)

elif page == "Threats":
    st.header("🎯 Threat Hunting Engine")
    threats = df[df["prediction"] != "Normal"].reset_index(drop=True)
    
    if not threats.empty:
        st.error(f"🚨 {len(threats)} Active Threats Detected")
        st.dataframe(threats, use_container_width=True)
        
        st.subheader("Active Security Alerts")
        st.dataframe(threats[["id.orig_h", "prediction", "location", "device_type", "alert"]], 
                    use_container_width=True)
        
        # Admin-only action
        if st.session_state.role == "admin":
            selected_ip = st.selectbox("Select Suspicious IP to Block", threats["id.orig_h"].unique())
            if st.button("🚫 Block IP on Firewall", type="primary"):
                result = block_ip(selected_ip)
                st.success(result)
        else:
            st.info("🔒 Blocking actions available only to Administrators")
    else:
        st.success("✅ No active threats detected.")

elif page == "Attack Map":
    st.header("🌍 Global Attack Map")
    map_data = pd.DataFrame({
        "lat": [-1.286389, 55.7558, 40.7128, 51.5074, 28.6139],
        "lon": [36.817223, 37.6173, -74.0060, -0.1278, 77.2090],
        "size": [80, 45, 65, 50, 30]
    })
    st.map(map_data, size="size")

elif page == "Logs":
    st.header("📜 Security Logs")
    st.dataframe(df, use_container_width=True)
    
    if st.session_state.role == "admin":
        if st.button("Export Logs as CSV"):
            filename = f"afyaguard_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            df.to_csv(filename, index=False)
            st.success(f"✅ Exported: {filename}")
    else:
        st.info("🔒 Export function available only to Administrators")

elif page == "Dataset Explorer":
    st.header("📁 Dataset Explorer")
    st.info("UWF-ZeekData22 — Real Zeek logs for healthcare threat analysis")
    st.dataframe(df, use_container_width=True)

st.caption("Afyaguard Enterprise SOC • Presentation Ready")
