from sys import exit

import lib.json_manage as json_manage
import lib.constants as constants
import exploitation_chain as exploitation_chain

import signal, os

# Script exit handler
def exit_handler(sig=None, frame=None):
    # Handle any cleanup here
    print('\n\nExiting...')
    exit(0)

# Setup exit handler
def setup_signal_handlers():
    signal.signal(signal.SIGINT, exit_handler)  # Ctrl+C
    signal.signal(signal.SIGTERM, exit_handler) # kill

# Cleans screen after an action
def clear_screen():
    if os.name == 'nt': # Windows
        os.system('cls')
    else: # Linux
        os.system('clear')

# Menu to select user and gets all users (to print them), and other parameters
def select_user(*fields, show_table=False, show_list=True):
    df = json_manage.get_custom_data_json(as_list=False, is_print=False, fields=fields)
    
    if show_list: # If want to show data in list format (with commas)
        print_list(*fields)
    
    if show_table: # If want to show data in data in tables (pandas markdown tables)
        print_table(*fields)
        
    users = df['user'].to_list() # Getting users to validate user's input
    while True:
        choice = input("\nIndicate user (or type 'back' to return): ").strip()
        if choice.lower() == 'back':
            return None
        if choice in users:
            return choice
        print(constants.INVALID_USER)

# Update password of a user
def update_password():
    user = select_user("user","password")
    if user:
        new_pass = input(f"Enter new password for {user}: ").strip()
        json_manage.update_info_for_user(user, new_password=new_pass)
     
# Update temp folder of a user
def update_temp_folder():
    user = select_user("user","temp_folder")
    if user:
        new_temp_folder = input(f"Enter temp folder for {user}: ").strip()
        json_manage.update_info_for_user(user, new_temp_folder=new_temp_folder)

# Update notes of a user
def update_notes():
    user = select_user("user","notes")
    if user:
        new_notes = input(f"Enter notes for {user}: ").strip()
        json_manage.update_info_for_user(user, new_notes=new_notes)

# Action pending to implement
def hack_user():
    user = select_user("user","password","temp_folder","notes")
    if user:
        print(f"[*] Simulating hack for {user}... (Here should be your hack logic)")

# Print banner
def show_banner():
    print(constants.BANNER)

def print_table(*fields):
    json_manage.get_custom_data_json(as_list=False, is_print=True, is_markdown=True, fields=fields)

def print_list(*fields):
    json_manage.get_custom_data_json(as_list=True, is_print=True, fields=fields)

# Generate a temp folder using bandit0 credentials and giving full permissions to all users
def make_temp_directory():
    client = exploitation_chain.ssh_connection(constants.DEFAULT_USER, constants.DEFAULT_PASSWORD)
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
