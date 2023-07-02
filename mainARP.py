from scapy.all import ARP, Ether, srp

def arp_scan(ip_range):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_range)
    result = srp(arp_request, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

# Usage
scan_result = arp_scan("192.168.1.0/24")
for device in scan_result:
    print(f"IP: {device['ip']} MAC: {device['mac']}")
