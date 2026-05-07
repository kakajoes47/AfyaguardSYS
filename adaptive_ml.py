def predict_threat(row):
    try:
        service = str(row.get("service", "")).lower()
        duration = float(row.get("duration", 0))
        orig_bytes = float(row.get("orig_bytes", 0))

        if "dns" in service and duration < 1:
            return "Reconnaissance"
        elif orig_bytes == 0:
            return "Port Scan"
        elif duration > 300:
            return "Suspicious Persistence"
        elif orig_bytes > 1000000:
            return "Possible Data Exfiltration"
        elif "ssh" in service and duration > 120:
            return "Credential Attack"
        else:
            return "Normal"
    except:
        return "Normal"
