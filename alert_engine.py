# alert_engine.py

def create_alert(ip, threat_type):
    """
    Security Alert Engine

    Generates readable threat alerts for:
    - Kibana dashboards
    - Admin response
    - n8n workflows
    - Email / SMS escalation later

    This is the base alert logic for
    healthcare threat response.
    """

    ip = str(ip)
    threat_type = str(threat_type)

    if threat_type == "Normal":
        return "No Active Alert"

    return (
        f"ALERT: {threat_type} detected "
        f"from source IP {ip}. "
        f"Immediate investigation recommended."
    )
