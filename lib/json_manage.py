import json
import pandas as pd
import sys

json_info_file = ".info.json"

# Load info from JSON info file
def get_info_json(file_path=json_info_file):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# Save info into JSON info file
def save_credentials_json(data, file_path=json_info_file):
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
                if not entry.get(key) or entry[key] != value:
                    entry[key] = value
                    updated = True
            # Changes are saved into .json file
            if updated:
                save_credentials_json(data)
            break

def get_custom_data_json(as_list=True, is_print=False, fields=[], is_markdown=False):
    data = get_info_json()
    if as_list:
        # result = []
        # for p in data:
        #     for column in p:
        #         if column in fields:
        #             result.append(p)
        
        if is_print:
            print(data)
        else:
            return data
    else:
        df = pd.DataFrame(data, columns=fields)
        if is_print:
            if is_markdown:
                print_boxed("List of: " + str(fields))
                print("\n"+df.to_markdown(index=False)+"\n")
            else:
                print_boxed("List of: " + str(fields))
                print("\n"+df+"\n")
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