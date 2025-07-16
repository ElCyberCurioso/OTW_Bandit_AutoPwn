import json

def load_credentials(path="credentials.json"):
    """Load credentials from a JSON file."""
    with open(path, "r") as f:
        return json.load(f)

def get_starting_user(target_user, credentials):
    """
    Find the closest available user credential equal to or lower than the target user.
    If only bandit0 is available, prompt the user for confirmation before proceeding.
    """
    target_num = int(''.join(filter(str.isdigit, target_user)))
    available_users = []

    for user in credentials:
        num = int(''.join(filter(str.isdigit, user)))
        if num <= target_num:
            available_users.append((num, user))

    if not available_users:
        raise ValueError("No credentials available for the selected target.")

    # If only bandit0 is available, ask the user for confirmation
    if len(available_users) == 1 and available_users[0][1] == "bandit0":
        confirm = input(
            "[!] Only bandit0 credentials found. Do you want to start exploitation from bandit0? (y/n): "
        ).strip().lower()
        if confirm != 'y' and confirm != 'Y' and confirm != 'yes' and confirm != 'YES':
            print("[*] Operation cancelled by the user.")
            return None, None

    # Select the user with the highest level available below or equal to the target
    start_user = max(available_users)[1]
    return start_user, credentials[start_user]

# Example usage
if __name__ == "__main__":
    credentials = load_credentials()
    target = "bandit16"
    try:
        start_user, start_pass = get_starting_user(target, credentials)
        if start_user and start_pass:
            print(f"[*] Starting exploitation from {start_user} with password: {start_pass}")
            # Call your exploitation function here
    except ValueError as e:
        print(f"[!] Error: {e}")
