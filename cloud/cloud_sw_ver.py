#!/usr/bin/env python
import pynetbox
import urllib3
from pprint import pprint
import json
import requests

urllib3.disable_warnings()

NETBOX_URL = "https://netbox.int.flexcloud.com.br/"
NETBOX_TOKEN = "dea33dafd8a1bf0daba55576573c259f2a73d341"

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

devices = nb.dcim.devices.all()

juniper = list(nb.dcim.devices.filter(manufacturer="juniper"))
for device in juniper:
    if device.device_type['manufacturer']:
        print(80* "#")
        print("This is a JunOS")
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
    print("Juniper not found")

arista = list(nb.dcim.devices.filter(manufacturer="arista"))
for device in arista:
    if device.device_type['manufacturer']:
        print(80* "#")
        print("This is a Arista OS")
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
    print("Arista not found")

fortinet = list(nb.dcim.devices.filter(manufacturer="fortinet"))
for device in fortinet:
    if device.device_type['manufacturer']:       
        print(80* "#")
        print("This is a Fortinet")
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
    print("Fortinet not found")

cisco_ios = list(nb.dcim.devices.filter(manufacturer="cisco"))
for device in cisco_ios:
    if device.device_type['manufacturer']:
        print(80* "#")
        print("This is a Cisco Catalist IOS")
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
        print("Cisco not found")

dell = list(nb.dcim.devices.filter(manufacturer="dell"))
for device in dell:
    if device.device_type['manufacturer']:       
        print(80* "#")
        print("This is a Dell OS")
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
    print("Dell OS not found")

aruba = list(nb.dcim.devices.filter(manufacturer="aruba"))
for device in aruba:
    if device.device_type['manufacturer']:       
        print(80* "#")
        print("This is a Aruba OS")
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
    print("Aruba OS not found")

panos = list(nb.dcim.devices.filter(manufacturer="panos"))
for device in panos:
    if device.device_type['manufacturer']:
        print(80* "#")
        print("This is a PaloAlto PAN-OS")
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
    print("PaloAlto PAN OS not found")

cisco_nxos = list(nb.dcim.devices.filter(manufacturer="nxos"))
for device in cisco_nxos:
    if device.device_type['manufacturer']:
        print(80* "#")
        print("This is a Cisco Nexus OS")
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
    print("Cisco Nexus OS not found")

cisco_asa = list(nb.dcim.devices.filter(manufacturer="asa"))
for device in cisco_asa:
    if device.device_type['manufacturer']:
        print(80* "#")
        print("This is a Cisco ASA OS")
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
    print("Cisco ASA OS not found")

