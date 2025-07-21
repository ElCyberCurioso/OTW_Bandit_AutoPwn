import lib.utilities as utilities
import lib.constants as constants
import lib.data_utilities as data_utilities

import os

# Menu input handler
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

# Method that handles MAIN menu
def main_menu():
    utilities.setup_signal_handlers() # Start exit handler
    utilities.clear_screen() # Clear screen before display menu
    
    utilities.show_banner()
    while True:
        data_utilities.print_boxed("Main menu")
        print(constants.MAIN_MENU)
        key = get_key()
        if key == '1':
            utilities.clear_screen()
            hack_menu()
        elif key == '2':
            utilities.clear_screen()
            list_menu()
        elif key == '3':
            utilities.clear_screen()
            edit_menu()
        elif key == '4':
            utilities.clear_screen()
            delete_menu()
        elif key == '5':
            utilities.clear_screen()
        elif key == '6':
            utilities.clear_screen()
            utilities.show_banner()
        elif key == '7':
            print("👋​ See you next time!​")
            break
        else:
            print(constants.INVALID_OPTION)

# Method that handles HACK menu
def hack_menu():
    while True:
        print(constants.HACK_MENU)
        key = get_key()
        if key == '1':
            utilities.hack_user()
        elif key == '2':
            utilities.clear_screen()
            break
        else:
            print(constants.INVALID_OPTION)

# Method that handles LIST menu
def list_menu():
    while True:
        print(constants.LIST_MENU)
        key = get_key()
        if key == '1':
            utilities.clear_screen()
            utilities.print_table("user","password","temp_folder")
        elif key == '2':
            utilities.clear_screen()
            utilities.print_table("user","details","url")
        elif key == '3':
            utilities.clear_screen()
            utilities.print_table("user","notes")
        elif key == '4':
            utilities.clear_screen()
            utilities.print_table("user","tags")
        elif key == '5':
            utilities.clear_screen()
            break
        else:
            print(constants.INVALID_OPTION)

# Method that handles EDIT menu
def edit_menu():
    while True:
        print(constants.EDIT_MENU)
        key = get_key()
        if key == '1':
            utilities.clear_screen()
            utilities.update_password(["user","password"])
        elif key == '2':
            utilities.clear_screen()
            utilities.update_temp_folder(["user","temp_folder"])
        elif key == '3':
            utilities.clear_screen()
            utilities.update_notes(["user","notes"])
        elif key == '4':
            utilities.clear_screen()
            utilities.update_sshkey(["user","sshkey"])
        elif key == '5':
            utilities.clear_screen()
            list_menu()
        elif key == '6':
            utilities.clear_screen()
            break
        else:
            print(constants.INVALID_OPTION)
            
# Method that handles DELETE menu
def delete_menu():
    while True:
        print(constants.DELETE_MENU)
        key = get_key()
        if key == '1':
            utilities.clear_screen()
            utilities.delete_field(["password"])
        elif key == '2':
            utilities.clear_screen()
            utilities.delete_field(["temp_folder"])
        elif key == '3':
            utilities.clear_screen()
            utilities.delete_field(["notes"])
        elif key == '4':
            utilities.clear_screen()
            utilities.delete_field(["sshkey"])
        elif key == '5':
            utilities.clear_screen()
            break
        else:
            print(constants.INVALID_OPTION)
