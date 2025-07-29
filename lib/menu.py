import time

import lib.constants as constants
import lib.config as config
import lib.utilities as utilities

# Method that handles LIST menu
def list_menu():
    list_menu, list_menu_back = config.list_menu_config()
    
    while not list_menu_back:
        list_sel = list_menu.show()
        if list_sel:
            utilities.print_table(list_menu.chosen_menu_entries)
        else:
            list_menu_back = True
            print(constants.BACK_TO_MAIN_MENU)

# Method that handles EDIT menu
def edit_menu():
    edit_menu, edit_menu_back = config.edit_menu_config()
    
    while not edit_menu_back:
        edit_sel = edit_menu.show()
        if edit_sel == 0:
            select_user_menu(utilities.update_password, constants.EDIT_DELETE_USER_ACTION, constants.EDIT_MENU[edit_sel], ["user","password"])
        elif edit_sel == 1:
            select_user_menu(utilities.update_temp_folder, constants.EDIT_DELETE_USER_ACTION, constants.EDIT_MENU[edit_sel], ["user","temp_folder"])
        elif edit_sel == 2:
            select_user_menu(utilities.update_notes, constants.EDIT_DELETE_USER_ACTION, constants.EDIT_MENU[edit_sel], ["user","notes"])
        elif edit_sel == 3:
            select_user_menu(utilities.update_sshkey, constants.EDIT_DELETE_USER_ACTION, constants.EDIT_MENU[edit_sel], ["user","sshkey"])
        elif edit_sel == 4:
            list_menu()
        elif edit_sel == 5 or edit_sel == None:
            # Return to main menu
            edit_menu_back = True
            print(constants.BACK_TO_MAIN_MENU)
    edit_menu_back = False

# Method that handles DELETE menu
def delete_menu():
    delete_menu, delete_menu_back = config.delete_menu_config()
    
    while not delete_menu_back:
        delete_sel = delete_menu.show()
        if delete_sel == 0:
            select_user_menu(utilities.delete_field, constants.EDIT_DELETE_USER_ACTION, constants.DELETE_MENU[delete_sel], ["user","password"], ["password"])
        elif delete_sel == 1:
            select_user_menu(utilities.delete_field, constants.EDIT_DELETE_USER_ACTION, constants.DELETE_MENU[delete_sel], ["user","temp_folder"], ["temp_folder"])
        elif delete_sel == 2:
            select_user_menu(utilities.delete_field, constants.EDIT_DELETE_USER_ACTION, constants.DELETE_MENU[delete_sel], ["user","notes"], ["notes"])
        elif delete_sel == 3:
            select_user_menu(utilities.delete_field, constants.EDIT_DELETE_USER_ACTION, constants.DELETE_MENU[delete_sel], ["user","sshkey"], ["sshkey"])
        elif delete_sel == 4 or delete_sel == None:
            # Return to main menu
            delete_menu_back = True
            print(constants.BACK_TO_MAIN_MENU)
    delete_menu_back = False

# Method that handles EXPORT menu
def export_menu():
    is_pdf = False
    is_excel = False
    
    export_menu, export_menu_back = config.export_menu_config()
    
    while not export_menu_back:
        export_sel = export_menu.show()
        if export_sel:
            fields_map = dict(zip(export_sel, export_menu.chosen_menu_entries))
            
            if [valor for clave, valor in fields_map.items() if clave == 0]:
                is_pdf = True
            if [valor for clave, valor in fields_map.items() if clave == 1]:
                is_excel = True
            
            # Recover selected fields to print
            result = [valor for clave, valor in fields_map.items() if clave not in (0, 1)]
            
            filename = input("Indicate filename of resultant file/files (type 'back' to return): ").strip().lower()
            if filename == "back":
                # Return to main menu
                export_menu_back = True 
                print(constants.BACK_TO_MAIN_MENU)
                return None
            
            # Proceeds to generate files
            utilities.export_fields(result, filename, is_pdf, is_excel)
            time.sleep(2.5) # To let user read action message
            
            # Return to main menu
            export_menu_back = True 
            print(constants.BACK_TO_MAIN_MENU)
        else:
            export_menu_back = True
            print(constants.BACK_TO_MAIN_MENU)

# Method that handles SELECT USER menu
def select_user_menu(next_action, next_text, next_title, *next_parameters):
    select_user_menu, select_user_menu_back = config.select_user_menu_config(next_text, next_title)
    
    while not select_user_menu_back:
        select_user_sel = select_user_menu.show()
        if select_user_sel == 0:
            next_action(*next_parameters)
            
            # Return to main menu
            select_user_menu_back = True 
            print(constants.BACK_TO_MAIN_MENU)
        elif select_user_sel == 1 or select_user_sel == None:
            # Return to main menu
            select_user_menu_back = True
            print(constants.BACK_TO_MAIN_MENU)
    select_user_menu_back = False
    
# Method that handles MAIN menu
def menu():
    # Recover menu's config
    main_menu, main_menu_exit = config.main_menu_config()
    
    while not main_menu_exit:
        main_sel = main_menu.show()

        # Hack Menu option
        if main_sel == 0:
            select_user_menu(utilities.hack_user, constants.HACK_USER_ACTION, constants.MAIN_MENU[main_sel])
        
        # List Menu option
        elif main_sel == 1:
            list_menu()
        
        # Edit Menu option
        elif main_sel == 2:
            edit_menu()
        
        # Delete Menu option
        elif main_sel == 3:
            delete_menu()
        
        # Export Menu option
        elif main_sel == 4:
            export_menu()
        
        # Exiting option
        elif main_sel == 5 or main_sel == None:
            main_menu_exit = True
            print("See you soon! 👋")
            