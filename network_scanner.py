import socket
from datetime import datetime

# ASCII Art Banner
print(r"""
  ____  _   _ _____ _     _        _____  ____  _   _ ____  
 |  _ \| | | | ____| |   | |      / _ \ \/ /\ \| | | |  _ \ 
 | |_) | |_| |  _| | |   | |     | | | \  /  | | | | | | | |
 |  __/|  _  | |___| |___| |___  | |_| /  \  | | |_| | |_| |
 |_|   |_| |_|_____|_____|_____|  \___/_/\_\ |_|\___/|____/ 
""")

# Get the IP address to scan
target = input("Enter the IP address to scan: ")

# Banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    # Scan ports 1 to 1024
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: Open")
        s.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    exit()
except socket.error:
    print("\nServer not responding.")
    exit()
