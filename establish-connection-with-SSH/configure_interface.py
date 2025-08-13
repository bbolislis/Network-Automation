import paramiko

HOST = "192.168.1.100"  # replace with your SSH server's IP
USER = "your_username"  # replace with your username
PASSWORD = "your_password"  # replace with your password
PORT = 22
INTERFACE = "GigabitEthernet0/1"
IP_ADDRESS = "192.168.2.10"
NETMASK = "255.255.255.0"

try:
  client = paramiko.SSHClient()
  client.load_system_host_keys()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # remove in production
  client.connect(HOST, port=PORT, username=USER, password=PASSWORD)

  # create an interactive shell session
  channel = client.invoke_shell()

  # define the configuration commands
  commands = [
    "enable",
    "your_enable_password", # replace with your enable password
    "configure terminal",
    f"interface {INTERFACE}",
    f"ip adddress {IP_ADDRESS} {NETMASK}",
    "no shutdown",
    "end",
    "exit"
  ]

  # send the commands to the device
  for command in commands:
    channel.send(command + "\n")
    # wait for the command to execute (adjust sleep time as needed)
    import time
    time.sleep(0.5)
    # print the output (optional)
    output = channel.recv(65535).decode()
    print(output)

  # close the connection
  channel.close()

except Exception as e:
  print(f"An error occurred: {e}")
finally:
  if 'client' in locals():
    client.close()