import streamlit as st
from ai.fetch_logs import fetch_logs
from ai.detector import detect_batch
import requests

st.title("AfyaGuard AI + Zeek Security Dashboard 🚨🤖")

try:
    res = requests.get("http://localhost:9200")
    if res.status_code == 200:
        st.success("Elasticsearch running ✅")
except:
    st.error("Elasticsearch not reachable ❌")

st.header("Live Threat Detection")

logs = fetch_logs(size=20)

if logs:
    results = detect_batch(logs)

    for r in results:
        st.write(r["result"], r["log"])
else:
    st.warning("No logs found")

st.write("Kibana → http://localhost:5601")
st.write("n8n → http://localhost:5678")
