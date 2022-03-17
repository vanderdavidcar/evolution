import pynetbox
import re
from napalm import get_network_driver
import config
import json
import urllib3


urllib3.disable_warnings()

NETBOX_URL = "https://demo.netbox.dev/"
NETBOX_TOKEN = config.api_key

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

# NAPALM to get.facts() of NX-OS
driver = get_network_driver("nxos")
device = driver(
    hostname="brbsa-bt02-repl1-2",
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
nxos_update = nb.dcim.devices.get(name="brbsa-bt01-repl1-1")
dict_update = dict(nxos_update)
# Update custom fields "sw_version" using regex information collected
dict_update["custom_fields"]["sw_version"] = version
nxos_update.save()

print("Current serial number: ", nxos_update.name)
print("Device Type: ", nxos_update.device_type)
print("sw_version: ", nxos_update.custom_fields["sw_version"])
print("Current tenant: ", nxos_update.tenant)
