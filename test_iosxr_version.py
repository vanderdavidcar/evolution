import pytest

ios_output = """
"os_version": "Cisco IOS XR Software, Version 7.0.2)",
"""
print(ios_output)

ios_data = "7.0.2"
assert ios_data == "12.2(55)SE5"


ios_output = """
"os_version": ""os_version": "Cisco IOS XR Software, Version 7",
"""
print(ios_output)
ios_data = "7.0.2"
assert ios_data is None
