import os, argparse
import lib.utilities as utilities
import menu as menu_texts

def parse_arguments():
    parser = argparse.ArgumentParser(description="Script multimodo (menú o comandos)")
    parser.add_argument('-a', '--accion', choices=['accion1', 'accion2'],
                        help='Ejecutar una acción directa sin menú')
    return parser.parse_args()

def main_menu():
    args = parse_arguments()
    if args.accion:
        utilities.clear_screen()
        if args.accion == 'accion1':
            accion1()
        elif args.accion == 'accion2':
            accion2()
    else:
        try:
            utilities.clear_screen()
            menu()
        except KeyboardInterrupt:
            utilities.exit_handler()