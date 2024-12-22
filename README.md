<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Network Security Monitoring System - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f9;
        }
        h1, h2, h3 {
            color: #333;
        }
        h2 {
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
        }
        code {
            font-family: "Courier New", Courier, monospace;
            background-color: #eaeaea;
            padding: 0 5px;
        }
        pre {
            background-color: #2c3e50;
            color: white;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        ul {
            list-style-type: disc;
            padding-left: 20px;
        }
        li {
            margin-bottom: 10px;
        }
        .highlight {
            color: #2980b9;
            font-weight: bold;
        }
        footer {
            text-align: center;
            margin-top: 30px;
            font-size: 0.8em;
            color: #777;
        }
    </style>
</head>
<body>

    <h1>Network Security Monitoring System</h1>
    
    <p>This project involves building a Network Security Monitoring System that captures network traffic and stores it in a database for analysis. The primary goal of the system is to monitor network activity, detect potential threats, and store packet details such as source and destination IPs, protocols, and other relevant information for further analysis.</p>
    
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#technologies">Technologies Used</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#database">Database Schema</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
    </ul>
    
    <h2 id="introduction">Introduction</h2>
    <p>This system uses <code>pyshark</code> to capture live packets from the network and processes them to extract relevant information such as IP addresses, protocol types, ports, and packet length. This information is then saved to a SQLite database for further analysis. The goal is to build a simple Intrusion Detection System (IDS) to monitor network traffic in real-time.</p>
    
    <h2 id="features">Features</h2>
    <ul>
        <li>Real-time packet capture using <code>pyshark</code>.</li>
        <li>Packet filtering based on protocols (TCP, UDP, HTTP, etc.).</li>
        <li>Storage of packet details such as source and destination IP, protocol, port, and packet length in a SQLite database.</li>
        <li>Simple web interface (optional, for future development).</li>
        <li>Database schema to store captured traffic data for future analysis.</li>
    </ul>
    
    <h2 id="technologies">Technologies Used</h2>
    <ul>
        <li><strong>Python 3.x</strong> - The main programming language used.</li>
        <li><strong>Pyshark</strong> - Python wrapper for the Wireshark network packet capture tool.</li>
        <li><strong>SQLite3</strong> - A lightweight database engine to store captured packet details.</li>
        <li><strong>Wireshark/Tshark</strong> - For packet capturing and analysis.</li>
    </ul>
    
    <h2 id="installation">Installation</h2>
    <p>Follow these steps to install the necessary dependencies and set up the system:</p>
    <pre>
        # Install required packages
        sudo apt update
        sudo apt install tshark python3-pyshark sqlite3
        
        # Clone the repository (replace with actual repository URL)
        git clone https://github.com/yourusername/network-security-monitoring.git
        
        # Navigate to the project folder
        cd network-security-monitoring
        
        # Set up the Python environment (optional but recommended)
        python3 -m venv myenv
        source myenv/bin/activate
        
        # Install Python dependencies
        pip install -r requirements.txt
    </pre>
    
    <h2 id="usage">Usage</h2>
    <p>To run the Network Security Monitoring System, execute the following command:</p>
    <pre>
        python3 main.py
    </pre>
    <p>The system will start listening for network packets, capture data, and store it in the SQLite database <code>traffic.db</code>.</p>
    
    <h2 id="database">Database Schema</h2>
    <p>The SQLite database stores packet details in a table named <code>packets</code>. Below is the schema for the table:</p>
    <pre>
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
    </pre>
    <p>This table stores the following columns:</p>
    <ul>
        <li><strong>id:</strong> Auto-incremented primary key.</li>
        <li><strong>timestamp:</strong> The time when the packet was captured.</li>
        <li><strong>source_ip:</strong> The source IP address of the packet.</li>
        <li><strong>destination_ip:</strong> The destination IP address of the packet.</li>
        <li><strong>protocol:</strong> The protocol used in the packet (e.g., TCP, UDP, ARP, etc.).</li>
        <li><strong>port:</strong> The port number (if applicable, for protocols like TCP/UDP).</li>
        <li><strong>length:</strong> The size of the packet.</li>
        <li><strong>info:</strong> A brief description of the packet.</li>
    </ul>
    
    <h2 id="contributing">Contributing</h2>
    <p>If you'd like to contribute to this project, please follow these steps:</p>
    <ul>
        <li>Fork the repository.</li>
        <li>Clone your fork to your local machine.</li>
        <li>Create a new branch for your feature or bug fix.</li>
        <li>Make your changes and commit them with descriptive messages.</li>
        <li>Push your changes to your fork.</li>
        <li>Open a pull request to the main repository.</li>
    </ul>
    
    <h2 id="license">License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    
    <footer>
        <p>Network Security Monitoring System &copy; 2024</p>
    </footer>
    
</body>
</html>
