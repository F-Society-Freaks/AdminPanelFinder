# Created by LimerBoy
# https://github.com/LimerBoy/AdminPanelFinder

# Import modules
from .inspection import Request, InspectPaths, InspectContent, PortIsOpen, GetTitle
from .signatures import Signatures
from .logger import Log
from ipaddress import ip_address
from threading import Thread

# Scan result
class __Result:
    def __init__(self, name, atype, path, title):
        self.name = name
        self.type = atype
        self.path = path
        self.title = title

# pizdec (ctrl+c, ctrl+v)
# Return IPs in IPv4 range, inclusive.
def IPsRange(start='', end=''):
    if not start and not end:
        return []
    if not end and start.__contains__("-"):
        start, end = start.split("-")
    end = end.replace("\n","")
    start = int(ip_address(start).packed.hex(), 16)
    end = int(ip_address(end).packed.hex(), 16)
    return [ip_address(ip).exploded for ip in range(start, end)]


# Scan selected address
def ScanAddress(address):
    # *-- HTTP port checking --*     #
    if not PortIsOpen(address):      # If HTTP port is closed
        return False, None           # stop scanning.
    # *-- Path's detection --*       # 
    detected, content, path = (      # Detect malware
        InspectPaths(address)        # default path's
    )                                # on server.
    if not detected:                 # If path's not found
        return False, None           # stop target scanning.
    # *-- Signatures inspection --*  #
    detected, signature = (          # Check all 
        InspectContent(content)      # signatures.
    )                                #
    if not detected:                 # If signature not match
        return False, None           # stop target scanning.
    # *-- Detected result --*        #
    return True, __Result(           # If signature match - return detected signature
        signature.name,              # name
        signature.type,              # type
        path,                        # server path
        GetTitle(content),           # <title> tag. 
    )           

# Check address in new (this) thread
def __СheckAddrThreaded(address):
    status, signature = ScanAddress(address)
    if status:
        Log(f" [+] Found: \"{signature.name}\" ({signature.type}) on \"{signature.path}\" with title \"{signature.title}\". ")
    #else:
    #    print(f"[-] Address is clean {address}")

# Scan IP address range
def ScanRange(ranges):
    threads = []                        # Threads list.
    # *-- Scan IP range --*             #
    for address in IPsRange(ranges):    # Scan range.
        t = Thread(                     # Create thread.
            target=__СheckAddrThreaded, # Set target.
            args=(address,)             # Set address.
        )                               #
        threads.append(t)               # Add thread to threads list.
        t.start()                       # Start thread.
    for thread in threads:              # Wait all threads
        thread.join()                   # for stop.