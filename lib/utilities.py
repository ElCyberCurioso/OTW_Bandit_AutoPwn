from sys import exit

import lib.constants as constants
import lib.exploitation_chain as ec
import lib.data_utilities as data_utilities

import signal, os, base64

# Script exit handler
def exit_handler(sig=None, frame=None):
    # Handle any cleanup here
    print('\nExiting...')
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
def select_user(*fields, show_list_table=True):
    if show_list_table: # If want to show data in list format (with commas)
        print_list(*fields)
    else: # If want to show data in data in tables (pandas markdown tables)
        print_table(*fields)
        
    users = constants.BANDIT_USERS # Getting users to validate user's input
    while True:
        choice = input("\nIndicate user (or type 'back' to return): ").strip()
        if choice.lower() == 'back':
            return None
        if choice in users:
            return choice
        print(constants.INVALID_USER)

# Update password of a user
def update_password(fields):
    user = select_user(fields)
    if user:
        new_pass = input(f"Enter new password for {user}: ").strip()
        data_utilities.update_info_for_user(user, new_password=new_pass)
     
# Update temp folder of a user
def update_temp_folder(fields):
    user = select_user(fields)
    if user:
        new_temp_folder = input(f"Enter temp folder for {user}: ").strip()
        data_utilities.update_info_for_user(user, new_temp_folder=new_temp_folder)

# Update notes of a user
def update_notes(fields):
    user = select_user(fields)
    if user:
        new_notes = input(f"Enter notes for {user}: ").strip()
        data_utilities.update_info_for_user(user, new_notes=new_notes)

# Update sshkey of a user
def update_sshkey(fields):
    user = select_user(fields)
    if user:
        sshkey_file = input(f"Enter sshkey (file path) for {user}: \n").strip()
        if os.path.isfile(sshkey_file): # If file exists
            data_utilities.update_info_for_user(user, new_sshkey=sshkey_file)

# Delete field of a user
def delete_field(field):
    user = select_user("user", field)
    if user:
        data_utilities.delete_info_for_user(user, field)        

# Action pending to implement
def hack_user():
    user = select_user("user","password","temp_folder","notes", show_list_table=False)
    if user:
        ec.main(user)

# Print banner
def show_banner():
    print(constants.BANNER)

# Print as pandas table
def print_table(*fields, user=None):
    data_utilities.get_custom_data_json(as_list=False, is_print=True, is_markdown=True, fields=fields, user=user)
    
# Print as list
def print_list(*fields, user=None):
    data_utilities.get_custom_data_json(as_list=True, is_print=True, fields=fields, user=user)

# Check if user exists
def validate_user(user):
    if user not in constants.BANDIT_USERS:
        print(f"❌ Invalid user: {user}")
        exit(0)

# Get base64 text of file content
def get_b64_file_content(file_path):
    file = open(file_path, "r")
    b64_sshkey = base64.b64encode(file.read().encode("ascii"))
    file.close()
    return b64_sshkey.decode("ascii")
