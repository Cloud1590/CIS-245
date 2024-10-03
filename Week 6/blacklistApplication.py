blacklist_ips = [
    "192.168.1.100",
    "10.0.0.5",
    "172.16.0.50",
    "203.0.113.25"
]

check_ips = ["192.168.1.100", "192.168.1.101", "172.16.0.50", "203.0.113.30"]

def is_ip_blacklisted(ip, blacklist):
    print("nothing")
    print(ip in blacklist)



def process_ips(ip_list, blacklist):
    blacklisted_ips = []
    for ip in ip_list:
        print("Checking:",ip)
        if is_ip_blacklisted(ip, blacklist):
            blacklisted_ips.append(ip)
            print("Found",ip)
    return blacklisted_ips

blacklisted = process_ips(check_ips, blacklist_ips)

print("Blacklisted IPs found:", blacklisted)
