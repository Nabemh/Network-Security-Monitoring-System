import sqlite3

def query_packets():
    conn = sqlite3.connect('traffic.db')
    cursor = conn.cursor()

    #retrieve packets
    cursor.execute('SELECT * FROM packets ORDER BY timestamp DESC LIMIT 10')
    packets = cursor.fetchall()

    for packet in packets:
        print(packet)

    conn.close()

if __name__ == "__main__":
    query_packets()