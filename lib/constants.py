JSON_INFO_FILE = ".info.json"

OTW_BANDIT_SSH_URL = "bandit.labs.overthewire.org"
OTW_BANDIT_SSH_PORT = 2220

DEFAULT_USER = "bandit0"
DEFAULT_PASSWORD = "bandit0"

BANNER = """
   ___                _____ _        __        ___          
  / _ \__   _____ _ _|_   _| |__   __\ \      / (_)_ __ ___ 
 | | | \ \ / / _ \ '__|| | | '_ \ / _ \ \ /\ / /| | '__/ _ \\
 | |_| |\ V /  __/ |   | | | | | |  __/\ V  V / | | | |  __/
  \___/  \_/ \___|_|   |_| |_| |_|\___| \_/\_/  |_|_|  \___|
  ____                  _ _ _                               
 | __ )  __ _ _ __   __| (_) |_                             
 |  _ \ / _` | '_ \ / _` | | __|                            
 | |_) | (_| | | | | (_| | | |_                             
 |____/ \__,_|_| |_|\__,_|_|\__|                            
     _         _        ______        ___   _               
    / \  _   _| |_ ___ |  _ \ \      / / \ | |              
   / _ \| | | | __/ _ \| |_) \ \ /\ / /|  \| |              
  / ___ \ |_| | || (_) |  __/ \ V  V / | |\  |              
 /_/   \_\__,_|\__\___/|_|     \_/\_/  |_| \_|              
                                                            
"""

MODIFY_MENU = """
--- Modify Info Menu ---
1. Update password
2. Update folder
3. Update notes
4. List info
5. Back
Choose an option:
"""

LIST_MENU = """
--- List Info Menu ---
1. List credentials (user + password + temp_folder)
2. List guiding info (user + details + url)
3. List notes (user + notes)
4. List tags (user + tags)
5. Back
Choose an option:
"""

HACK_MENU = """
--- Hack Menu ---
1. Indicate user to hack
2. Back
Choose an option:
"""

MAIN_MENU = """
1. Hack bandit user
2. List info
3. Modify info
4. Clean screen
5. Show banner
6. Exit
Choose an option:
"""

INVALID_OPTION = "Invalid option."
INVALID_USER = "Invalid user, please try again!"