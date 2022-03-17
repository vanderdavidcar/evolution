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

fortinet = list(nb.dcim.devices.filter(manufacturer="fortinet"))
for display in fortinet:
    if display.device_type['manufacturer']:
        print("This is a Fortigate")
        print(display.id, display.name, display.device_type, display.custom_fields)
        print()
else:
    print("Fortinet not found")

cisco_ios = list(nb.dcim.devices.filter(manufacturer="cisco"))
for display in cisco_ios:
    if display.device_type['manufacturer']:
        print("This is a Cisco Catalyst OS")
        print(display.id, display.name, display.device_type, display.custom_fields)
        print()
else:
    print("Cisco Catalyst OS not found")

arista = list(nb.dcim.devices.filter(manufacturer="arista"))
for display in arista:
    if display.device_type['manufacturer']:
        print("This is a Arista OS")
        print(display.id, display.name, display.device_type, display.custom_fields)
        print()
else:
    print("Arista not found")
    
juniper = list(nb.dcim.devices.filter(manufacturer="juniper"))
for display in juniper:
    if display.device_type['manufacturer']:
        print("This is a JunOS")
        print(display.id, display.name, display.device_type, display.custom_fields)
        print()
else:
    print("Juniper not found")

dell = list(nb.dcim.devices.filter(manufacturer="dell"))
for display in dell:
    if display.device_type['manufacturer']:
        print("This is a DellOS")
        print(display.id, display.name, display.device_type, display.custom_fields)
        print()
else:
    print("DellOS not found")

#platform = list(nb.dcim.devices.filter(manufacturer="fortinet").update(custom_fields="FortiOS"))
#for display in platform:
#    display = nb.dcim.devices.update([
#    {display.custom_fields['sw_version']: 'FortiOS'},
#    ])
#    print(display.id, display.name, display.device_type, display.custom_fields)
    #display.custom_fields = "FortiOS"
    #display.updates()
    #display = nb.dcim.devices.update({"sw_version": "FortiOS"})
