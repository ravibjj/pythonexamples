# Simple Port Scanner
# Ravi Nori
# Usage : takes an ip address or hostname and will scan for all OPEN ports

import sys
import socket
from datetime import datetime

# Header Banner
print("*" * 50)
print("Port Scanner")
print("*" * 50)

# Defining the target
if len(sys.argv) == 2:
    # translate hostname to IPV4
    if sys.argv[1].isnumeric() == True:
        targetip = sys.argv[1]
    else:
        targetip = socket.gethostbyname(sys.argv[1])
else:
    print("Please re-enter a valid ip or hostname")

# Scanning Banner
print("-" * 50)
print("Scanning Target IP: " + targetip)
print("Scanning commences at :" + str(datetime.now()))
print("-" * 50)

try:
    # scan ports between 1 and 65,535
    for port in range (1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # returns an error indicator if not valid response
        result = s.connect_ex((targetip,port))
        # will display only open ports
        if result == 0:
            print("Port {} is open".format(port))
        #else:
         #   print("Port {} is closed".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname or IP or could not be resolved!")
    sys.exit()
except socket.error:
    print("\n Server not responding!")
    sys.exit()



