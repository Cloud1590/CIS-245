blacklist_ips = [
    "192.168.1.100",
    "10.0.0.5",
    "172.16.0.50",
    "203.0.113.25"
]

check_ips = ["192.168.1.100", "192.168.1.101", "172.16.0.50", "203.0.113.30"]

# check if an IP is blacklisted
def is_ip_blacklisted(ip, blacklist):
    return ip in blacklist

# process a list of IPs
def process_ips(ip_list, blacklist):
    blacklisted_ips = []
    for ip in ip_list:
        if is_ip_blacklisted(ip, blacklist):
            blacklisted_ips.append(ip)
    return blacklisted_ips

# check if an IP is blacklisted
blacklisted = process_ips(check_ips, blacklist_ips)

# print the blacklisted IPs
print("Blacklisted IPs found:", blacklisted)
