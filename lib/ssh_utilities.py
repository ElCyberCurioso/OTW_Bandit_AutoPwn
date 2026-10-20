import paramiko, time

import lib.constants as constants

def connect_ssh_with_retries(username, password, max_retries=5, retry_delay=5, pkey=None):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    retries = 0
    while True:
        try:
            if pkey:
                client.connect(hostname=constants.OTW_BANDIT_SSH_URL, port=constants.OTW_BANDIT_SSH_PORT, username=username, password=password, pkey=pkey, banner_timeout=10)
                return client
            else:
                client.connect(hostname=constants.OTW_BANDIT_SSH_URL, port=constants.OTW_BANDIT_SSH_PORT, username=username, password=password, banner_timeout=10)
                return client
            
        except (paramiko.ssh_exception.SSHException, ConnectionResetError):
            print("[!] Error while connecting")
            retries += 1
            if retries >= max_retries:
                print("[!] Max retries reached. Aborting...")
                raise
            print(f"[*] Retry in {retry_delay} seconds... (Retry {retries}/{max_retries})")
            time.sleep(retry_delay)

# Manage to open ssh connection with password or sshkey file and retrieve a client object with the successful connection
def ssh_connection(username, password):
    client = connect_ssh_with_retries(username, password)
    return client

# Manage to open ssh connection with an sshkey and retrieve a client object with the successful connection
def ssh_connection_sshkey(username, pkey):
    client = connect_ssh_with_retries(username, "", pkey=pkey)
    return client

# Run a command on an open client and return its stdout, stripped.
# stdout.read() blocks until the command finishes (EOF), so this also
# serves as "wait until command completes" when the output is unused.
def run(client, command):
    _, stdout, _ = client.exec_command(command)
    return stdout.read().decode().strip()

# Drain an interactive shell channel for up to `timeout` seconds and
# return everything received.
def read_channel(channel, timeout=5):
    output = ""
    start_time = time.time()
    while time.time() - start_time <= timeout:
        if channel.recv_ready():
            output += channel.recv(1024).decode(errors="ignore")
        time.sleep(0.2)
    return output
