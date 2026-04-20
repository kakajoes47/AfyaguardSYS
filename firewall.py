# firewall.py

def block_ip(ip):
    """
    Admin IP Blocking Engine

    Safe demo version for project presentation.
    Simulates blocking suspicious attacker IPs.

    Real production version can later use:
    iptables / ufw / firewall-cmd integration
    """

    ip = str(ip)

    # Safety check
    if not ip:
        return "Invalid IP address."

    # Demo success response
    return f"Security Action Successful: IP {ip} has been blocked."
