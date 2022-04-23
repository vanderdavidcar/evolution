# Netbox using Pynetbox

Following the instructions below:


# Dependencies:

Install the requirements to install all dependencies:

$ pip install -r requirements.txt


# Endpoint
I set up netbox-docker and use eve-ng to emulate environment and tested with link "https://demo.netbox.dev/" 
If necessary, change that for another one.


# Authentication:

Put api token, URL, username and password informations into variables in config.py file.

api_key = ""
nb_username = ""
nb_password = ""
nb_url = ""


# IP/FQDN - DNS

I used WSL (Windows Subsystem Linux) to tests all codes, so access by SSH was done with FQDN, all devices needed into /etc/hosts, because my code searching for models e.g (c9200-48p, isr1111) create a python list and connect via SSH for DNS name.

To avoid the error below, please make sure you have a DNS of devices in /etc/hosts

    raise NetmikoTimeoutException(msg)
netmiko.ssh_exception.NetmikoTimeoutException: DNS failure--the hostname you provided was not resolvable in DNS: dmi01-akron-rtr01:22


# Exercises:

4 - Collect information for devices with Status = Active, Tenant = NOC in Netbox Doing a loop to find Status = Active, Tenant = NOC in Netbox
  Using file collect_status.py  
  
5 - Information to collect: software version Custom field to update: "sw_version" Assume network device list would contain Cisco Catalyst IOS
    For this porpose use update_sw_versions.py.

I did with Napalm and Netmiko, there is a version in NETMIKO update_sw_version.py if you want to update "custom fields | sw_version" ou only clear that field input "yes" or "no". If choose "yes" the program is take that version and put on custom fields if "no" the program will clean all devices custom fields.
 
Using files update_nxos_custfields.py, update_ios_custfields.py and update_iosxr_custfields.py
For your testing change the model in line 34 like (c9200-48p, isr1111), but regex created in this environment was only (IOS, NXOS and IOSXR)

e.g: 
ios_model = list(nb.dcim.devices.filter(model="catalyst-2960"))
nxos_model = list(nb.dcim.devices.filter(model="nexus-9300"))
iosxr_model = list(nb.dcim.devices.filter(model="ios-xr"))

# Pytest:
Created test_model.py and parse_model.py that have a regex of versions
