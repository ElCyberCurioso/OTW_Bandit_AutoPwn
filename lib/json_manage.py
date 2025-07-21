import json

import lib.constants as constants

# Load info from JSON info file
def get_info_json(file_path=constants.JSON_INFO_FILE):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# Save info into JSON info file
def save_credentials_json(data, file_path=constants.JSON_INFO_FILE):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
