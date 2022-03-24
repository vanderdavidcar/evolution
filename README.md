# Evolution Lab - Netbox using Pynetbox and Napalm

Following the instructions below:


# Dependencies:

Install the requirements to install all dependencies:

$ pip install -r requirements.txt


# Endpoint

NETBOX_URL = "https://demo.netbox.dev/"
If necessary, change that for another one, all my codes was tested in "https://netbox.int.flexcloud.com.br/"


# Authentication:

Put api token, username and password informations into variables in config.py file.

api_key = ""
nb_username = ""
nb_password = ""


# IP/FQDN

For files update_nxos_custfields.py, update_ios_custfields.py and update_iosxr_custfields.py, put IP Address or FQDN in lines 34 (hostname="") and 51 (name="").

# Exercises:

4 - Collect information for devices with Status = Active, Tenant = NOC in Netbox Doing a loop to find Status = Active, Tenant = NOC in Netbox
  Using file collect_status.py

5 - Information to collect: software version Custom field to update: "sw_version" Assume network device list would contain Cisco Catalyst IOS
  Using files update_nxos_custfields.py, update_ios_custfields.py and update_iosxr_custfields.py


#  # Note:

I need more concepts about class and functions to create pytest file to works properly. So the files start with test_* name doesn't work from pytest.

