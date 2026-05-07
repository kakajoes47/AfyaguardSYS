def identify_device(ip):
    ip = str(ip)
    if ip.startswith("192.168"):
        return "Internal Hospital Device"
    elif ip.startswith("10."):
        return "Medical Equipment (IoMT)"
    elif ip.startswith("172."):
        return "Administrative System"
    else:
        return "External Unknown Device"
