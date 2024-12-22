import pyshark
import sqlite3


def save_to_db(packet):
    conn = sqlite3.connect('traffic.db')
    cursor = conn.cursor()

      # extracting packet information
    if hasattr(packet, 'ip'):
        source_ip = packet.ip.src
        destination_ip = packet.ip.dst
    else:
        source_ip = "Unknown"
        destination_ip = "Unknown"

    protocol = packet.transport_layer or 'Unknown'
    port = None  # Default to None if no port is found
    if hasattr(packet, 'tcp') or hasattr(packet, 'udp'):
        port = packet[packet.transport_layer].dstport

    length = packet.length
    info = str(packet)[:100]  # Limiting the size


    #inserting informantion into database
    cursor.execute('''
                   INSERT INTO packets (source_ip, destination_ip, protocol, port, length, info)
                   VALUES (?, ?, ?, ?, ?, ?)
                   ''', (source_ip, destination_ip, protocol, port, length, info))
    
    conn.commit()
    conn.close()

def traffic_capture():
    capture_packets = pyshark.LiveCapture(interface="wlp8s0")
    print ("Listening...")
    for packet in capture_packets.sniff_continuously(packet_count=10):
        save_to_db(packet)
        print(f"Saved packet {packet}")

if __name__ == "__main__":
    traffic_capture()