import pytest

ios_output = """
"os_version": "C2960S Software (C2960S-UNIVERSALK9-M), Version 12.2(55)SE5, RELEASE SOFTWARE (fc1)",
"""
#print(ios_output)

ios_data = "12.2(55)SE5"
assert ios_data == "12.2(55)SE5"


ios_output = """
"os_version": "C2960S Software (C2960S-UNIVERSALK9-M), Version , RELEASE SOFTWARE (fc1)",
"""
#print(ios_output)
ios_data = "12.2(55)SE5"
assert ios_data is None
