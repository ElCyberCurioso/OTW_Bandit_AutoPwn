from sys import exit

import lib.constants as constants
import lib.exploitation_chain as ec
import lib.data_utilities as data_utilities
import lib.export_utilities as export_utilities

import signal, os, base64, time

# Script exit handler
def exit_handler(sig=None, frame=None):
    # Handle any cleanup here
    print(f"\n{constants.EXITING}")
    exit(0)

# Setup exit handler
def setup_signal_handlers():
    signal.signal(signal.SIGINT, exit_handler)  # Ctrl+C
    signal.signal(signal.SIGTERM, exit_handler) # kill

# Cleans screen after an action
def clear_screen():
    if os.name == "nt": # Windows
        os.system("cls")
    else: # Linux
        os.system("clear")

# Menu to select user and gets all users (to print them), and other parameters
def select_user(fields, show_list_table=True, cols=3):
    if show_list_table: # If want to show data in list format (with commas)
        # Show user besides other fields
        print_list(cols, fields)
    else: # If want to show data in data in tables (pandas markdown tables)
        print_table(fields)
        
    users = constants.BANDIT_USERS[1:] # Getting users to validate user's input, but not including bandit0
    while True:
        choice = input("\nIndicate a user or 'all' (type 'back' to return): ").strip().lower()
        if choice == "back":
            return None
        if choice == "all":
            return users
        if choice in users:
            return choice
        print(constants.INVALID_USER)

# Update password of a user
def update_password(fields):
    columns_to_show = 3 # In how many columns wrap results
    user = select_user(fields, cols=columns_to_show)
    if user:
        new_pass = input(f"Enter new password for {user}: ").strip()
        data_utilities.update_info_for_user(user, new_password=new_pass)
     
# Update temp folder of a user
def update_temp_folder(fields):
    columns_to_show = 3 # In how many columns wrap results
    user = select_user(fields, cols=columns_to_show)
    if user:
        new_temp_folder = input(f"Enter temp folder for {user}: ").strip()
        data_utilities.update_info_for_user(user, new_temp_folder=new_temp_folder)

# Update notes of a user
def update_notes(fields):
    columns_to_show = 3 # In how many columns wrap results
    user = select_user(fields, cols=columns_to_show)
    if user:
        new_notes = input(f"Enter notes for {user}: ").strip()
        data_utilities.update_info_for_user(user, new_notes=new_notes)

# Update sshkey of a user
def update_sshkey(fields):
    columns_to_show = 3 # In how many columns wrap results
    user = select_user(fields, cols=columns_to_show)
    if user:
        sshkey_file = input(f"Enter sshkey (file path) for {user}: \n").strip()
        if os.path.isfile(sshkey_file): # If file exists
            data_utilities.update_info_for_user(user, new_sshkey=sshkey_file)

# Delete field of a user
def delete_field(fields_to_show, fields_to_delete):
    columns_to_show = 3 # In how many columns wrap results
    user = select_user(fields_to_show, cols=columns_to_show)
    if user:
        if user == constants.BANDIT_USERS[1:]: # All users
            data_utilities.delete_all_info_for_users(fields_to_delete)
        else:
            data_utilities.delete_info_for_user(user, fields_to_delete)

# Export to PDF or Excel info
def export_fields(fields, filename, is_pdf, is_excel):
    users = select_user(fields,show_list_table=False)
    if users:
        export_utilities.export(fields, filename, users, is_pdf, is_excel)

# Action pending to implement
def hack_user():
    user = select_user(["user","password"])
    if user:
        ec.main(user)

# Print banner
def show_banner():
    print(constants.BANNER)

# Print as pandas table
def print_table(fields, users=None):
    data_utilities.get_custom_data_json(as_list=False, is_print=True, is_markdown=True, fields=fields, users=users)
    
# Print as list
def print_list(cols, fields, users=None):
    data_utilities.get_custom_data_json(cols, as_list=True, is_print=True, fields=fields, users=users)

# Check if user exists
def validate_user(user):
    if user not in constants.BANDIT_USERS:
        print(f"Invalid user: {user}")
        exit(0)

# Get base64 text of file content
def get_b64_file_content(file_path):
    file = open(file_path, "r")
    b64_sshkey = base64.b64encode(file.read().encode("ascii"))
    file.close()
    return b64_sshkey.decode("ascii")

def get_export_menu_fields():
    # Insert all fields into export menu
    position = 3
    items1 = constants.EXPORT_MENU
    items2 = constants.ARRAY_ALL_FIELDS
    items = items1[:position] + items2 + items1[position:]
    return items

def count_elements(variable):
    if isinstance(variable, str):
        return 1
    try:
        return len(variable)
    except TypeError:
        return 1  # In case is not iterable or string