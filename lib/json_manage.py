import json
import pandas as pd
import sys

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

# Update properties of a level on each execution
def update_info_for_user(user_to_update, new_password="", new_temp_folder="", new_notes=""):
    data = get_info_json()
    
    # For every bandit user
    for entry in data:
        if entry["user"] == user_to_update:
            changes = {
                "password": new_password,
                "temp_folder": new_temp_folder,
                "notes": new_notes
            }
            updated = False
            
            for key, value in changes.items():
                # If changes are found, values are updated
                if value and entry[key] != value:
                    print(key + ": " + entry[key] + " -> " + value)
                    entry[key] = value
                    updated = True
            # Changes are saved into .json file
            if updated:
                save_credentials_json(data)
            break

def _print_single_field(data, field):
    print(", ".join([entry[field] for entry in data]))

def _print_data(data):
    print(data)

def _print_dataframe(df, fields, is_markdown):
    print_boxed("List of: " + str(fields))
    if is_markdown:
        print("\n" + df.to_markdown(index=False) + "\n")
    else:
        print("\n" + str(df) + "\n")

def _print_list_data(data, fields):
    if fields:
        if len(fields) == 1:
            _print_single_field(data, fields[0])
        else:
            _print_data([{field: entry.get(field, "") for field in fields} for entry in data])
    else:
        _print_data(data)

def get_custom_data_json(as_list=True, is_print=False, fields=None, is_markdown=False):
    if fields is None:
        fields = []
    data = get_info_json()
    if as_list:
        if is_print:
            _print_list_data(data, fields)
        else:
            return data
    else:
        df = pd.DataFrame(data, columns=fields)
        if is_print:
            _print_dataframe(df, fields, is_markdown)
        else:
            return df

def print_boxed(text):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    border = '+' + '-' * (max_length + 2) + '+'

    print(border)
    for line in lines:
        print(f'| {line.ljust(max_length)} |')
    print(border)

# get_custom_data_json(as_list=True, is_print=True, fields=["user"], is_markdown=True)