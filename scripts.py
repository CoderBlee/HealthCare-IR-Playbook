from scapy.all import *

def detect_unusual_activity(packets):
    for packet in packets:
        if packet.haslayer(TCP):
            # Simple detection of unusual high port usage
            if packet[TCP].dport > 1024:
                print(f"Unusual activity detected: {packet.summary()}")

# Capture network packets (example, interface might need to be specified)
packets = sniff(count=100)
detect_unusual_activity(packets)
