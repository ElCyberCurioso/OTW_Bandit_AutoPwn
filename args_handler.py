import argparse
import sys

VALID_USERS = ["bandit1", "bandit2", "bandit3"]

def validate_user(user):
    if user not in VALID_USERS:
        print(f"[ERROR] Invalid user: {user}")
        sys.exit(1)

def handle_hack(args):
    validate_user(args.user)
    print(f"[HACK] Hacking user {args.user}")

def handle_edit(args):
    validate_user(args.user)
    print(f"[EDIT] Editing user {args.user}")
    if args.password:
        print(f"- Changing password: {args.password}")
    if args.temp_folder:
        print(f"- Changing temp folder: {args.temp_folder}")
    if args.note:
        print(f"- Changing note: {args.note}")

def handle_delete(args):
    validate_user(args.user)
    print(f"[DELETE] Deleting data for user {args.user}")
    if args.password:
        print("- Deleting password")
    if args.temp_folder:
        print("- Deleting temp folder")
    if args.note:
        print("- Deleting note")

def handle_list(args):
    if args.user:
        validate_user(args.user)
        print(f"[LIST] Listing data for user {args.user}")
    else:
        print("[LIST] Listing data for all users")
    if args.credentials:
        print("- Listing credentials")
    if args.info:
        print("- Listing information")
    if args.notes:
        print("- Listing notes")
    if args.temp_folder:
        print("- Listing temp folders")

def handle_export(args):
    print("[EXPORT] Exporting data")
    if args.pdf:
        print(f"- Exporting to PDF: {args.pdf}")
    if args.excel:
        print(f"- Exporting to Excel: {args.excel}")
    if args.fields:
        valid_fields = {"user", "password", "details", "tags", "url", "temp_folder", "notes"}
        selected_fields = {f.strip() for f in args.fields.split(",")}
        if not selected_fields.issubset(valid_fields):
            print(f"[ERROR] Invalid fields: {selected_fields - valid_fields}")
            sys.exit(1)
        print(f"- Exporting fields: {', '.join(selected_fields)}")

def main_handlers():
    parser = argparse.ArgumentParser(description="User management tool with advanced options.")
    subparsers = parser.add_subparsers(dest="mode", required=True, help="Operation mode")

    # Hack Mode
    hack_parser = subparsers.add_parser("hack", help="Hack to get the password of the user indicated")
    hack_parser.add_argument("user", help="Target user")
    
    # Edit Mode
    edit_parser = subparsers.add_parser("edit", help="Edit user data")
    edit_parser.add_argument("-p", "--password", metavar="PASSWORD", help="Change password")
    edit_parser.add_argument("-i", "--id-rsa", metavar="IDRSA", help="Change sshkey")
    edit_parser.add_argument("-t", "--temp-folder", metavar="FOLDER", help="Change temp folder")
    edit_parser.add_argument("-n", "--note", metavar="NOTE", help="Change note")
    edit_parser.add_argument("user", help="Target user")

    # Delete Mode
    delete_parser = subparsers.add_parser("delete", help="Delete user data")
    delete_parser.add_argument("-p", "--password", action="store_true", help="Delete password")
    delete_parser.add_argument("-t", "--temp-folder", action="store_true", help="Delete temp folder")
    delete_parser.add_argument("-n", "--note", action="store_true", help="Delete note")
    delete_parser.add_argument("user", help="Target user")

    # List Mode
    list_parser = subparsers.add_parser("list", help="List user data")
    list_parser.add_argument("-c", "--credentials", action="store_true", help="List credentials")
    list_parser.add_argument("-i", "--info", action="store_true", help="List information")
    list_parser.add_argument("--notes", action="store_true", help="List notes")
    list_parser.add_argument("-t", "--temp-folder", action="store_true", help="List temp folders")
    list_parser.add_argument("user", nargs="?", help="Target user (optional)")

    # Export Mode
    export_parser = subparsers.add_parser("export", help="Export user data")
    export_parser.add_argument("-p","--pdf", metavar="PDF_FILE", help="Export to PDF")
    export_parser.add_argument("-e", "--excel", metavar="EXCEL_FILE", help="Export to Excel")
    export_parser.add_argument("-f", "--fields", metavar="FIELDS", help='Fields to export: "user","password","details","tags","url","temp_folder","notes"')

    args = parser.parse_args()

    mode_handlers = {
        "hack": handle_hack,
        "edit": handle_edit,
        "delete": handle_delete,
        "list": handle_list,
        "export": handle_export
    }

    handler = mode_handlers.get(args.mode)
    if handler:
        handler(args)
