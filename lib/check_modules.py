import sys
import subprocess
import pkg_resources

def check_installed_modules(required={}):
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        print("Modules missing: " + missing + ". Installing....")
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)