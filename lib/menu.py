import lib.constants as constants
import lib.config as config
import lib.utilities as utilities

# Method that handles HACK menu
def hack_menu():
    hack_menu, hack_menu_back = config.hack_menu_config()
    
    while not hack_menu_back:
        hack_sel = hack_menu.show()
        if hack_sel == 0:
            utilities.hack_user()
        elif hack_sel == 1 or hack_sel == None:
            hack_menu_back = True
            print(constants.BACK_TO_MAIN_MENU)
    hack_menu_back = False

# Method that handles LIST menu
def list_menu():
    list_menu, list_menu_back = config.list_menu_config()
    
    while not list_menu_back:
        list_sel = list_menu.show()
        if list_sel == 0:
            ################
            print("")
        elif list_sel == 1:
            ################
            print("")
        elif list_sel == 2 or list_sel == None:
            list_menu_back = True
            print(constants.BACK_TO_MAIN_MENU)
    list_menu_back = False

# Method that handles EDIT menu
def edit_menu():
    edit_menu, edit_menu_back = config.edit_menu_config()
    
    while not edit_menu_back:
        edit_sel = edit_menu.show()
        if edit_sel == 0:
            ################
            print("")
        elif edit_sel == 1:
            ################
            print("")
        elif edit_sel == 2 or edit_sel == None:
            edit_menu_back = True
            print(constants.BACK_TO_MAIN_MENU)
    edit_menu_back = False

# Method that handles DELETE menu
def delete_menu():
    delete_menu, delete_menu_back = config.delete_menu_config()
    
    while not delete_menu_back:
        delete_sel = delete_menu.show()
        if delete_sel == 0:
            ################
            print("")
        elif delete_sel == 1:
            ################
            print("")
        elif delete_sel == 2 or delete_sel == None:
            delete_menu_back = True
            print(constants.BACK_TO_MAIN_MENU)
    delete_menu_back = False

# Method that handles SELECT USER menu
def select_user_menu():
    select_user_menu, select_user_menu_back = config.select_user_menu_config()
    
    while not select_user_menu_back:
        select_user_sel = select_user_menu.show()
        if select_user_sel == 0:
            ################
            print("")
        elif select_user_sel == 1:
            ################
            print("")
        elif select_user_sel == 2 or select_user_sel == None:
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
            hack_menu()
        
        # List Menu option
        elif main_sel == 1:
            list_menu()
        
        # Edit Menu option
        elif main_sel == 2:
            edit_menu()
        
        # Delete Menu option
        elif main_sel == 3:
            delete_menu()
        
        # Exiting option
        elif main_sel == 4 or main_sel == None:
            main_menu_exit = True
            print("Exiting....")
            