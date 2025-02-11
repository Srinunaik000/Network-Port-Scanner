## Port Scanner & CIDR Range Scanner
- This repository contains a Port Scanner and a CIDR Range Scanner written in Python. The script allows you to scan open ports on a single IP address or perform a network scan to identify live hosts within a CIDR range using ICMP (ping sweep).

### Features
- Single IP Scan (-t <IP>): Scan a single IP address for open ports.
- CIDR Range Scan (-c <CIDR>): Scan a subnet (CIDR) to find which IPs are alive.

### Requirements
- Python 3.x: Ensure Python 3 is installed on your system.
- No additional libraries: This script only requires Python’s built-in libraries.

### Installation & Setup
#### Clone the repository:
- git clone https://github.com/Srinunaik000/Network-Port-Scanner.git
- cd Network-port-Scanner
- Make sure you have Python 3.x installed:

### Executable Permission
chmod +x portscan.py net_scan.py

python3 --version
- No additional libraries are needed. The script uses Python's built-in libraries (socket, subprocess, ipaddress, and platform).

### Usage
1. Scan a Single IP for Open Ports
- To scan a single IP address for open ports (from 1 to 1024):

python3 portscan.py -t <TARGET_IP>
#### Example:
python3 portscan.py -t <ipaddress>
This will scan ports 1-1024 for the given IP and show which ones are open.

2. Scan a CIDR Range for Live Hosts
- To scan an entire subnet and check which IPs are alive (ICMP ping sweep):
python3 net_scan.py -c <CIDR>
#### Example:
python3 net_scan.py -c 192.168.1.0/24
- This will ping each host in the 192.168.1.0/24 range and list which ones are alive (reachable)
