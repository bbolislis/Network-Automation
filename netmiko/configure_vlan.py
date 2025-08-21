from netmiko import ConnectHandler

device = {
  'device_type': 'cisco_ios',
  'host': '192.168.1.10',
  'username': 'your_username',
  'password': 'your_password',
  'secret': 'your_enable_secret',
}

vlan_id = '100'
vlan_name = 'Data'

config_commands = [
  f'vlan {vlan_id}',
  f'name {vlan_name}',
]

try:
  net_connect = ConnectHandler(**device)
  net_connect.enable()
  output = net_connect.send_config_set(config_commands)
  print(output)
  net_connect.disconnect()

except Exception as e:
  print(f"An error occurred: {e}")