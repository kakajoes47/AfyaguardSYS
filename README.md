🛡️ AfyaGuard AI Cyberpunk SOC Dashboard

AfyaGuard AI is a next-generation cybersecurity monitoring system that combines
AI-powered anomaly detection, IDS logs, and real-time visualization into a single
beautiful cyberpunk-style dashboard.

---

🚀 Features

🧠 AI Detection

- Isolation Forest anomaly detection
- Behavioral traffic analysis
- Automatic severity classification (LOW / MEDIUM / HIGH)

🛑 Threat Monitoring

- Integration with Zeek (network monitoring)
- Integration with Suricata (IDS alerts)
- Real-time attack classification:
  - Scan
  - DoS
  - Brute Force
  - Malware

📊 Dashboard (Streamlit)

- Cyberpunk UI design
- Live metrics (logs, packets, bytes)
- Traffic visualization
- Threat detection panel
- Attack distribution charts
- Log explorer

🚨 Alerts

- SMS alerts via Africa's Talking
- Real-time notifications on detected threats

🔐 Security

- Login system:
  - Username: "afyaguard"
  - Password: "afya2026"
- Environment-based secret management (no keys in code)

---

🏗️ System Architecture

Zeek / Suricata
        ↓
     Filebeat
        ↓
Elasticsearch
        ↓
 AfyaGuard AI (Streamlit + AI)
        ↓
   SMS Alerts (Africa's Talking)

---

📁 Project Structure

AfyaguardSYS/
│
├── ai/                # Existing AI or scripts
├── data/              # Data files
├── filebeat/          # Log shipping config
├── docker-compose.yml # Infrastructure setup
│
├── utils/             # Core system logic
│   ├── elastic.py     # Elasticsearch connection
│   ├── ai_model.py    # AI anomaly detection
│   ├── detection.py   # Threat detection logic
│   ├── classifier.py  # Attack classification
│   ├── alerts.py      # SMS alerts
│
├── app.py             # Main dashboard
├── requirements.txt   # Python dependencies
├── README.md          # Documentation

---

⚙️ Installation

1. Clone Repository

git clone https://github.com/your-username/afyaguard-ai.git
cd afyaguard-ai

---

2. Install Dependencies

pip install -r requirements.txt

---

3. Configure Environment Variables

⚠️ Do NOT hardcode credentials

export AT_USERNAME=your_username
export AT_API_KEY=your_api_key
export AT_PHONE=+2547XXXXXXXX

---

4. Start Elasticsearch Stack

Make sure your pipeline is running:

- Zeek ✅
- Suricata ✅
- Filebeat ✅
- Elasticsearch ✅

---

5. Run Dashboard

streamlit run app.py

---

🔑 Login Access

Username: afyaguard
Password: afya2026

---

📊 Dashboard Sections

Section| Description
Overview| System metrics
Traffic| Network traffic visualization
Threats| AI + IDS detected threats
Attack Map| Attack distribution
Logs| Raw log viewer

---

🚨 Alerts System

When threats are detected:

- SMS is sent via Africa's Talking
- Message example:

🚨 AfyaGuard ALERT: 5 threats detected

---

🔐 Security Best Practices

- Use environment variables for API keys
- Rotate API keys regularly
- Never commit secrets to GitHub
- Use firewall rules for Elasticsearch

---

🧪 Troubleshooting

❌ Dashboard is empty

- Check Elasticsearch:

curl http://localhost:9200

- Check indices:

curl http://localhost:9200/_cat/indices?v

- Ensure logs exist:

suricata-*
zeek-*
filebeat-*

---

❌ SMS not sending

- Verify API key
- Check phone format (+254...)
- Ensure internet access

---

🌍 Future Improvements

- 🌐 GeoIP attack map
- 🤖 Advanced ML models
- 📩 Email alerts
- ☁️ Cloud deployment
- 🧑‍💻 Multi-user authentication

---

📜 License

© 2026 Joachim Kioko (@kakajoes)
All rights reserved.

---

💡 Inspiration

Built as a real-world SOC (Security Operations Center) simulation
combining open-source security tools and AI.

---

⚡ Final Note

AfyaGuard AI is not just a dashboard —
it is a foundation for a full cybersecurity platform.

---

🔥 Stay secure. Stay ahead.
