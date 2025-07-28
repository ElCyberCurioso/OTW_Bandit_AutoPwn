import lib.constants as constants
from simple_term_menu import TerminalMenu

# Main menu config
main_menu_title = "  Main Menu.\n  Press Q or Esc to quit. \n"
main_menu_items = constants.MAIN_MENU
main_menu_cursor = "$ "
main_menu_cursor_style = ("fg_red", "bold")
main_menu_style = ("bg_green", "fg_black")

# Hack menu config
hack_menu_title = "  HACK Info Menu.\n  Press Q or Esc to quit. \n"
hack_menu_items = constants.HACK_MENU
hack_menu_cursor = main_menu_cursor
hack_menu_cursor_style = main_menu_cursor_style
hack_menu_style = main_menu_style

# List menu config
list_menu_title = "  LIST Info Menu.\n  Press Q or Esc to quit. \n"
list_menu_items = constants.LIST_MENU
list_menu_cursor = main_menu_cursor
list_menu_cursor_style = main_menu_cursor_style
list_menu_style = main_menu_style

# Edit menu config
edit_menu_title = "  EDIT Info Menu.\n  Press Q or Esc to quit. \n"
edit_menu_items = constants.EDIT_MENU
edit_menu_cursor = main_menu_cursor
edit_menu_cursor_style = main_menu_cursor_style
edit_menu_style = main_menu_style

# Delete menu config
delete_menu_title = "  DELETE Info Menu.\n  Press Q or Esc to quit. \n"
delete_menu_items = constants.DELETE_MENU
delete_menu_cursor = main_menu_cursor
delete_menu_cursor_style = main_menu_cursor_style
delete_menu_style = main_menu_style

# Input user menu config
select_user_menu_title = "  Select User Menu.\n  Press Q or Esc to quit. \n"
select_user_menu_items = constants.SELECT_USER_MENU
select_user_menu_cursor = main_menu_cursor
select_user_menu_cursor_style = main_menu_cursor_style
select_user_menu_style = main_menu_style

# Method that handles MAIN menu
def main_menu_config():
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )
    
    return main_menu, main_menu_exit

# Method that handles HACK menu
def hack_menu_config():
    hack_menu_exit = False

    hack_menu = TerminalMenu(
        menu_entries=hack_menu_items,
        title=hack_menu_title,
        menu_cursor=hack_menu_cursor,
        menu_cursor_style=hack_menu_cursor_style,
        menu_highlight_style=hack_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )
    
    return hack_menu, hack_menu_exit

# Method that handles LIST menu
def list_menu_config():
    list_menu_exit = False

    list_menu = TerminalMenu(
        menu_entries=list_menu_items,
        title=list_menu_title,
        menu_cursor=list_menu_cursor,
        menu_cursor_style=list_menu_cursor_style,
        menu_highlight_style=list_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )
    
    return list_menu, list_menu_exit

# Method that handles EDIT menu
def edit_menu_config():
    edit_menu_exit = False

    edit_menu = TerminalMenu(
        menu_entries=edit_menu_items,
        title=edit_menu_title,
        menu_cursor=edit_menu_cursor,
        menu_cursor_style=edit_menu_cursor_style,
        menu_highlight_style=edit_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )
    
    return edit_menu, edit_menu_exit

# Method that handles DELETE menu
def delete_menu_config():
    delete_menu_exit = False

    delete_menu = TerminalMenu(
        menu_entries=delete_menu_items,
        title=delete_menu_title,
        menu_cursor=delete_menu_cursor,
        menu_cursor_style=delete_menu_cursor_style,
        menu_highlight_style=delete_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    return delete_menu, delete_menu_exit

# Method that handles SELECT USER menu
def select_user_menu_config():
    select_user_menu_exit = False

    select_user_menu = TerminalMenu(
        menu_entries=select_user_menu_items,
        title=select_user_menu_title,
        menu_cursor=select_user_menu_cursor,
        menu_cursor_style=select_user_menu_cursor_style,
        menu_highlight_style=select_user_menu_style,
        cycle_cursor=True,
        clear_screen=True,
    )

    return select_user_menu, select_user_menu_exit