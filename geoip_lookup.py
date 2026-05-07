def get_location(ip):
    ip = str(ip)
    locations = {
        "8.8.8.8": "United States",
        "185.143.223.12": "Russia",
        "45.77.12.89": "Germany",
        "192.168.1.10": "Internal Hospital Network",
        "10.0.0.45": "Internal Hospital Network",
        "172.16.5.20": "Internal Hospital Network"
    }
    return locations.get(ip, "Unknown Location")
