import lib.json_manage as json_manage

from signal import signal, SIGINT
from sys import exit

def handler(signal_received, frame):
    # Handle any cleanup here
    print('\n\nExiting...')
    exit(0)

def select_user():
    df = json_manage.get_custom_data_json(as_list=False, is_print=False, fields=["user"])
    users = df['user'].to_list()
    while True:
        choice = input("Indicate user (or type 'back' to return): ").strip()
        if choice.lower() == 'back':
            return None
        if choice in users:
            return choice
        print("Invalid user, please try again!")

def update_password():
    user = select_user()
    if user:
        new_pass = input(f"Enter new password for {user}: ").strip()
        json_manage.update_info_for_user(user, new_password=new_pass)
        
def update_temp_folder():
    user = select_user()
    if user:
        new_temp_folder = input(f"Enter temp folder for {user}: ").strip()
        json_manage.update_info_for_user(user, new_temp_folder=new_temp_folder)

def update_notes():
    user = select_user()
    if user:
        new_notes = input(f"Enter notes for {user}: ").strip()
        json_manage.update_info_for_user(user, new_notes=new_notes)
        
def hack_user():
    user = select_user()
    if user:
        print(f"[*] Simulating hack for {user}... (Here should be your hack logic)")

def show_banner():
    font = """
   ___                _____ _        __        ___          
  / _ \__   _____ _ _|_   _| |__   __\ \      / (_)_ __ ___ 
 | | | \ \ / / _ \ '__|| | | '_ \ / _ \ \ /\ / /| | '__/ _ \\
 | |_| |\ V /  __/ |   | | | | | |  __/\ V  V / | | | |  __/
  \___/  \_/ \___|_|   |_| |_| |_|\___| \_/\_/  |_|_|  \___|
  ____                  _ _ _                               
 | __ )  __ _ _ __   __| (_) |_                             
 |  _ \ / _` | '_ \ / _` | | __|                            
 | |_) | (_| | | | | (_| | | |_                             
 |____/ \__,_|_| |_|\__,_|_|\__|                            
     _         _        ______        ___   _               
    / \  _   _| |_ ___ |  _ \ \      / / \ | |              
   / _ \| | | | __/ _ \| |_) \ \ /\ / /|  \| |              
  / ___ \ |_| | || (_) |  __/ \ V  V / | |\  |              
 /_/   \_\__,_|\__\___/|_|     \_/\_/  |_| \_|              
                                                            
"""
    print(font)

def main_menu():
    show_banner()
    while True:
        print("""
--- Main Menu ---
1. Hack bandit user
2. List info
3. Modify info
4. Show banner
5. Exit
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            hack_menu()
        elif choice == '2':
            json_manage.get_custom_data_json(as_list=False, is_print=True, is_markdown=True, fields=["user","password","url","temp_folder","notes"])
        elif choice == '3':
            modify_menu()
        elif choice == '4':
            show_banner()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

def hack_menu():
    while True:
        print("""
--- Hack Menu ---
1. Indicate user to hack
2. Back
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            hack_user()
        elif choice == '2':
            break
        else:
            print("Invalid option.")

def modify_menu():
    while True:
        print("""
--- Modify Info Menu ---
1. Update password
2. Indicate temp folder
3. Insert notes
4. Back
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            update_password()
        elif choice == '2':
            update_temp_folder()
        elif choice == '3':
            update_notes()
        elif choice == '4':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    signal(SIGINT, handler)
    main_menu()