JSON_INFO_FILE = ".info.json"
EXPORT_FOLDER = "exports"

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

BACK_TO_MAIN_MENU_OPTION = "Back to main menu"

MAIN_MENU = ["Hack bandit user 😈", "List info 🔎", "Edit info 📋", "Delete info 💀", "Export info 💾", "Exit 🚀"]

ARRAY_ALL_FIELDS = ["user", "password", "details", "tags", "url", "sshkey", "temp_folder"]

LIST_MENU = ARRAY_ALL_FIELDS

EDIT_MENU = ["Update password",
             "Update temp folder",
             "Update notes",
             "Update sshkey",
             "List info",
             BACK_TO_MAIN_MENU_OPTION]

DELETE_MENU = ["Delete password",
               "Delete temp folder",
               "Delete notes",
               "Delete sshkey",
               BACK_TO_MAIN_MENU_OPTION]

EXPORT_MENU = ["Export to PDF",
               "Export to Excel",
               ""]

SELECT_USER_MENU = ["<default_text>",
                    BACK_TO_MAIN_MENU_OPTION]

INVALID_OPTION = "Invalid option"
INVALID_USER = "Invalid user, please try again!"
TARGET_USER = "Target user (optional)"

HACK_USER_ACTION = "Indicate user to hack"
EDIT_DELETE_USER_ACTION = "Indicate the user to apply the changes to"

BACK_TO_MAIN_MENU = "Going back to Main Menu"

KEYS_INSTRUCTIONS = "Press Q or Esc to quit. \n"

EXITING = "See you soon! 👋"

BANDIT_USERS = [
    "bandit0", "bandit1", "bandit2", "bandit3", "bandit4", "bandit5",
    "bandit6", "bandit7", "bandit8", "bandit9", "bandit10", "bandit11",
    "bandit12", "bandit13", "bandit14", "bandit15", "bandit16", "bandit17",
    "bandit18", "bandit19", "bandit20", "bandit21", "bandit22", "bandit23",
    "bandit24", "bandit25", "bandit26", "bandit27", "bandit28", "bandit29",
    "bandit30", "bandit31", "bandit32", "bandit33"
]

GIT_REPO_BANDIT_27_28 = "ssh://bandit27-git@localhost:2220/home/bandit27-git/repo"
GIT_REPO_BANDIT_28_29 = "ssh://bandit28-git@localhost:2220/home/bandit28-git/repo"
GIT_REPO_BANDIT_29_30 = "ssh://bandit29-git@localhost:2220/home/bandit29-git/repo"
GIT_REPO_BANDIT_30_31 = "ssh://bandit30-git@localhost:2220/home/bandit30-git/repo"
GIT_REPO_BANDIT_31_32 = "ssh://bandit31-git@localhost:2220/home/bandit31-git/repo"
