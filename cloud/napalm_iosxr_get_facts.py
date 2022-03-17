#!/usr/bin/env python
from napalm import get_network_driver
import json
import config_cloud


driver = get_network_driver("iosxr")
device = driver(hostname='br-lp-spad06-rt-bgw02',
                username= config_cloud.cloud_username,
                password= config_cloud.cloud_password)
                #optional_args={'port':22})

device.open()
facts = device.get_interfaces()
device.close

