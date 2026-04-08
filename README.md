# AfyaGuard 🤖🛡️

AI-powered cybersecurity system with Zeek + Suricata.

## Stack
- Zeek (Network monitoring)
- Suricata (IDS)
- Elasticsearch + Kibana (SIEM)
- n8n (Automation)
- AI anomaly detection
- Streamlit dashboard

## Run

```bash
git clone https://github.com/kakajoes47/AfyaguardSYS.git
cd afyaguard
sudo docker compose up -d
pip install -r requirements.txt
python ai/train.py
python ai/live_monitor.py
streamlit run app.py
