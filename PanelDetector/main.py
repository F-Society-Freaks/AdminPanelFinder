# Created by LimerBoy
# https://github.com/LimerBoy/AdminPanelFinder

# Import modules
from core.banner import *
from core.scanner import ScanRange#, СheckAddrThreaded
from core.loader import SelectIPRanges

# Scan selected country
ranges, country = SelectIPRanges()
print(f" [!] Starting scanning {len(ranges)} ip ranges ({country})\n")
for _range in ranges:
    ScanRange(_range)

#for address in [
#     "gay-love.ru", # Nexus Stealer
#     "ddgroupupdate.com",# Nexus Stealer
#     "datamon.cc",# Nexus Stealer
#     "156.96.151.236", # Azorult Stealer
#     "a0451296.xsph.ru", # Azorult Stealer
#     "manchestergardensllc.com", # BlackNet Botnet
#     "cl22567.tmweb.ru", # Predator The Thief Stealer
#     "x99951lw.beget.tech", # Predator The Thief Stealer
#     "lc69ef39.justinstalledpanel.com", # Oski Stealer
#     "194.87.93.235", # Oski  Stealer
#     "pivnayabiz.hldns.ru", # Taurus Stealer
#     "jnoon.site", # Taurus Stealer
#     ]:
#    СheckAddrThreaded(address)
    
    