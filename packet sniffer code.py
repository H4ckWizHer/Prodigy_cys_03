from scapy.all import *

# Global variable to store packets
captured_packets = []

def get_protocol_name(protocol_num):
    """Convert protocol number to protocol name."""
    protocol_name = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
    return protocol_name.get(protocol_num, "Other")

def capture_packets(interface):
    """Function to capture packets with a user-friendly approach."""
    def packet_callback(packet):
        captured_packets.append(packet)
        print(f"Packet #{len(captured_packets)} captured.")
        
    try:
        print(f"[*] Initiating packet capture on {interface}. Press Ctrl+C to stop.")
        sniff(iface=interface, filter="ip", prn=packet_callback, store=False)
    except KeyboardInterrupt:
        print("\n[*] Packet capture halted by user.")
        
def analyze_packets():
    """Function to analyze captured packets based on user-selected criteria."""
    if not captured_packets:
        print("No packets to analyze. Try capturing packets first.")
        return

    print("\nSelect the detail level for packet analysis:")
    print("1. IP Addresses")
    print("2. Protocols")
    print("3. Payload Data")
    print("4. All of the above")
    choice = input("Enter your choice (1-4): ").strip()

    for packet in captured_packets:
        if IP in packet:
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            protocol = get_protocol_name(packet[IP].proto)
            
            if choice == '1':
                print(f"From: {src_ip} To: {dst_ip}")
            elif choice == '2':
                print(f"Protocol: {protocol}")
            elif choice == '3':
                if Raw in packet:
                    payload = repr(packet[Raw].load)[:50]  # Display first 50 characters
                    print(f"Payload (first 50 chars): {payload}")
            elif choice == '4':
                print(f"From: {src_ip} To: {dst_ip} | Protocol: {protocol}")
                if Raw in packet:
                    payload = repr(packet[Raw].load)[:50]
                    print(f"Payload (first 50 chars): {payload}")
            else:
                print("Invalid choice.")
            print("---------------------------------------------------")

def main():
    print("Welcome to the Ethical Packet Sniffer Tool for Educational Purposes.")
    print("Please use this tool responsibly and only on networks you have permission to analyze.\n")
    
    while True:
        print("\n1. Capture Network Packets")
        print("2. Analyze Network Packets")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            interface = input("Choose the interface (e.g., eth0, wlan0): ").strip()
            capture_packets(interface)
        elif choice == '2':
            analyze_packets()
        elif choice == '3':
            print("Thank you for using the Ethical Packet Sniffer. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
