from netmiko import ConnectHandler

device = {
  'device_type': 'cisco_ios',
  'host': '192.168.1.10',
  'username': 'your_username',
  'password': 'your_password',
}

commands = [
  'show version',
  'show ip interface brief',
  'show running-config',
]

try:
  net_connect = ConnectHandler(**device)
  for command in commands:
    output = net_connect.send_command(command)
    print(f"Output of '{command}':\n{output}\n")
  net_connect.disconnect()

except Exception as e:
  print(f"An error occurred: {e}")
