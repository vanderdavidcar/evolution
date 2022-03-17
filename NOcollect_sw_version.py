#!/usr/bin/env python
import pynetbox
import urllib3
import config

urllib3.disable_warnings()

NETBOX_URL = "https://demo.netbox.dev/"
NETBOX_TOKEN = config.api_key

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

devices = nb.dcim.devices.all()

juniper = list(nb.dcim.devices.filter(manufacturer="juniper", status="active"))
for device in juniper:
    if device.device_type["manufacturer"]:
        print(80 * "#")
        print("This is a JunOS")
        print(
            "\n"
            "Name:\t{devname}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}".format(
                devname=device.name,
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devmodel=device.device_type["model"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )
else:
    print("Juniper not found")

arista = list(nb.dcim.devices.filter(manufacturer="arista"))
for device in arista:
    if device.device_type["manufacturer"]:
        print(80 * "#")
        print("This is a Arista OS")
        print(
            "\n"
            "Name:\t{devname}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}".format(
                devname=device.name,
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devmodel=device.device_type["model"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )
else:
    print("Arista not found")

brocade = list(nb.dcim.devices.filter(manufacturer="brocade"))
for device in arista:
    if device.device_type["manufacturer"]:
        print(80 * "#")
        print("This is a Brocade OS")
        print(
            "\n"
            "Name:\t{devname}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}".format(
                devname=device.name,
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devmodel=device.device_type["model"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )
else:
    print("Brocade not found")

f5 = list(nb.dcim.devices.filter(manufacturer="f5"))
for device in f5:
    if device.device_type["manufacturer"]:
        print(80 * "#")
        print("This is a Arista OS")
        print(
            "\n"
            "Name:\t{devname}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}".format(
                devname=device.name,
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devmodel=device.device_type["model"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )
else:
    print("F5 not found")

extreme = list(nb.dcim.devices.filter(manufacturer="extreme"))
for device in arista:
    if device.device_type["manufacturer"]:
        print(80 * "#")
        print("This is a Extreme OS")
        print(
            "\n"
            "Name:\t{devname}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}".format(
                devname=device.name,
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devmodel=device.device_type["model"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )
else:
    print("Extreme not found")

cisco_ios = list(nb.dcim.devices.filter(manufacturer="cisco"))
for device in cisco_ios:
    if device.device_type["manufacturer"]:
        print(80 * "#")
        print("This is a Cisco Catalist IOS")
        print(
            "\n"
            "Name:\t{devname}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}".format(
                devname=device.name,
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devmodel=device.device_type["model"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )
    else:
        print("Cisco not found")

paloalto = list(nb.dcim.devices.filter(manufacturer="palo-alto"))
for device in paloalto:
    if device.device_type["manufacturer"]:
        print(80 * "#")
        print("This is a PaloAlto PAN-OS")
        print(
            "\n"
            "Name:\t{devname}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}".format(
                devname=device.name,
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devmodel=device.device_type["model"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )
else:
    print("PaloAlto PAN OS not found")

generic = list(nb.dcim.devices.filter(manufacturer="generic"))
for device in generic:
    if device.device_type["manufacturer"]:
        print(80 * "#")
        print("This is a Generic")
        print(
            "\n"
            "Name:\t{devname}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}".format(
                devname=device.name,
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devmodel=device.device_type["model"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )
else:
    print("Generic not found")

lenovo = list(nb.dcim.devices.filter(manufacturer="lenovo"))
for device in lenovo:
    if device.device_type["manufacturer"]:
        print(80 * "#")
        print("This is a Lenovo")
        print(
            "\n"
            "Name:\t{devname}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}".format(
                devname=device.name,
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devmodel=device.device_type["model"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )
else:
    print("Cisco Lenovo not found")

opengear = list(nb.dcim.devices.filter(manufacturer="opengear"))
for device in opengear:
    if device.device_type["manufacturer"]:
        print(80 * "#")
        print("This is a OpenGear")
        print(
            "\n"
            "Name:\t{devname}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}".format(
                devname=device.name,
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devmodel=device.device_type["model"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )
else:
    print("Cisco OpenGear found")

ubiquiti = list(nb.dcim.devices.filter(manufacturer="ubiquiti"))
for device in ubiquiti:
    if device.device_type["manufacturer"]:
        print(80 * "#")
        print("This is a Ubiquiti OS")
        print(
            "\n"
            "Name:\t{devname}"
            "\nManufacturer:\t{devmanufacturer}"
            "\nModel:\t{devmodel}"
            "\nOSversion:\t{devcustomfield}".format(
                devname=device.name,
                devmanufacturer=device.device_type["manufacturer"]["display"],
                devmodel=device.device_type["model"],
                devcustomfield=device.custom_fields["sw_version"],
            )
        )
else:
    print("Ubiquiti OS not found")
