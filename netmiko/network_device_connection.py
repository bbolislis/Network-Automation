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