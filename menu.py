import lib.json_manage as json_manage
import lib.check_modules as check_modules
import lib.utilities as utilities
import lib.menu_texts as menu_texts

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
    utilities.show_banner()
    while True:
        json_manage.print_boxed("Main menu")
        print(menu_texts.main_menu)
        key = get_key()
        if key == '1':
            utilities.clear_screen()
            utilities.print_table("user","password")
            hack_menu()
        elif key == '2':
            utilities.clear_screen()
            utilities.print_table("user","password","url","temp_folder","notes")
        elif key == '3':
            utilities.clear_screen()
            utilities.print_table("user","password","url","temp_folder","notes")
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
            print(menu_texts.invalid_option)

def hack_menu():
    while True:
        print(menu_texts.hack_menu)
        key = get_key()
        if key == '1':
            utilities.hack_user()
            utilities.clear_screen()
        elif key == '2':
            utilities.clear_screen()
            break
        else:
            print(menu_texts.invalid_option)

def modify_menu():
    while True:
        print(menu_texts.modify_menu)
        key = get_key()
        if key == '1':
            utilities.clear_screen()
            utilities.update_password()
            utilities.clear_screen()
        elif key == '2':
            utilities.clear_screen()
            utilities.update_temp_folder()
            utilities.clear_screen()
        elif key == '3':
            utilities.clear_screen()
            utilities.update_notes()
            utilities.clear_screen()
        elif key == '4':
            utilities.clear_screen()
            break
        else:
            print(menu_texts.invalid_option)

if __name__ == "__main__":
    # check_modules.check_installed_modules()
    utilities.setup_signal_handlers()
    utilities.clear_screen()
    main_menu()