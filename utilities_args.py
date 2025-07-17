import sys

import menu as menu
import lib.utilities as utilities
import lib.constants as constants
import lib.json_manage as json_manage

# VALID_USERS = ["bandit1", "bandit2", "bandit3"]

# def validate_user(user):
#     if user not in VALID_USERS:
#         print(f"[ERROR] Invalid user: {user}")
#         sys.exit(1)

def handle_menu(args):
    # validate_user(args.user)
    menu.main_menu()

def handle_hack(args):
    # validate_user(args.user)
    print(f"[HACK] Special hack mode activated for user {args.user}\n")

def handle_edit(args):
    password = ""
    temp_folder = ""
    notes = ""
    
    if args.password:
        password = args.password
    if args.temp_folder:
        temp_folder = args.temp_folder
    if args.note:
        notes = args.note
    
    json_manage.update_info_for_user(args.user, new_password=password, new_temp_folder=temp_folder, new_notes=notes)

def handle_delete(args):
    password = ""
    temp_folder = ""
    notes = ""
    # validate_user(args.user)
    print(f"[DELETE] Deleting data for user {args.user}\n")
    
    if args.password:
        password = args.password
    if args.temp_folder:
        temp_folder = args.temp_folder
    if args.notes:
        notes = args.notes
    
    json_manage.update_info_for_user(args.user, new_password=args.password, new_temp_folder=temp_folder, new_notes=notes)

def handle_list(args):
    fields = []
    
    if args.user:
        # validate_user(args.user)
        print(f"[LIST] Listing data for user {args.user}\n")
    else:
        print("[LIST] Listing data for all users\n")
        
    if args.password:
        fields.append("password")
    if args.details:
        fields.append("details")
    if args.tags:
        fields.append("tags")
    if args.url:
        fields.append("url")
    if args.temp_folder:
        fields.append("temp_folder")
    if args.notes:
        fields.append("notes")
        
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
