# adaptive_ml.py

def predict_threat(row):
    """
    Adaptive AI threat classification engine
    for Healthcare Cybersecurity Threat Hunting
    """

    try:
        service = str(row.get("service", "")).lower()
        duration = float(row.get("duration", 0))
        orig_bytes = float(row.get("orig_bytes", 0))
        resp_bytes = float(row.get("resp_bytes", 0))

        # -----------------------------------
        # Reconnaissance Detection
        # -----------------------------------
        if "dns" in service and duration < 1:
            return "Reconnaissance"

        # -----------------------------------
        # Port Scan Detection
        # -----------------------------------
        elif orig_bytes == 0 and resp_bytes == 0:
            return "Port Scan"

        # -----------------------------------
        # Long Suspicious Sessions
        # -----------------------------------
        elif duration > 300:
            return "Suspicious Persistence"

        # -----------------------------------
        # Large Data Movement
        # -----------------------------------
        elif orig_bytes > 1000000:
            return "Possible Data Exfiltration"

        # -----------------------------------
        # SSH Brute Force Style Behavior
        # -----------------------------------
        elif "ssh" in service and duration > 120:
            return "Credential Attack"

        # -----------------------------------
        # Safe Traffic
        # -----------------------------------
        else:
            return "Normal"

    except Exception:
        return "Normal"
