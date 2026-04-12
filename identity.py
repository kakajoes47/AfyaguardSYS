device_map = {
    "192.168.1.50": {"user":"Nurse Mary","device":"Ward PC","department":"Ward"},
    "192.168.1.60": {"user":"Dr John","device":"Doctor Laptop","department":"Consultation"},
    "192.168.1.70": {"user":"Admin Jane","device":"Admin Terminal","department":"Admin"}
}

def enrich(ip):
    return device_map.get(ip, {
        "user":"Unknown",
        "device":"External Device",
        "department":"External"
    })
