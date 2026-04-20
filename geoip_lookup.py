# geoip_lookup.py

def get_location(ip):
    """
    Global Attack Source Intelligence

    Maps suspicious source IPs
    to their approximate attack origin location.
    Demo version for lecturer presentation.

    Real production version can later use:
    ipinfo API
    MaxMind GeoLite2
    AbuseIPDB
    VirusTotal intelligence feeds
    """

    ip = str(ip)

    sample_locations = {
        "8.8.8.8": "United States",
        "185.143.223.12": "Russia",
        "45.77.12.89": "Germany",
        "103.21.244.0": "Singapore",
        "192.168.1.10": "Internal Hospital Network"
    }

    return sample_locations.get(
        ip,
        "Unknown Location"
    )
