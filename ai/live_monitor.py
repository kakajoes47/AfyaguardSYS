import time
from fetch_logs import fetch_logs
from detector import detect_batch
import requests

def send_alert(log):
    try:
        requests.post("http://localhost:5678/webhook/alert", json=log)
    except:
        pass

def monitor():
    print("AI monitoring started...")

    while True:
        logs = fetch_logs()
        results = detect_batch(logs)

        for r in results:
            if r["result"] == "Anomaly 🚨":
                print("🚨 Threat detected:", r["log"])
                send_alert(r["log"])

        time.sleep(10)

if __name__ == "__main__":
    monitor()
