import os
import pandas as pd

import lib.json_manage as json_manage
import lib.utilities as utilities

# Update properties of a level on each execution
def update_info_for_user(user_to_update, new_password="", new_temp_folder="", new_notes="", new_sshkey=""):
    new_values = {}
    
    data = json_manage.get_info_json()
    entry = _find_user_entry(data, user_to_update)
    if entry is None:
        print(f"❌ User '{user_to_update}' not found.")
        return
    
    if new_password:
        new_values.update({"password": new_password})
    
    if new_temp_folder:
        new_values.update({"temp_folder": new_temp_folder})
    
    if new_notes:
        new_values.update({"notes": new_notes})
    
    if new_sshkey and os.path.isfile(new_sshkey): # Check if file exists
        new_values.update({"sshkey": utilities.get_b64_file_content(new_sshkey)})
    
    changes, updated = _update_entry_fields(entry, new_values)

    if not updated:
        print("No changes detected.")
        return

    if _confirm_changes(changes):
        json_manage.save_credentials_json(data)

def delete_info_for_user(user_to_update, fields=[]):
    changes = ""
    updated = False
        
    data = json_manage.get_info_json()
    entry = _find_user_entry(data, user_to_update)
    if entry is None:
        print(f"❌ User '{user_to_update}' not found.")
        return
    
    for key in fields:
        if not entry[key]:
            changes += f"{key}: already empty\n"
        else:
            changes += f"{key}: {entry[key]} -> \"\" (empty)\n"
            entry[key] = ""
            updated = True
    
    if not updated:
        print("No changes detected.")
        return
    
    if _confirm_changes(changes):
        json_manage.save_credentials_json(data)

def _find_user_entry(data, user_to_update):
    for entry in data:
        if entry["user"] == user_to_update:
            return entry
    return None

def _update_entry_fields(entry, new_values):
    changes = ""
    updated = False
    for key, value in new_values.items():
        if value and entry[key] != value:
            changes += f"{key}: {entry[key]} -> {value}\n"
            entry[key] = value
            updated = True
    return changes, updated

def _confirm_changes(changes):
    while True:
        print(changes)
        confirm = input("Confirm changes (y/n)? ").strip().lower()
        if confirm in ("y", "n"):
            return confirm == "y"
        print("\n❌ Invalid option! Please enter a valid one...")

# Method called when a single field will be printed: bandit0, bandit1,...
def _print_single_field(data, field):
    print(", ".join([entry[field] for entry in data]))

# Method called when a couple of fields will be printed: bandit0:bandit0, bandit1:<pass>,...
def _print_double_fields(data, fields):
    print(", ".join([entry[fields[0]] + ":" + entry[fields[1]] for entry in data]))

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
        if len(fields) == 1: # If filtered by one field
            _print_single_field(data, fields[0])
        elif len(fields) == 2: # If filtered by two fields
            _print_double_fields(data, fields)
        else:
            _print_data([{field: entry.get(field, "") for field in fields} for entry in data])
    else:
        _print_data(data)

def _filter_data_by_user(data, user):
    if user:
        return [item for item in data if item['user'] == user]
    return data

def _format_list_fields(data, fields):
    for entry in data:
        for field in fields:
            if field in entry and isinstance(entry[field], list):
                entry[field] = ", ".join(str(x) for x in entry[field])
    return data

def _get_dataframe(data, fields):
    return pd.DataFrame(data, columns=fields)

def get_custom_data_json(user=None, as_list=True, is_print=False, fields=None, is_markdown=False):
    if fields is None:
        fields = []
    # Checks if fields is a string list, not a list of lists
    if any(isinstance(f, list) for f in fields):
        # For nested lists
        fields = [item for sublist in fields for item in (sublist if isinstance(sublist, list) else [sublist])]
    data = json_manage.get_info_json()
    data = _filter_data_by_user(data, user)

    # Treat info as list
    if as_list:
        if is_print:
            _print_list_data(data, fields)
        else:
            return data
    # Treat info as DataFrame
    else:
        data = _format_list_fields(data, fields)
        df = _get_dataframe(data, fields)
        if is_print:
            _print_dataframe(df, fields, is_markdown)
        else:
            return df

# Print string into a box on console
#   +-----------+
#   |  Example  |
#   +-----------+
def print_boxed(text):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    border = '+' + '-' * (max_length + 2) + '+'

    print(border)
    for line in lines:
        print(f'| {line.ljust(max_length)} |')
    print(border)