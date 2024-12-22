import sqlite3

def init_db():
    conn = sqlite3.connect('traffic.db')
    cursor = conn.cursor()

    # Creating packets table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS packets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        source_ip TEXT,
        destination_ip TEXT,
        protocol TEXT,
        port INTEGER,
        length INTEGER,
        info TEXT
    );
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
