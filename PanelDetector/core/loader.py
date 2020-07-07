# Created by LimerBoy
# https://github.com/LimerBoy/AdminPanelFinder
#
# --Need more IP ranges?
# -- https://4it.me/getlistip
# -- https://suip.biz/ru/?act=ipcountry

# Import modules
from os import listdir
from sys import exit

# Select IP ranges from directory
def SelectIPRanges():
    path = "ip-ranges/"           # Directory path.
    files = listdir(path)         # Get directory files.
    for i, f in enumerate(files): # Enumerate and
        print(f" [{i+1}] - {f}")  # print files.
    # *-- Get user input --*
    try:
        file = path + files[int(input("\n [?] Please select country to scan --> ")) - 1]
    except ValueError: 
        exit(f" [!] ERROR: Please enter a numerical value!")
    except IndexError:
        exit(f" [!] ERROR: Please enter value from 1 to {len(files)}!")
    else:
    # *-- Read file --*
        with open(file, "r") as ranges_file: # Open file in reading mode.
            ranges = ranges_file.readlines() # Read all lines.

    return ranges, file.split("/")[-1]