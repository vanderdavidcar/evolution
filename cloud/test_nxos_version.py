import pytest

nxos_output = """
    "vendor": "Cisco",
    "serial_number": "FDO23350U1E",
    "model": "Nexus9000 93180YC-EX chassis",
    "hostname": "brbsa-bt02-repl2",
    "os_version": "9.2(3)",
"""
print(nxos_output)

nxos_data = "9.2(3)"
print(nxos_data)
assert nxos_data == "9.2(3)"


nxos_output = """
    "vendor": "Cisco",
    "serial_number": "FDO23350U1E",
    "model": "Nexus9000 93180YC-EX chassis",
    "hostname": "brbsa-bt02-repl2",
"""
print(nxos_output)
nxos_data = "9.2(3)"
print(nxos_data)
assert nxos_data is None