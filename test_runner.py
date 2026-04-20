# test_runner.py

from adaptive_ml import predict_threat
from identity import identify_device
from geoip_lookup import get_location
from alert_engine import create_alert


def run_system_validation():
    """
    Final validation tests for
    AfyaGuard Enterprise Healthcare SOC
    """

    sample_logs = [
        {
            "service": "dns",
            "duration": 0.2,
            "orig_bytes": 0,
            "resp_bytes": 0,
            "ip": "8.8.8.8"
        },
        {
            "service": "http",
            "duration": 20,
            "orig_bytes": 5000,
            "resp_bytes": 10000,
            "ip": "192.168.1.10"
        },
        {
            "service": "ssh",
            "duration": 600,
            "orig_bytes": 1500000,
            "resp_bytes": 2000,
            "ip": "185.143.223.12"
        }
    ]

    print("\n==============================")
    print("AFYAGUARD SYSTEM VALIDATION")
    print("==============================\n")

    for i, log in enumerate(sample_logs, start=1):
        prediction = predict_threat(log)
        device = identify_device(log["ip"])
        location = get_location(log["ip"])
        alert = create_alert(log["ip"], prediction)

        print(f"Test Case {i}")
        print(f"IP Address     : {log['ip']}")
        print(f"Threat Type    : {prediction}")
        print(f"Device Type    : {device}")
        print(f"Location       : {location}")
        print(f"Generated Alert: {alert}")
        print("-" * 40)

    print("\nSystem validation complete.")
    print("Project ready for lecturer demo.\n")


if __name__ == "__main__":
    run_system_validation()
