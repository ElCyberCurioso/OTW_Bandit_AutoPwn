import sys

import menu as menu
import lib.utilities as utilities
import lib.constants as constants
import lib.json_manage as json_manage
import exploitation_chain as ec

def handle_menu(args):
    utilities.validate_user(args.user)
    menu.main_menu()

def handle_hack(args):
    utilities.validate_user(args.user)
    ec.main(args.user)

def handle_edit(args):
    password = ""
    temp_folder = ""
    notes = ""
    
    if args.password:
        password = args.password
    if args.temp_folder:
        temp_folder = args.temp_folder
    if args.notes:
        notes = args.notes
    
    json_manage.update_info_for_user(args.user, new_password=password, new_temp_folder=temp_folder, new_notes=notes)

def handle_delete(args):
    fields = []
    utilities.validate_user(args.user)
    
    if args.password:
        fields.append("password")
    if args.temp_folder:
        fields.append("temp_folder")
    if args.notes:
        fields.append("notes")
    
    json_manage.delete_info_for_user(args.user, fields)

def get_selected_fields(args):
    field_names = ["user", "password", "details", "tags", "url", "temp_folder", "notes"]
    selected_flags = [args.users, args.password, args.details, args.tags, args.url, args.temp_folder, args.notes]
    list_all = all(selected_flags) or not any(selected_flags)
    if list_all:
        return field_names
    return [name for flag, name in zip(selected_flags, field_names) if flag]

def handle_list(args):
    if args.user:
        utilities.validate_user(args.user)
        print(f"[LIST] Listing data for user {args.user}\n")
    else:
        print("[LIST] Listing data for all users\n")

    fields = get_selected_fields(args)
    utilities.print_table(fields, user=args.user)

def handle_export(args):
    print("[EXPORT] Exporting data\n")
    if args.pdf:
        print(f"- Exporting to PDF: {args.pdf}\n")
    if args.excel:
        print(f"- Exporting to Excel: {args.excel}\n")
    if args.fields:
        valid_fields = {"user", "password", "details", "tags", "url", "temp_folder", "notes"}
        selected_fields = {f.strip() for f in args.fields.split(",")}
        if not selected_fields.issubset(valid_fields):
            print(f"[ERROR] Invalid fields: {selected_fields - valid_fields}")
            sys.exit(1)
        print(f"- Exporting fields: {', '.join(selected_fields)}")
