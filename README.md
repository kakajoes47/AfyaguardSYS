# README.md

# 🛡️ AfyaGuard Enterprise Healthcare SOC

## Adaptive AI-Driven Cybersecurity Threat Hunting System for Healthcare Networks

A premium enterprise-grade Security Operations Center (SOC) platform built for healthcare environments to detect, classify, monitor, and respond to cybersecurity threats using AI-driven threat hunting, Zeek network monitoring, Kibana SIEM visualization, Elasticsearch logging, and automated security workflows.

---

# 🚀 Core Features

## 🧠 Adaptive AI Threat Detection

Automatically detects and classifies:

- Port Scans
- Reconnaissance Attacks
- Credential Attacks
- Suspicious Persistence
- Possible Data Exfiltration
- Internal vs External Threats

---

## 🌍 Global Attack Intelligence Map

Tracks:

- Source IP origin
- Global attacker locations
- Suspicious external traffic
- Attack source visibility

Supports hospital cyber defense investigations.

---

## 👤 Device Identity Monitoring

Identifies:

- Internal hospital devices
- Medical equipment
- Administrative systems
- External unknown devices

Helps isolate attacked hospital assets.

---

## 🚫 Admin IP Blocking

Allows administrators to:

- Identify malicious IPs
- Block suspicious attacker sources
- Simulate incident response workflows

---

## 📊 Premium Executive Dashboard

Includes:

- SOC overview
- Threat dashboards
- Traffic monitoring
- Security alerts
- Attack source intelligence
- Executive-grade cyber defense visualization

---

## 📦 SIEM Stack

Integrated with:

- Zeek
- Filebeat
- Elasticsearch
- Kibana
- n8n automation workflows

Enterprise-grade architecture.

---

# 📁 Project Structure

```text
AfyaguardSYS/
│
├── app.py
├── adaptive_ml.py
├── zeek_reader.py
├── identity.py
├── firewall.py
├── geoip_lookup.py
├── alert_engine.py
├── test_runner.py
├── style.css
├── requirements.txt
├── docker-compose.yml
├── README.md
│
├── filebeat/
│   └── filebeat.yml
│
├── zeek/
│   └── logs/
│
├── suricata/
│   └── logs/
│
└── models/
