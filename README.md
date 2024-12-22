# Network Security Monitoring System

## Project Overview
This project implements a basic Network Security Monitoring System (NSMS) that captures and analyzes network traffic in real-time. The system detects and stores information about the network packets, such as source and destination IP addresses, protocols, ports, and more. The goal is to help identify potential intrusions or suspicious activity by analyzing traffic patterns.

## Technologies Used
- **Python** - For implementing the monitoring logic and data handling.  
- **Wireshark** - Used for packet capturing via PyShark.  
- **SQLite** - For storing packet information in a local database.

## Features
- Real-time packet capturing using PyShark and Wireshark.  
- Packet data storage in an SQLite database.  
- Analysis and extraction of useful data like IP addresses, protocols, ports, and packet length.  
- Alert system (optional) for detecting suspicious activity based on predefined patterns.

## Setup and Installation
1. Clone the repository:  
    ```bash  
    git clone https://github.com/yourusername/Network-Security-Monitoring-System.git  
    ```  
2. Navigate to the project directory:  
    ```bash  
    cd Network-Security-Monitoring-System  
    ```  
3. Create and activate a virtual environment (optional but recommended):  
    ```bash  
    python3 -m venv venv  
    source venv/bin/activate  
    ```  
4. Install the required dependencies:  
    ```bash  
    pip install -r requirements.txt  
    ```  
5. Run the project:  
    ```bash  
    python main.py  
    ```

## Conclusion
This system provides a basic but effective way of monitoring network traffic in real time. By storing the packet data in a database, it is possible to perform further analysis and even detect anomalies or suspicious activity. The system can be enhanced with additional features, such as automatic alerts or deeper analysis of specific protocols or packet behaviors.
