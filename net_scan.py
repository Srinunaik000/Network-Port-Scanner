import ipaddress
import subprocess
import platform
import threading

def is_host_alive(ip):
    """Ping a host to check if it's alive."""
    try:
        # Set ping command based on OS
        param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        result = subprocess.run(["ping", param, ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except:
        return False

def scan_cidr_network(cidr):
    """Scan an entire subnet for live hosts."""
    live_hosts = []
    ip_list = [str(ip) for ip in ipaddress.IPv4Network(cidr, strict=False)]
    
    def worker(ip):
        if is_host_alive(ip):
            print(f"[+] Live Host Found: {ip}")
            live_hosts.append(ip)
    
    threads = []
    for ip in ip_list:
        thread = threading.Thread(target=worker, args=(ip,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

    print("\nScan Completed!")
    print(f"Live Hosts in {cidr}: {live_hosts}")

# Example usage
cidr_range = input("Enter CIDR (e.g., 192.168.1.0/24): ")
scan_cidr_network(cidr_range)
