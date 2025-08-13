import paramiko

HOST = "10.1.10.1"          # replace with your SSH server's IP
USER = "your_username"      # replace with your username
PASSWORD = "your_password"  # replace with your password
PORT = 22                   # or your custom SSH port

try:
  # create a new SSH client object
  client = paramiko.SSHClient()

  # set SSH key parameters to auto accept unknown hosts. (This should be removed in production)
  client.load_system_host_keys
  client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  # connect to host
  client.connect(HOST, port=PORT, username=USER, password=PASSWORD)

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