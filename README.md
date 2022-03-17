# evolution Lab - Netbox using Pynetbox and Napalm

I couldn't access the demonetbox using user/pass: admin, so I tested my codes in another environment. For this reason testing my codes following the instructions below:

1 - Put api token, username and password informations into variables in config.py

api_key = ""
nb_username = ""
nb_password = ""

2 - In my environment has only cisco devices so I created NXOS and IOS sw_version updates and works fine. So for the codes update_ios_custfields.py and update_nxos_custfields.py put IP Address in hostname variable, and the code will works properly.

Note:
I need more concepts about class and functions to create pystest file.
I did my best!
