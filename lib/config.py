import lib.constants as constants
import lib.utilities as utilities

from simple_term_menu import TerminalMenu

# Main menu config
main_menu_cursor = "~$ "
main_left_space = " " * len(main_menu_cursor)
main_menu_title = main_left_space + "Main Menu.\n" + main_left_space + constants.KEYS_INSTRUCTIONS
main_menu_items = constants.MAIN_MENU
main_menu_cursor_style = ("fg_green",)
main_menu_style = ("bg_green", "fg_black", "italics")

# List menu config
list_menu_title = main_left_space[:-1] + "LIST Info Menu.\n" + main_left_space[:-1] + constants.KEYS_INSTRUCTIONS
list_menu_items = constants.LIST_MENU
list_menu_cursor = main_menu_cursor
list_menu_cursor_style = main_menu_cursor_style
list_menu_style = main_menu_style

# Edit menu config
edit_menu_title = main_left_space + "EDIT Info Menu.\n" + main_left_space + constants.KEYS_INSTRUCTIONS
edit_menu_items = constants.EDIT_MENU
edit_menu_cursor = main_menu_cursor
edit_menu_cursor_style = main_menu_cursor_style
edit_menu_style = main_menu_style

# Delete menu config
delete_menu_title = main_left_space + "DELETE Info Menu.\n" + main_left_space + constants.KEYS_INSTRUCTIONS
delete_menu_items = constants.DELETE_MENU
delete_menu_cursor = main_menu_cursor
delete_menu_cursor_style = main_menu_cursor_style
delete_menu_style = main_menu_style

# Export menu config
export_menu_title = main_left_space[:-1] + "EXPORT Info Menu.\n" + main_left_space[:-1] + constants.KEYS_INSTRUCTIONS
export_menu_items = utilities.get_export_menu_fields()
export_menu_cursor = main_menu_cursor
export_menu_cursor_style = main_menu_cursor_style
export_menu_style = main_menu_style

# Input user menu config
select_user_menu_title = "Select User Menu.\n" + main_left_space + constants.KEYS_INSTRUCTIONS
select_user_menu_items = constants.SELECT_USER_MENU
select_user_menu_cursor = main_menu_cursor
select_user_menu_cursor_style = main_menu_cursor_style
select_user_menu_style = main_menu_style

# Method that handles MAIN menu
def main_menu_config():
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=constants.BANNER + "\n" + main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
        clear_screen=False,
    )
    
    return main_menu, main_menu_exit

# Method that handles LIST menu
def list_menu_config():
    list_menu_exit = False
    
    list_menu = TerminalMenu(
        constants.LIST_MENU,
        title=list_menu_title,
        multi_select=True,
        show_multi_select_hint=True,
        cycle_cursor=True,
        clear_screen=False,
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

# Method that handles EXPORT menu
def export_menu_config():
    export_menu_exit = False

    export_menu = TerminalMenu(
        utilities.get_export_menu_fields(),
        title=export_menu_title,
        multi_select=True,
        show_multi_select_hint=True,
        cycle_cursor=True,
        clear_screen=False,
        skip_empty_entries=True,
    )

    return export_menu, export_menu_exit

# Method that handles SELECT USER menu
def select_user_menu_config(next_text, next_title):
    select_user_menu_exit = False

    select_user_menu = TerminalMenu(
        menu_entries=[next_text if x == "<default_text>" else x for x in select_user_menu_items], # Change <default_text> with next_text parameter in menu entries array
        title=main_left_space + next_title + " > " + select_user_menu_title,
        menu_cursor=select_user_menu_cursor,
        menu_cursor_style=select_user_menu_cursor_style,
        menu_highlight_style=select_user_menu_style,
        cycle_cursor=True,
        clear_screen=False,
    )

    return select_user_menu, select_user_menu_exit