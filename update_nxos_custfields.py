import pynetbox
import re
from napalm import get_network_driver
import config
import json
import urllib3
urllib3.disable_warnings()

"""
1 - Access the Netbox Demo
"""
NETBOX_URL = config.nb_url

"""
2 - Get API Token on Netbox
"""
NETBOX_TOKEN = config.api_key

"""
3 - Insted of Postman I'm using Pynetbox to send GET and take informations from devices
"""
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

"""
5 - Information to collect: software version
Custom field to update: "sw_version"
Assume network device list would contain Cisco Nexus OS
"""
# List of devices vendors "NXOS"
nxos_model = nb.dcim.devices.filter(model="nexus-9300")

# NAPALM to get.facts() of NX-OS
for devices in nxos_model:
    driver = get_network_driver("nxos")
    device = driver(
        hostname=devices,
        username=config.nb_username,
        password=config.nb_password,
)
device.open()
nxos_getfacts = json.dumps(device.get_facts(), indent=4)

# Store get.facts() as variable
results = nxos_getfacts

# Pattern to use regex in a file nxos_version.txt
version_pattern = re.compile(r'"os_version": "(?P<version>\S.....)')
nxos_version = version_pattern.search(results)

# Print regex information collect ina file nxos_version.txt
print("NX-OS Version regex: ".ljust(18) + nxos_version.group("version"))
version = nxos_version.group("version")

# Retrieve router object for update with dictionary
for devices in nxos_model:
    # Update custom fields "sw_version" using regex information collected
    devices["custom_fields"]["sw_version"] = version
    devices.save()

    print("Hostname: ", devices.name)
    print("Device Type: ", devices.device_type)
    print("sw_version: ", devices.custom_fields["sw_version"])
    print("Current tenant: ", devices.tenant)