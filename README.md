## Port Scanner & CIDR Range Scanner
- This repository contains a Port Scanner and a CIDR Range Scanner written in Python. The script allows you to scan open ports on a single IP address or perform a network scan to identify live hosts within a CIDR range using ICMP (ping sweep).

### Features
- Single IP Scan (-t <IP>): Scan a single IP address for open ports.
- CIDR Range Scan (-c <CIDR>): Scan a subnet (CIDR) to find which IPs are alive.

### Requirements
- Python 3.x: Ensure Python 3 is installed on your system.
- No additional libraries: This script only requires Python’s built-in libraries.

### Modules Used:
- socket - For port scanning using TCP connections.
- subprocess - For executing ping commands to check host availability (ICMP).
- ipaddress - For handling CIDR input and iterating through subnet IPs.
- platform - To determine the operating system and set the correct ping command options.

### Installation & Setup
#### Clone the repository:
- git clone https://github.com/your-username/port-scanner.git
- cd port-scanner
- Make sure you have Python 3.x installed:

bash
Copy
Edit
python3 --version
No additional libraries are needed. The script uses Python's built-in libraries (socket, subprocess, ipaddress, and platform).

Usage
1. Scan a Single IP for Open Ports
To scan a single IP address for open ports (from 1 to 1024):

bash
Copy
Edit
python3 scanner.py -t <TARGET_IP>
Example:

bash
Copy
Edit
python3 scanner.py -t 192.168.1.10
This will scan ports 1-1024 for the given IP and show which ones are open.

2. Scan a CIDR Range for Live Hosts
To scan an entire subnet and check which IPs are alive (ICMP ping sweep):

bash
Copy
Edit
python3 scanner.py -c <CIDR>
Example:

bash
Copy
Edit
python3 scanner.py -c 192.168.1.0/24
This will ping each host in the 192.168.1.0/24 range and list which ones are alive (reachable)
