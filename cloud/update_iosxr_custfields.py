import pynetbox
import re
from napalm import get_network_driver
import config
import json
import urllib3

urllib3.disable_warnings()

NETBOX_URL = "https://netbox.int.flexcloud.com.br/"
NETBOX_TOKEN = config.api_key

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

# NAPALM to get.facts() of IOS
driver = get_network_driver("iosxr")
device = driver(
    hostname="br-lp-spad06-rt-bgw02",
    username=config.nb_username,
    password=config.nb_password,
)

device.open()
ios_getfacts = json.dumps(device.get_facts(), indent=4)


# Store get.facts() as variable
results = ios_getfacts

# Pattern to use regex in a file ios_version.txt
version_pattern = re.compile(r"Cisco IOS XR Software, Version (?P<version>\S....)")
ios_version = version_pattern.search(results)

# Print regex information collect ina file ios_version.txt
print("IOS Version regex: ".ljust(18) + ios_version.group("version"))
version = ios_version.group("version")
# Retrieve router object for update with dictionary
ios_update = nb.dcim.devices.get(name="br-lp-spad06-rt-bgw02")
dict_update = dict(ios_update)
# Update custom fields "sw_version" using regex information collected
dict_update["custom_fields"]["sw_version"] = version
ios_update.save()

print("Current serial number: ", ios_update.name)
print("Device Type: ", ios_update.device_type)
print("sw_version: ", ios_update.custom_fields["sw_version"])
print("Current tenant: ", ios_update.tenant)
    
    