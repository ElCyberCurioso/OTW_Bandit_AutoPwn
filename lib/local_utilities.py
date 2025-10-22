import os, shutil, pexpect

# Check if file exist on the current directory or an indicated one
def check_file_exists(this_file, file_name, file_directory=None):
    if file_directory:
        search_path = file_directory
    else:
        search_path = os.path.dirname(os.path.abspath(this_file))
        
    file = os.path.join(search_path, file_name)
    if os.path.isfile(file):
        return file, search_path, True
    else:
        return file, search_path, False

# Copy file file_name from source_folder if doesnt exist on current folder
def get_file_if_not_exists(file_name, source_folder, main_folder):
    # Check if exists on the current directory
    file_current_path, _, file_exists_current_dir = check_file_exists(__file__, file_name, file_directory=main_folder)
        
    # If file not found in current directory
    if not file_exists_current_dir:
        # Check if exists on the source directory
        file_source_path, _, file_exists_source_dir = check_file_exists(__file__, file_name, source_folder)
        
        # But is found in source directory
        if file_exists_source_dir:
            # Copy to the current directory
            shutil.copy2(file_source_path, file_current_path)
            print(f"File '{file_name}' copied from '{source_folder}' to main folder.")
        else:
            print(f"File '{file_name}' not found in source folder '{source_folder}'.")
            raise FileNotFoundError(f"Source file '{file_name}' not found in '{source_folder}'.")

# Create resource folder
def create_resources_folder():
    current_path = os.path.dirname(__file__)
    main_project_path = os.path.join(current_path, "../")
    resources_path = os.path.join(main_project_path, "resources")
    
    if not os.path.exists(resources_path):
        os.makedirs(resources_path)
    
    return resources_path

# Create a bandit folder inside resource folder
def create_subfolder_on_resources_folder(resources_path, subfolders):
    subfolder_path = os.path.join(resources_path, subfolders)
    
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    
    return subfolder_path

# Manage to clone a git repo into a temp folder
def git_clone_repo_bandit(repo_url, current_password, dest_dir):
    # Iniciamos el proceso interactivo
    child = pexpect.spawn(f"git clone {repo_url} {dest_dir}", encoding='utf-8')

    # Espera el prompt de contraseña
    child.expect("assword:")
    child.sendline(current_password)

    # Espera a que termine
    child.expect(pexpect.EOF)

    print(child.before)