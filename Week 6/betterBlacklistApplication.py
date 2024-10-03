# List of blacklisted IP addresses
blacklisted_ips_list = [
    "192.168.1.100",
    "10.0.0.5",
    "172.16.0.50",
    "203.0.113.25"
]

# List of IP addresses to check
ip_addresses_to_check = ["192.168.1.100", "192.168.1.101", "172.16.0.50", "203.0.113.30"]

# Function to check if a specific IP is blacklisted
def is_ip_in_blacklist(ip_address, blacklist):
    return ip_address in blacklist

# Function to process the list of IP addresses and return only those that are blacklisted
def get_blacklisted_ips(ip_list, blacklist):
    found_blacklisted_ips = []
    for ip in ip_list:
        if is_ip_in_blacklist(ip, blacklist):
            found_blacklisted_ips.append(ip)
    return found_blacklisted_ips

# Find and print blacklisted IPs
blacklisted_ips = get_blacklisted_ips(ip_addresses_to_check, blacklisted_ips_list)

print("Blacklisted IPs found:", blacklisted_ips)