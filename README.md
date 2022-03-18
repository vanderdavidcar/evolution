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


# Note:
I need more concepts about class and functions to create pystest file.
