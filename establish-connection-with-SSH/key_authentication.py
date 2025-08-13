import paramiko

HOST = "192.168.1.100"    # replace with your SSH server's IP
USER = "your_username"    # replace with your username
PORT = 22
PRIVATE_KEY_PATH = "~/.ssh/authorized_keys"   # replace with the path to your private key

try:
  client = paramiko.SSHClient()
  client.load_system_host_keys()
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())    # remove in production

  # load the private key
  private_key = paramiko.RSAKey.from_private_key_file(PRIVATE_KEY_PATH)

  # connect to the host using the private key
  client.connect(HOST, port=PORT, username=USER, pkey=private_key)

  # execute a command
  stdin, stdout, stderr = client.exec_command("show version")

  # read the output
  output = stdout.read().decode()
  print(output)

  # check for errors
  errors = stderr.read().decode()
  if errors:
    print(f"Errors: {errors}")

except Exception as e:
  print(f"An error occurred: {e}")
finally:
  if 'client' in locals():
    client.close()
