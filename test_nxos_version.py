import pytest

nxos_output = """
"os_version": "9.2(3)",
"""
print(nxos_output)

nxos_data = "9.2(3)"
print(nxos_data)
assert nxos_data == "9.2(3)"


nxos_output = """
"os_version": "10",
"""
print(nxos_output)
nxos_data = "9.2(3)"
print(nxos_data)
assert nxos_data is None