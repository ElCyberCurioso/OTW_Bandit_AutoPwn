import argparse

import utilities_args as utilities_args

def main():
    parser = argparse.ArgumentParser(description="User management tool with advanced options.")
    subparsers = parser.add_subparsers(dest="mode", required=True, help="Operation mode")

    # Menu Mode
    subparsers.add_parser("menu", help="Menu mode")

    # Edit Mode
    edit_parser = subparsers.add_parser("edit", help="Edit user data")
    edit_parser.add_argument("-p", "--password", metavar="PASSWORD", help="Change password")
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
    list_parser.add_argument("-p", "--password", action="store_true", help="List passwords")
    list_parser.add_argument("-d", "--details", action="store_true", help="List details")
    list_parser.add_argument("-t", "--tags", action="store_true", help="List tags")
    list_parser.add_argument("-u", "--url", action="store_true", help="List URLs")
    list_parser.add_argument("-f", "--temp-folder", action="store_true", help="List temp folders asigned to users")
    list_parser.add_argument("-n", "--notes", action="store_true", help="List notes")
    list_parser.add_argument("user", nargs="?", help="Target user (optional)")

    # Export Mode
    export_parser = subparsers.add_parser("export", help="Export user data")
    export_parser.add_argument("--pdf", metavar="PDF_FILE", help="Export to PDF")
    export_parser.add_argument("-e", "--excel", metavar="EXCEL_FILE", help="Export to Excel")
    export_parser.add_argument("-f", "--fields", metavar="FIELDS", help='Fields to export: "user","password","details","tags","url","temp_folder","notes"')

    # Hack Mode
    hack_parser = subparsers.add_parser("hack", help="Special hack mode (for testing)")
    hack_parser.add_argument("user", help="Target user")

    args = parser.parse_args()

    mode_handlers = {
        "menu": utilities_args.handle_menu,
        "edit": utilities_args.handle_edit,
        "delete": utilities_args.handle_delete,
        "list": utilities_args.handle_list,
        "export": utilities_args.handle_export,
        "hack": utilities_args.handle_hack
    }

    handler = mode_handlers.get(args.mode)
    if handler:
        handler(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()