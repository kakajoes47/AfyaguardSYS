# identity.py

def identify_device(ip):
    """
    Device Identity Monitoring Engine

    Identifies the likely device type
    based on IP address ranges
    inside the hospital network.
    """

    ip = str(ip)

    # -----------------------------------
    # Internal Hospital Devices
    # -----------------------------------
    if ip.startswith("192.168"):
        return "Internal Hospital Device"

    # -----------------------------------
    # Medical Equipment
    # -----------------------------------
    elif ip.startswith("10."):
        return "Medical Equipment"

    # -----------------------------------
    # Administrative Systems
    # -----------------------------------
    elif ip.startswith("172."):
        return "Administrative System"

    # -----------------------------------
    # External Unknown Devices
    # -----------------------------------
    else:
        return "External Unknown Device"
