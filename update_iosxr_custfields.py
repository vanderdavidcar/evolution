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
3 - Instead of Postman I'm using Pynetbox to send GET and take informations from devices
"""
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

"""
5 - Information to collect: software version
Custom field to update: "sw_version"
Assume network device list would contain Cisco Catalyst IOS-XR
"""
# List of devices vendors "NXOS"
iosxr_model = nb.dcim.devices.filter(model="cisco-iosxr")

# NAPALM to get.facts() of NX-OS
for devices in iosxr_model:
    driver = get_network_driver("iosxr")
    device = driver(
        hostname=devices,
        username=config.nb_username,
        password=config.nb_password,
)
device.open()
iosxr_getfacts = json.dumps(device.get_facts(), indent=4)

# Store get.facts() as variable
results = iosxr_getfacts

# Pattern to use regex in a file iosxr_version.txt
version_pattern = re.compile(r"Cisco IOS XR Software, Version (?P<version>\S....)")
iosxr_version = version_pattern.search(results)

# Print regex information collect ina file iosxr_version.txt
print("IOS-XR Version regex: ".ljust(18) + iosxr_version.group("version"))
version = iosxr_version.group("version")

# Retrieve router object for update with dictionary
for devices in iosxr_model:
    # Update custom fields "sw_version" using regex information collected
    devices["custom_fields"]["sw_version"] = version
    devices.save()

    print("Current serial number: ", devices.name)
    print("Device Type: ", devices.device_type)
    print("sw_version: ", devices.custom_fields["sw_version"])
    print("Current tenant: ", devices.tenant)
