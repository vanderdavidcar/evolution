#!/usr/bin/env python
from textwrap import indent
from napalm import get_network_driver
import json
import config_cloud
import urllib3
urllib3.disable_warnings()

NETBOX_URL = "https://netbox.int.flexcloud.com.br/"
NETBOX_TOKEN = config_cloud.api_key


driver = get_network_driver("asa")
device = driver(hostname='BSL-PES-FW01',
                username= config_cloud.cloud_username,
                password= config_cloud.cloud_password,)
                #optional_args={'port':8181})

device.open()
#device.get_interfaces()
print(json.dumps(device.get_facts(), indent=4))
print(json.dumps(device.get_environment(), indent=4))
print(json.dumps(device.get_config(retrieve='running', full=False)))

