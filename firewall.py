def create_alert(ip, threat_type):
    if threat_type == "Normal":
        return "No Active Alert"
    return f"🚨 ALERT: {threat_type} detected from {ip}. Immediate investigation recommended."
