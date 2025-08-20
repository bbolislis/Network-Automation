import re
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

command = 'show ip interface brief'
output = net_connect.send_command(command)

#Regular Expression to extract interface, IP address and status
regex = r'(\S+)\s+([\d.]+)\s+\S+\s+(up|down)\s+(up|down)'

#Find all mathces in the output
matches = re.findall(regex, output)

#Print the extracted information
for match in matches:
  interface, ip_address, protocol_status, admin_status = match
  print(f"Interface: {interface}, IP Address: {ip_address}, Admin Status: {admin_status}")

net_connect.disconnect()