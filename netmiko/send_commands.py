from netmiko import ConnectHandler

device = {
  'device_type': 'cisco_ios',
  'host': '192.168.1.1',
  'username': 'your_username',
  'password': 'your_password',
  'secret': 'your_enable_secret',
}

try:
  net_connect = ConnectHandler(**device)
  print("Successfully connected to the device.")
except Exception as e:
  print(f"Failed to connect to the device: {e}")
  exit()

#Send configuration commands to network devices
config_commands = [
  'interface loopback 100',
  'description NETMIKO_TEST',
  'ip address 192.168.100.1 255.255.255.0',
]

output = net_connect.send_config_set(config_commands)
print(output)

net_connect.disconnect()

'''
  Important Considerations:

    Enable Mode: If your device requires you to enter enable mode before executing configuration commands, you can specify the secret parameter in the device dictionary. Netmiko will automatically enter enable mode before sending the configuration commands.
    Configuration Rollback: When making configuration changes, it's always a good idea to have a rollback plan in case something goes wrong. Netmiko doesn't provide built-in rollback functionality, so you'll need to implement your own rollback mechanism. This could involve saving the current configuration before making changes and then restoring the saved configuration if necessary.
'''