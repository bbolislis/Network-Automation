from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException, SSHException
import socket

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
except NetmikoTimeoutException as e:
  print(f"Connection time out to device: {device['host']}")
except NetmikoAuthenticationException as e:
  print(f"Authentication failure on device: {device['host']}")
except SSHException as e:
  print(f"SSH error on device: {device['host']}")
except socket.error as e:
  print(f"Socket error on device: {device['host']}")
except Exception as e:
  print(f"An unexpected error occurred: {e}")
else:
  command = 'show_version'
  output = net_connect.send_command(command)
  print(output)
  net_connect.disconnect()