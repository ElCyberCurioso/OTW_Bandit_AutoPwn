import paramiko, time

import lib.constants as constants

def connect_ssh_with_retries(username, password, max_retries=5, retry_delay=5, pkey=None):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    retries = 0
    while True:
        try:
            if pkey:
                client.connect(hostname=constants.OTW_BANDIT_SSH_URL, port=constants.OTW_BANDIT_SSH_PORT, username=username, password=password, pkey=pkey, timeout=10)
                return client
            else:
                client.connect(hostname=constants.OTW_BANDIT_SSH_URL, port=constants.OTW_BANDIT_SSH_PORT, username=username, password=password, timeout=10)
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
