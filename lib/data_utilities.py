import os, time
import pandas as pd

import lib.json_manage as json_manage
import lib.utilities as utilities

# Update properties of a level on each execution
def update_info_for_user(user_to_update, is_automated=False, new_password="", new_temp_folder="", new_notes="", new_sshkey=""):
    new_values = {}
    
    data = json_manage.get_info_json()
    entry = _find_user_entry(data, user_to_update)
    if entry is None:
        print(f"User '{user_to_update}' not found.")
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

    if not is_automated:
        if _confirm_changes(changes):
            json_manage.save_credentials_json(data)
    else:
        json_manage.save_credentials_json(data)

def delete_info_for_user(user_to_update, fields=[]):
    changes = ""
    updated = False
    
    data = json_manage.get_info_json()
    entry = _find_user_entry(data, user_to_update)
    if entry is None:
        print(f"User '{user_to_update}' not found.")
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
        print("Performing changes...")
        json_manage.save_credentials_json(data)
        time.sleep(2)

def delete_all_info_for_users(field=None):
    changes = ""
    updated = False
    key = field[0]
    
    data = json_manage.get_info_json()

    if not key:
        print(f"Field '{key}' not found.")
        return
    
    for entry in data[1:]:
        if not entry[key]:
            changes += f"({entry['user']}) {key}: already empty\n"
        else:
            changes += f"({entry['user']}) {key}: {entry[key]} -> \"\" (empty)\n"
            entry[key] = ""
            updated = True
    
    if not updated:
        print("No changes detected. Exiting...")
        time.sleep(2)
        return
    
    if _confirm_changes(changes):
        print("Performing changes...")
        json_manage.save_credentials_json(data)
        time.sleep(2)

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
        print("\nInvalid option! Please enter a valid one...")

# Method called to print a list
def _print_fields(data, fields, cols):
    
    if len(fields) == 1:
        values = [entry[fields[0]] for entry in data]
    elif len(fields) == 2:
        values = [entry[fields[0]] + ":" + entry[fields[1]] for entry in data]
    
    # Generate all strings to be displayed (index + value)
    formatted_values = [f"{v}" for _, v in enumerate(values)]

    # Determine the maximum width among all formatted entries
    max_width = max(len(s) for s in formatted_values) + 2  # Add padding between columns

    # Calculate how many rows are needed
    rows, extra = divmod(len(values), cols)
    if extra > 0:
        rows += 1  # Add one more row if there are leftover items

    # Print each row
    for row in range(rows):
        line = ""
        for col in range(cols):
            i = col * rows + row  # Calculate the index for column-major order
            if i < len(formatted_values):
                line += formatted_values[i].ljust(max_width)  # Left-align each column entry
        print(line)

def _print_dataframe(df, fields, is_markdown):
    print_boxed("List of: " + str(fields))
    
    if is_markdown:
        print("\n" + df.to_markdown(index=False) + "\n")
    else:
        print("\n" + str(df) + "\n")

def _print_list_data(data, fields, cols):
    if fields:
        _print_fields(data, fields, cols)
    else:
        print(data)

def _filter_data_by_user(data, users):
    if users:
        return [item for item in data if item['user'] in users]
    return data

def _format_list_fields(data, fields):
    for entry in data:
        for field in fields:
            if field in entry and isinstance(entry[field], list):
                entry[field] = ", ".join(str(x) for x in entry[field])
    return data

def _get_dataframe(data, fields):
    return pd.DataFrame(data, columns=fields)

def _flatten_fields(fields):
    """Aplana una lista de campos que puede contener sublistas."""
    if fields is None:
        return []
    if not any(isinstance(f, list) for f in fields):
        return fields
    return [item for sublist in fields for item in (sublist if isinstance(sublist, list) else [sublist])]

def _handle_list_case(data, fields, cols, is_print, users):
    """Maneja el caso cuando los datos se deben retornar como lista."""
    if is_print:
        _print_list_data(data, fields, cols)
        return None
    
    return [data[0].get(field) for field in fields] if (users and data) else data

def _handle_dataframe_case(data, fields, is_print, is_markdown):
    """Maneja el caso cuando los datos se deben retornar como DataFrame."""
    data = _format_list_fields(data, fields)
    df = _get_dataframe(data, fields)
    
    if is_print:
        _print_dataframe(df, fields, is_markdown)
        return None
    
    return df

def get_custom_data_json(cols=None, users=[], as_list=True, is_print=False, fields=None, is_markdown=False):
    fields = _flatten_fields(fields)
    data = json_manage.get_info_json()
    data = _filter_data_by_user(data, users)

    if as_list:
        return _handle_list_case(data, fields, cols, is_print, users)
    else:
        return _handle_dataframe_case(data, fields, is_print, is_markdown)

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