#!/usr/bin/env python
import pynetbox
import urllib3
from pprint import pprint
urllib3.disable_warnings()
from napalm import get_network_driver
import json
import config_cloud
import re

NETBOX_URL = "https://netbox.int.flexcloud.com.br/"
NETBOX_TOKEN = config_cloud.api_key

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

devices = list(nb.dcim.devices.all())

#ten_stat_cond = nb.dcim.devices.filter(tenant="connect-edge", status="planned")
ten_stat_cond = nb.dcim.devices.filter(name="brbsa-bt01-repl1-1", status="active")
for device in ten_stat_cond:
    print('\n'
            "Name:\t{devname}"
            "\nTenant:\t{devtenant}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}"
            "\nStatus:\t{devstatus}"
            "\nSite:\t{devsite}".format(
            devname=device.name, devtenant=device.tenant,
            devstatus=device.status['label'], devsite=device.site,
            devmodel=device.device_type['model'],
            devmanufacturer=device.device_type['manufacturer']['display'], 
            devcustomfield=device.custom_fields['sw_version']
            )
        )

driver = get_network_driver("nxos")
device = driver(hostname='brbsa-bt01-repl1-1',
                username= config_cloud.cloud_username,
                password= config_cloud.cloud_password,)
                #optional_args={'port':8181})

device.open()
#device.get_interfaces()
print(json.dumps(device.get_facts(), indent=4))