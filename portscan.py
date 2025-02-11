import socket
import argparse

banner = """
     ____            _     ____  
    |  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __  
    | |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|  
    |  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |  
    |_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|  

Author: SrinuNaik (D3V1L)
"""

def scan_ports(target):
    print(banner)
    print(f"Scanning target: {target}\n")
    
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP address to scan")
    
    args = parser.parse_args()
    
    scan_ports(args.target)
