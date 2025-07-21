import time

import lib.constants as constants
import lib.ssh_utilities as ssh_utilities

# Manage to clone a git repo into a temp folder
def git_clone_repo_bandit(client, temp_dir, repo_url, current_password):
    channel = client.invoke_shell()
    time.sleep(1)

    channel.send("id\n")
    time.sleep(1)

    channel.send("whoami\n")
    time.sleep(1)
    
    channel.send("GIT_SSH_COMMAND=\"ssh -o StrictHostKeyChecking=no\" git clone " + repo_url + " " + temp_dir + "\n")
    time.sleep(1)
    
    channel.send(current_password + "\n")
    time.sleep(1)

    # Read buffer output
    output = ""
    start_time = time.time()
    while True:
        if channel.recv_ready():
            output += channel.recv(1024).decode(errors="ignore")
        if time.time() - start_time > 5:  # Wait 5 seconds
            break
        time.sleep(0.2)

    # Close connection
    channel.send("exit\n")

# Generate a temp folder using bandit0 credentials and giving full permissions to all users
def make_temp_directory(existing_client=None):
    if not existing_client:
        client = ssh_utilities.ssh_connection(constants.DEFAULT_USER, constants.DEFAULT_PASSWORD)
    else:
        client = existing_client
    
    _, stdout, _ = client.exec_command("mktemp -d")
    temp_dir = stdout.read().decode().strip()
    _, stdout, _ = client.exec_command("chmod 777 " + temp_dir)
    return temp_dir

# Clean a temp directory using an open session
def clean_temp_directory(client, temp_dir):
    _, _, _ = client.exec_command("rm -rf " + temp_dir)

# Getting password of a bandit user using an open session
def get_current_password(client):
    _, stdout, _ = client.exec_command('whoami')
    current_user = stdout.read().decode().strip()
    _, stdout, _ = client.exec_command("cat /etc/bandit_pass/" + current_user)
    current_password = stdout.read().decode().strip()
    return current_password
