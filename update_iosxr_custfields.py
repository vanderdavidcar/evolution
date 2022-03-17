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
NETBOX_URL = "https://demo.netbox.dev/"

"""
2 - Get API Token on Netbox
"""
NETBOX_TOKEN = config.api_key

"""
3 - Insted Postman I'm using Pynetbox to send a GET a take this informations
"""
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

"""
5 - Information to collect: software version
Custom field to update: "sw_version"
Assume network device list would contain Cisco Catalyst IOS
"""
# NAPALM to get.facts() of IOS
driver = get_network_driver("iosxr")
device = driver(
    hostname="", username=config.nb_username, password=config.nb_password
)
device.open()
iosxr_getfacts = json.dumps(device.get_facts(), indent=4)


# Store get.facts() as variable
results = iosxr_getfacts

# Pattern to use regex in a file iosxr_version.txt
version_pattern = re.compile(r"Cisco IOS XR Software, Version (?P<version>\S....)")
iosxr_version = version_pattern.search(results)

# Print regex information collect ina file iosxr_version.txt
print("IOS Version regex: ".ljust(18) + iosxr_version.group("version"))
version = iosxr_version.group("version")
# Retrieve router object for update with dictionary
iosxr_update = nb.dcim.devices.get(name="")
dict_update = dict(iosxr_update)
# Update custom fields "sw_version" using regex information collected
dict_update["custom_fields"]["sw_version"] = version
iosxr_update.save()

print("Current serial number: ", iosxr_update.name)
print("Device Type: ", iosxr_update.device_type)
print("sw_version: ", iosxr_update.custom_fields["sw_version"])
print("Current tenant: ", iosxr_update.tenant)
