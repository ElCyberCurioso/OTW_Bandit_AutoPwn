import lib.json_manage as json_manage
import lib.check_modules as check_modules
import lib.utilities as utilities
import lib.constants as constants
import otw_bandit_autopwn as otw_bandit_autopwn

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

# Manage main menu
def main_menu():
    utilities.setup_signal_handlers() # Start exit handler
    utilities.clear_screen() # Clear screen before display menu
    
    utilities.show_banner()
    while True:
        json_manage.print_boxed("Main menu")
        print(constants.MAIN_MENU)
        key = get_key()
        if key == '1':
            utilities.clear_screen()
            utilities.print_table("user","password")
            hack_menu()
        elif key == '2':
            utilities.clear_screen()
            list_menu()
        elif key == '3':
            utilities.clear_screen()
            # utilities.print_table("user","password","temp_folder","notes")
            modify_menu()
        elif key == '4':
            utilities.clear_screen()
        elif key == '5':
            utilities.clear_screen()
            utilities.show_banner()
        elif key == '6':
            print("Goodbye!")
            break
        else:
            print(constants.INVALID_OPTION)

def hack_menu():
    while True:
        print(constants.HACK_MENU)
        key = get_key()
        if key == '1':
            utilities.hack_user()
            utilities.clear_screen()
        elif key == '2':
            utilities.clear_screen()
            break
        else:
            print(constants.INVALID_OPTION)

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

def modify_menu():
    while True:
        print(constants.MODIFY_MENU)
        key = get_key()
        if key == '1':
            utilities.clear_screen()
            utilities.update_password()
        elif key == '2':
            utilities.clear_screen()
            utilities.update_temp_folder()
        elif key == '3':
            utilities.clear_screen()
            utilities.update_notes()
        elif key == '4':
            utilities.clear_screen()
            list_menu()
        elif key == '5':
            utilities.clear_screen()
            break
        else:
            print(constants.INVALID_OPTION)

# if __name__ == "__main__":
    # check_modules.check_installed_modules()
    
    main_menu() # Start main menu