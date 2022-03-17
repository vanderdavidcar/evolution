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

vcloud = nb.dcim.devices.filter(tenant="vcloud", status="active")
for display in vcloud:
    print(display.name, display.status)

custom_fields = nb.dcim.devices.filter(custom_fields="cpu")
for display in custom_fields:
    print(display.name, display.custom_fields)

platform = nb.dcim.devices.filter(manufacturer="fortinet")
for display in platform:
    print(display.name, display.device_type, display.custom_fields)
    #display = nb.dcim.devices.update({"sw_version": "FortiOS"})


#devices = list(nb.dcim.devices.filter(role='spine-osp'))