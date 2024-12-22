import pyshark

def traffic():
    try:
        # Capturing live packets using LiveCapture
        capture_packets = pyshark.LiveCapture(interface="wlp8s0", tshark_path="/usr/bin/tshark")

        # Initializing the capture
        print("Listening for packets... Press Ctrl+C to stop.")
        
        # Sniff 10 packets and display a summary of each
        for packet in capture_packets.sniff_continuously(packet_count=10):
            print(packet)  # Or print(packet.summary())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    traffic()
