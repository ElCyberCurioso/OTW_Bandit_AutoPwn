import argparse, os, shutil

import utilities_args as utilities_args
import lib.constants as constants
import lib.check_modules as check_modules
import lib.utilities as utilities

def main():
    
    class CustomAction(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            if 'ordered_args' not in namespace:
                setattr(namespace, 'ordered_args', [])
            previous = namespace.ordered_args
            previous.append((self.dest, values))
            setattr(namespace, 'ordered_args', previous)
    
    parser = argparse.ArgumentParser(description="User management tool with advanced options.")
    subparsers = parser.add_subparsers(dest="mode", required=True, help="Operation mode")

    # Menu Mode
    subparsers.add_parser("menu", help="Menu mode")

    # Edit Mode
    edit_parser = subparsers.add_parser("edit", help="Edit user data")
    edit_parser.add_argument("-p", "--password", metavar="PASSWORD", help="Change password")
    edit_parser.add_argument("-t", "--temp-folder", metavar="FOLDER", help="Change temp folder")
    edit_parser.add_argument("-n", "--notes", metavar="NOTE", help="Change notes")
    edit_parser.add_argument("-s", "--sshkey", metavar="SSHKEY", help="Change sshkey")
    edit_parser.add_argument("user", help=constants.TARGET_USER)

    # Delete Mode
    delete_parser = subparsers.add_parser("delete", help="Delete user data")
    delete_parser.add_argument("-p", "--password", action="store_true", help="Delete password")
    delete_parser.add_argument("-t", "--temp-folder", action="store_true", help="Delete temp folder")
    delete_parser.add_argument("-n", "--notes", action="store_true", help="Delete notes")
    delete_parser.add_argument("user", help=constants.TARGET_USER)

    # List Mode
    list_parser = subparsers.add_parser("list", help="List user data")
    list_parser.add_argument("-s", "--users", action="store_true", help="List users")
    list_parser.add_argument("-p", "--password", action="store_true", help="List passwords")
    list_parser.add_argument("-d", "--details", action="store_true", help="List details")
    list_parser.add_argument("-t", "--tags", action="store_true", help="List tags")
    list_parser.add_argument("-u", "--url", action="store_true", help="List URLs")
    list_parser.add_argument("-f", "--temp-folder", action="store_true", help="List temp folders asigned to users")
    list_parser.add_argument("-n", "--notes", action="store_true", help="List notes")
    list_parser.add_argument("user", nargs="?", help=constants.TARGET_USER)

    # Export Mode
    export_parser = subparsers.add_parser("export", help="Export user data")
    export_parser.add_argument("-p","--pdf", metavar="PDF_FILE", help="Export to PDF")
    export_parser.add_argument("-e", "--excel", metavar="EXCEL_FILE", help="Export to Excel")
    export_parser.add_argument("-f", "--fields", metavar="FIELDS", help='Fields to export: "user","password","details","tags","url","sshkey","temp_folder","notes"', action=CustomAction)
    export_parser.add_argument("user", nargs="?", help=constants.TARGET_USER)

    # Hack Mode
    hack_parser = subparsers.add_parser("hack", help="Special hack mode (for testing)")
    hack_parser.add_argument("user", help=constants.TARGET_USER)

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

def ensure_file_exists(file_name, source_folder):
    file_current_path, _, file_exists_current_dir = utilities.check_file_exists(__file__, file_name)
    file_source_path, _, file_exists_source_dir = utilities.check_file_exists(__file__, file_name, source_folder)
    
    # If file not found in current directory
    if not file_exists_current_dir:
        # But is found in source directory
        if file_exists_source_dir:
            # Copy to the current directory
            shutil.copy2(file_source_path, file_current_path)
            print(f"📄 File '{file_name}' copied from '{source_folder}' to main folder.")
        else:
            print(f"❌ File '{file_name}' not found in source folder '{source_folder}'.")
            raise FileNotFoundError(f"Source file '{file_name}' not found in '{source_folder}'.")

if __name__ == "__main__":
    # Check the installed modules in order to install the necessary ones.
    required = {
        "argparse": "argparse",
        "pandas": "pandas",
        "paramiko": "paramiko",
        "bz2": "bz2file",
        "lzma": "python-lzma",
        "py7zr": "py7zr",
        "fpdf": "fpdf",
        "openpyxl": "openpyxl"
    }
    check_modules.check_and_install_modules(required)
    
    # Check if .info.json exists
    ensure_file_exists(".info.json", "utils")
    
    main()