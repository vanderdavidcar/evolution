#!/usr/bin/env python
from napalm import get_network_driver
import json
import config_cloud


driver = get_network_driver("asa")
device = driver(hostname='BSL-VFW-ASA01',
                username= config_cloud.cloud_user,
                password= config_cloud.cloud_pwd)
                #optional_args={'port':22})

device.open()
facts = device.get_facts()
device.close

