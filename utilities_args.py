import sys

import menu as menu
import lib.utilities as utilities
import lib.constants as constants
import lib.json_manage as json_manage
import exploitation_chain as ec
import lib.export as export

def handle_menu(_):
    menu.main_menu()

def handle_hack(args):
    utilities.validate_user(args.user)
    ec.main(args.user)

def handle_edit(args):
    password = ""
    temp_folder = ""
    notes = ""
    sshkey = ""
    
    if args.password:
        password = args.password
    if args.temp_folder:
        temp_folder = args.temp_folder
    if args.notes:
        notes = args.notes
    if args.sshkey:
        sshkey = args.sshkey
    
    json_manage.update_info_for_user(args.user, new_password=password, new_temp_folder=temp_folder, new_notes=notes, new_sshkey=sshkey)

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
        print(f"📋​ Listing data for user {args.user}\n")
    else:
        print("📋​ Listing data for all users\n")

    fields = get_selected_fields(args)
    utilities.print_table(fields, user=args.user)

def _export_to_pdf(df, filename, user):
    if user:
        filename = filename + "_" + user
    if not filename.endswith(".pdf"):
        filename = filename + ".pdf"
    
    _, _, file_exists = utilities.check_file_exists(__file__, filename)
    if file_exists:
        print("\n❌​ File exist already!")
        return
    
    print(f"​\n✔️ Exporting to PDF: {filename}\n")
    export.export_to_pdf(df, filename)

def _export_to_excel(df, filename, user):
    if user:
        filename = filename + "_" + user
    if not filename.endswith(".xlsx"):
        filename = filename + ".xlsx"
    
    _, _, file_exists = utilities.check_file_exists(__file__, filename)
    if file_exists:
        print("\n❌​ File exist already!")
        return
    
    print(f"​\n✔️ Exporting to Excel: {filename}\n")
    export.export_to_excel(df, filename)

def handle_export(args):
    print("📎 Exporting data")
    invalid_fields = []
    array_selected_fields = []

    if args.ordered_args:
        valid_fields = {"user", "password", "details", "tags", "url", "sshkey", "temp_folder", "notes"}
        selected_fields = args.ordered_args[0][1]
        array_selected_fields = selected_fields.split(',')
        invalid_fields = [field for field in array_selected_fields if field not in valid_fields]
        if invalid_fields:
            print(f"❌​ Invalid fields: {invalid_fields}")
            sys.exit(1)
        print(f"​\n📁​ Exporting fields: {selected_fields}")

    if args.user:
        utilities.validate_user(args.user)

    df = json_manage.get_custom_data_json(user=args.user, as_list=False, is_print=False, fields=array_selected_fields)

    if args.pdf:
        _export_to_pdf(df, args.pdf, args.user)
    if args.excel:
        _export_to_excel(df, args.excel, args.user)
        