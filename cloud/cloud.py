#!/usr/bin/env python
import pynetbox
import urllib3
from pprint import pprint
urllib3.disable_warnings()


NETBOX_URL = "https://netbox.int.flexcloud.com.br/"
NETBOX_TOKEN = "dea33dafd8a1bf0daba55576573c259f2a73d341"

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False



devices = list(nb.dcim.devices.all())

leafs = list(nb.dcim.devices.get(name='brlp-spac09-spine2-2')) 
print(leafs)
print('#############################')


vmware = list(nb.dcim.devices.get(name='BCM-PP01-CL01-ESX001')) 
print(vmware)

devices = list(nb.tenancy.tenants.filter(q='embratel'))
for device in devices:
    if devices:
        print(device)
    else:
        print("Not found")

print('#############################')

leaf_devices = list(nb.dcim.devices.get(name='brcta-bt02-stor1-2'))
print(leaf_devices)
print('#############################')

devices = list(nb.dcim.devices.filter(name='brlp-spac09-spine2-2'))
for device in devices:
    if devices:
        print(device.name)
    else:
        print("Not found")
print('#############################')
devices = list(nb.dcim.devices.filter(role='spine-osp'))
for device in devices:
    if devices:
        print(device)
    else:
        print("Not found")
print('#############################')
devices = list(nb.dcim.devices.filter(role='leaf-storage'))
for device in devices:
    if devices:
        print(device)
    else:
        print("Not found")
print('#############################')

#status = list(nb.dcim.devices.filter(status='Planned', status=True))
#print(status)


#for device in devices:
#    print(device)