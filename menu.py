import lib.json_manage as json_manage
import lib.check_modules as check_modules
import os

from signal import signal, SIGINT
from sys import exit


def handler(signal_received, frame):
    # Handle any cleanup here
    print('\n\nExiting...')
    exit(0)

def menu_handler():
    if os.name == 'nt':
        import msvcrt
        def get_key():
            return msvcrt.getch().decode('utf-8')
    else:
        import tty
        import termios
        def get_key():
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def select_user(*fields):
    df = json_manage.get_custom_data_json(as_list=False, is_print=False, fields=fields)
    json_manage.get_custom_data_json(as_list=False, is_print=True, fields=fields, is_markdown=True)
    users = df['user'].to_list()
    while True:
        choice = input("\nIndicate user (or type 'back' to return): ").strip()
        if choice.lower() == 'back':
            return None
        if choice in users:
            return choice
        print("Invalid user, please try again!")

def update_password():
    user = select_user("user","password")
    if user:
        new_pass = input(f"Enter new password for {user}: ").strip()
        json_manage.update_info_for_user(user, new_password=new_pass)
        
def update_temp_folder():
    user = select_user("user","temp_folder")
    if user:
        new_temp_folder = input(f"Enter temp folder for {user}: ").strip()
        json_manage.update_info_for_user(user, new_temp_folder=new_temp_folder)

def update_notes():
    user = select_user("user","notes")
    if user:
        new_notes = input(f"Enter notes for {user}: ").strip()
        json_manage.update_info_for_user(user, new_notes=new_notes)
        
def hack_user():
    user = select_user("user","password","temp_folder","notes")
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
        json_manage.print_boxed("Main menu")
        print("""
1. Hack bandit user
2. List info
3. Modify info
4. Clean screen
5. Exit
""")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            json_manage.get_custom_data_json(as_list=False, is_print=True, is_markdown=True, fields=["user","password"])
            hack_menu()
        elif choice == '2':
            clear_screen()
            json_manage.get_custom_data_json(as_list=False, is_print=True, is_markdown=True, fields=["user","password","url","temp_folder","notes"])
        elif choice == '3':
            json_manage.get_custom_data_json(as_list=False, is_print=True, is_markdown=True, fields=["user","password","url","temp_folder","notes"])
            modify_menu()
        elif choice == '4':
            clear_screen()
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
            clear_screen()
        elif choice == '2':
            clear_screen()
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
            clear_screen()
        elif choice == '2':
            update_temp_folder()
            clear_screen()
        elif choice == '3':
            update_notes()
            clear_screen()
        elif choice == '4':
            clear_screen()
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    # check_modules.check_installed_modules()
    signal(SIGINT, handler)
    clear_screen()
    main_menu()