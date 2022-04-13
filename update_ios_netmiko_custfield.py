from netmiko import ConnectHandler
import pynetbox
import re
import config
import urllib3

urllib3.disable_warnings()


"""
1 - Access the Netbox Demo
"""
NETBOX_URL = config.nb_url

"""
2 - Get API Token on Netbox
"""
NETBOX_TOKEN = config.api_key

"""
3 - Insted of Postman I'm using Pynetbox to send GET and take
informations from devices
"""
nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False

"""
5 - Information to collect: software version
Custom field to update: "sw_version"
Assume network device list would contain Cisco Catalyst IOS
"""
# List of devices vendors "NXOS"
ios_model = list(nb.dcim.devices.filter(model="iol"))
print(ios_model)

for devices in ios_model:
    print('Connecting to device" ' + str(devices))
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': str(devices),
        'username': config.nb_username,
        'password': config.nb_password
    }
    net_connect = ConnectHandler(**ios_device)
    sh_ver = net_connect.send_command('show version')

    version_pattern = re.compile(r'Version (?P<version>\S........)')
    ios_version = version_pattern.search(sh_ver)

    # Print regex information collect ina file ios_version.txt
    print("IOS Version regex: ".ljust(18) + ios_version.group("version"))
    version = ios_version.group("version")
    print(version)

    # Retrieve router object for update with dictionary
    for devices in ios_model:
        # Update custom fields "sw_version" using regex information collected
        dict(devices)['custom_fields']["sw_version"] = version
        devices.save()
        break

    print("Current serial number: ", devices.name)
    print("Device Type: ", devices.device_type)
    print("sw_version: ", devices.custom_fields["sw_version"])
    print("Current tenant: ", devices.tenant)
    