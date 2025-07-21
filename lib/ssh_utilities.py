import paramiko, time

import lib.constants as constants

def wait_for_ssh_to_be_ready(host, port, timeout, retry_interval):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    retry_interval = float(retry_interval)
    timeout = int(timeout)
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        time.sleep(retry_interval)
        try:
            client.connect(host, int(port), allow_agent=False,
                           look_for_keys=False)
        except paramiko.ssh_exception.SSHException as e:
            # socket is open, but not SSH service responded
            if e.message == 'Error reading SSH protocol banner':
                print(e)
                continue
            print('SSH transport is available!')
            break
        except paramiko.ssh_exception.NoValidConnectionsError as e:
            print('SSH transport is not ready...')
            continue

# Manage to open ssh connection with password or sshkey file and retrieve a client object with the successful connection
def ssh_connection(username, password):
    client = paramiko.SSHClient()
    
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()

    client.connect(hostname=constants.OTW_BANDIT_SSH_URL, port=constants.OTW_BANDIT_SSH_PORT, username=username, password=password)

    return client

# Manage to open ssh connection with an sshkey and retrieve a client object with the successful connection
def ssh_connection_sshkey(username, pkey):
    client = paramiko.SSHClient()
    
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()

    client.connect(hostname=constants.OTW_BANDIT_SSH_URL, port=constants.OTW_BANDIT_SSH_PORT, username=username, password="", pkey=pkey)

    return client
