# Evolution Lab - Netbox using Pynetbox and Napalm

Following the instructions below:


# Dependencies:

Install the requirements to install all dependecies:

$ pip install -r requirements.txt



# Authentication:

Put api token, username and password informations into variables in config.py file.

api_key = ""
nb_username = ""
nb_password = ""


# IP/FQDN

For files update_nxos_custfields.py and, put IP Address or FQDN in hostname variable, and the code will works properly.

update_nxos_custfields.py
Line 34, put IP/FQDN in hostname

update_ios_custfields.py
Line 34, put IP/FQDN in hostname


# Note:
I need more concepts about class and functions to create pystest file.
