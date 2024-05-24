import pyshark

# Load the pcap file
PCAP_FILE = "D:\\Users\\curtismechling\\Documents\\CTFs\\Hack The Box\\Business CTF 2024\\Forensics\\forensics_tangle_heist\\capture.pcap"
cap = pyshark.FileCapture(PCAP_FILE)


# Function to extract LDAP and Kerberos packets
def extract_packets(cap):
    ldap_packets = []
    kerberos_packets = []

    for packet in cap:
        if "LDAP" in packet:
            ldap_packets.append(packet)
        elif "KERBEROS" in packet:
            kerberos_packets.append(packet)

    return ldap_packets, kerberos_packets


def main():
    ldap_packets, kerberos_packets = extract_packets(cap)

    # Extract information from LDAP packets
    ldap_info = []
    for packet in ldap_packets:
        try:
            info = {
                "time": packet.sniff_time,
                "source": packet.ip.src,
                "destination": packet.ip.dst,
                "info": str(packet.ldap),
            }
            ldap_info.append(info)
        except AttributeError:
            continue

    # Extract information from Kerberos packets
    kerberos_info = []
    for packet in kerberos_packets:
        try:
            info = {
                "time": packet.sniff_time,
                "source": packet.ip.src,
                "destination": packet.ip.dst,
                "info": str(packet.kerberos),
            }
            kerberos_info.append(info)
        except AttributeError:
            continue

    len(ldap_packets), len(kerberos_packets), ldap_info[:3], kerberos_info[:3]


if __name__ == "__main__":
    main()
