import subprocess, sys
import importlib.util

def install_missing_modules(missing):
    for import_name, pip_name in missing:
        print(f"Installing {pip_name}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
            print(f"✅ {pip_name} installed successfully.")
        except Exception as e:
            print(f"❌ Error installing {pip_name}: {e}")
    print("✅ Dependency check completed.")

def check_and_install_modules(modules: dict):
    """
    Checks if required modules are installed. If not, asks the user to install them.

    :param modules: Dictionary { 'import_name': 'pip_package_name' }
    """
    missing = [
        (import_name, pip_name)
        for import_name, pip_name in modules.items()
        if importlib.util.find_spec(import_name) is None
    ]

    if not missing:
        # print("✅ All required modules are already installed.")
        return

    print("⚠️ The following required modules are missing:")
    for import_name, pip_name in missing:
        print(f" - {pip_name} (imported as '{import_name}')")
    choice = input("Do you want to install them now? (y/n): ").strip().lower()
    if choice == 'y':
        install_missing_modules(missing)
    else:
        print("❌ Installation cancelled. The script may not work properly.")
        sys.exit(1)
