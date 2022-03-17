import pytest

ios_output = """
"uptime": 33731460,
    "vendor": "Cisco",
    "os_version": "C2960S Software (C2960S-UNIVERSALK9-M), Version 12.2(55)SE5, RELEASE SOFTWARE (fc1)",
    "serial_number": "FOC1702W39L",
    "model": "WS-C2960S-48LPS-L",
    "hostname": "br-lp-spac04-mgmt-1-2",
"""
print(ios_output)

ios_data = "12.2(55)SE5"
assert ios_data == "12.2(55)SE5"


ios_output = """
"uptime": 33731460,
    "vendor": "Cisco",
    "os_version": "C2960S Software (C2960S-UNIVERSALK9-M), Version , RELEASE SOFTWARE (fc1)",
    "serial_number": "FOC1702W39L",
    "model": "WS-C2960S-48LPS-L",
    "hostname": "br-lp-spac04-mgmt-1-2",
"""
print(ios_output)
ios_data = "12.2(55)SE5"
assert ios_data is None