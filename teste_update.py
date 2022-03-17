#!/usr/bin/env python
import pynetbox
import urllib3
from pprint import pprint
urllib3.disable_warnings()
from napalm import get_network_driver
import json
import config
import re

NETBOX_URL = "https://netbox.int.flexcloud.com.br/"
NETBOX_TOKEN = config.api_key

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

devices = list(nb.dcim.devices.all())

# Retrieve router object for update with dictionary
rtr2 = (nb.dcim.devices.get(name="brbsa-bt01-repl1-2"))
dict_rtr2 = dict(rtr2)
dict_rtr2['custom_fields']['sw_version'] = "9.3"
rtr2.save()

print("Current serial number: ", rtr2.name)
print("Device Type: ", rtr2.device_type)
print("sw_version: ", rtr2.custom_fields['sw_version'])
print("Current tenant: ", rtr2.tenant)
