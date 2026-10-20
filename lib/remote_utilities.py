import time

import lib.constants as constants
import lib.data_utilities as data_utilities
import lib.ssh_utilities as ssh_utilities


# Manage to clone a git repo on the remote host into a temp folder (via interactive shell)
def git_clone_remote(client, temp_dir, repo_url, current_password):
    channel = client.invoke_shell()
    time.sleep(constants.SHELL_STEP_WAIT)

    channel.send("id\n")
    time.sleep(constants.SHELL_STEP_WAIT)

    channel.send("whoami\n")
    time.sleep(constants.SHELL_STEP_WAIT)

    channel.send("GIT_SSH_COMMAND=\"ssh -o StrictHostKeyChecking=no\" git clone " + repo_url + " " + temp_dir + "\n")
    time.sleep(constants.SHELL_STEP_WAIT)

    channel.send(current_password + "\n")
    time.sleep(constants.SHELL_STEP_WAIT)

    # Read buffer output
    ssh_utilities.read_channel(channel)

    # Close connection
    channel.send("exit\n")

# Generate a temp folder using bandit0 credentials and giving full permissions to all users
def make_temp_directory(user, existing_client=None, credentials_default=False):
    if not existing_client or credentials_default:
        client = ssh_utilities.ssh_connection(constants.DEFAULT_USER, constants.DEFAULT_PASSWORD)
    else:
        client = existing_client

    _, stdout, _ = client.exec_command("mktemp -d")
    temp_dir = stdout.read().decode().strip()
    _, stdout, _ = client.exec_command("chmod 777 " + temp_dir)

    data_utilities.update_info_for_user(user, is_automated=True, new_temp_folder=temp_dir)

    if not existing_client:
        client.close()
    return temp_dir

# Clean a temp directory using an open session
def clean_temp_directory(client, temp_dir):
    _, _, _ = client.exec_command("rm -rf " + temp_dir + "/*")

# Get temp directory from .json file if exists, else create it and save it to .json
def get_temp_directory(client, user):
    temp_dir = ""

    user_temp_folder = data_utilities.get_custom_data_json(users=user, fields=["temp_folder"])
    temp_dir = str(user_temp_folder[0])
    if temp_dir:
        # Check if folder exists
        _, stdout, _ = client.exec_command("ls " + temp_dir + " &>/dev/null && echo 'exists' || echo 'no exists'")
        result = stdout.read().decode().strip()

        if result == "no exists":
            temp_dir = make_temp_directory(user, existing_client=client)
    else:
        temp_dir = make_temp_directory(user, existing_client=client)

    clean_temp_directory(client, temp_dir)

    return temp_dir
