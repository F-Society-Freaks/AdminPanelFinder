# Created by LimerBoy
# https://github.com/LimerBoy/AdminPanelFinder

# Import modules
from base64 import b64encode 
from requests import get
from random import choice
from socket import socket, AF_INET, SOCK_STREAM
from hashlib import md5
from time import sleep
from re import compile as re_compile
from .signatures import Signatures

# HTTP proxy
proxies = {
    "http": "",
    "https": "",
}

# HTML <title> tag ReGex pattern
__title_pattern = re_compile("(?<=<title>).*?(?=</title>)")

# Add http to IP address
def __FormatAddr(address):
    if not address.startswith("http"):
        address = "http://" + address
    return address

# Get page title
def GetTitle(content):
    data = __title_pattern.findall(content)
    if len(data) > 0:
        return data[0]
    else:
        return ""    

# Get random user agent
def RandomUserAgents():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; rv:76.0) Gecko/20100101 Firefox/76.0",
        "Mozilla/5.0 (Linux; Android 10; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.93 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Snapchat/10.77.5.59 (like Safari/604.1)",
        "Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15",
    ]
    agent = choice(agents)
    return {"user-agent": agent}

# Check html content by signatures
def InspectContent(content):
    content = str(content
        .replace("\n", "")      # and replace "\n"
        .replace("\r", "")      # and "\r" to ""
        .lower()                # and lowercase.
    )
    # *-- Signatures inspection --*        #
    for signature in Signatures:           # Check all signatures.
        for data in signature.signatures:  # 
            if data.lower() in content:    # If signature is match
                return True, signature     # return detected signature.
                                           #
    return False, None                     # Continue scanning.

# Scan host and detect path's
def InspectPaths(address):
    for sig in Signatures:              # Check all signatures path's
        for path in sig.paths:          # Get path's from signature. 
            status, content = (         #
                Request(address + path) # Make HTTP request
            )                           # to http://address/path.
                                        #
            if status:                  # If selected path exists
                p = str("http://"       # add path http,
                    + address           # add path address,
                    + path)             # add location.
                return True, content, p # return detected signature.
                                        #
    return False, None, None            # Return nothing.

# Retrieve HTML content
def Request(address):
    # *-- Get page content --*      #
    address = __FormatAddr(address) # Add http://
    try:                            #
        request=get(address,        # HTTP GET request.
        headers=RandomUserAgents(), # Set random user agents.
        proxies=proxies)            # Set proxy.
    except:                         # If error occurs
        return False, None          # return nothing.
                                    #
    if request.status_code != 200:  # If response code is not 200
        return False, None          # continue scanning.
                                    #
    return True, request.text       # Return content


# Check if HTTP port is open
def PortIsOpen(address, port=80):
    while True:
        try:
            # *-- HTTP port checking --*        #
            sock = socket(AF_INET, SOCK_STREAM) # Create TCP socket.
            sock.settimeout(0.5)                # Set timeout.
            target = (address, port)            # Set target.
            result = sock.connect_ex(target)    # Connect.
            sock.close()                        # Close socket.
            return result.__eq__(0)             # Return status.
        except OSError:                         # If socket creation failed
            sleep(3)                            # we sleep 3 seconds
            continue                            # and try again.
    