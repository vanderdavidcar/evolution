#!/usr/bin/env python
import config
from socketserver import ThreadingUnixDatagramServer
import pynetbox
import urllib3
urllib3.disable_warnings()


NETBOX_URL = "https://demo.netbox.dev/"
NETBOX_TOKEN = config.api_key

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

devices = list(nb.dcim.devices.all())

teste_tenant = list(nb.dcim.devices.filter(status="planned"))
for device in teste_tenant:
    if device:
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
else:
    print("Not found!")
            
#print(device.tenant, device.name)
#tenants = nb.dcim.devices.get(name=11)
#pprint(dict(tenants))

