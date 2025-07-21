# 🐙 OTW Bandit AutoPwn

**Automate your Bandit challenges with Python + Pandas**

## 📌 Description

**OTW\_Bandit\_AutoPwn** is an automated tool designed to solve challenges from the [**OverTheWire Bandit**](https://overthewire.org/wargames/bandit/) wargame.\
It uses Python and Pandas to manage users, passwords, and automate SSH command execution for solving levels.

Perfect for beginners who want to learn basic Linux and scripting techniques.

## 🛠️ Features

- 📝 User and password management in JSON format
- 🐍 Interactive command-line menu
- 🚀 Automated SSH command execution for each level
- 📊 Uses Pandas to read, edit, and save user data
- 🔐 Options to view, edit, and add users

## ⚡ Quick Installation

```bash
git clone https://github.com/ElCyberCurioso/OTW_Bandit_AutoPwn.git
cd OTW_Bandit_AutoPwn
pip install -r requirements.txt
python3 main.py
```

## 🎮 Requirements

- Python 3.10+
- Pandas
- Paramiko or SSH libraries (if required)
- Internet connection (for SSH access)

## 🕹️ How to Use

1️⃣ Interactive menu to navigate (`main.py menu`)\

With interactive menu:

```
   ___                _____ _        __        ___
  / _ \__   _____ _ _|_   _| |__   __\ \      / (_)_ __ ___ 
 | | | \ \ / / _ \ '__|| | | '_ \ / _ \ \ /\ / /| | '__/ _ \
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


+-----------+
| Main menu |
+-----------+

1️⃣  Hack bandit user 👨‍💻
2️⃣  List info 📋​
3️⃣  Edit info ​✒️​
4️⃣  Delete info 🧼​
5️⃣  Clean screen 🧹​
6️⃣  Show banner ​🏴‍☠️​
7️⃣  Exit ​🚀​
```

HACK Menu:

```
--- HACK Menu ---
1️⃣  Indicate user to hack ​​🗃️​
2️⃣  Back ​🔙​

+-------------------------------------------------------+
| List of: ('user', 'password', 'temp_folder', 'notes') |
+-------------------------------------------------------+

| user     | password                         | temp_folder   | notes   |
|:---------|:---------------------------------|:--------------|:--------|
| bandit0  | bandit0                          |               |         |
| bandit1  | test321123                       |               |         |
| bandit2  |                                  |               |         |
| bandit3  |                                  |               |         |


Indicate user (or type 'back' to return): bandit1
🔎​​ Starting exploitation from bandit1 with password: test321123
✅​ Reached target user: bandit1:test321123
```

LIST menu:

```
--- LIST Info Menu ---
1️⃣  List credentials (user + password + temp_folder)
2️⃣  List guiding info (user + details + url)        
3️⃣  List notes (user + notes)
4️⃣  List tags (user + tags)
5️⃣  Back ​🔙​

+----------------------------------------------+
| List of: ('user', 'password', 'temp_folder') |
+----------------------------------------------+

| user     | password                         | temp_folder   |
|:---------|:---------------------------------|:--------------|
| bandit0  | bandit0                          |               |
| bandit1  | test321123                       |               |
| bandit2  |                                  |               |
| bandit3  |                                  |               |
...

+-------------------------------------+
| List of: ('user', 'details', 'url') |
+-------------------------------------+

| user     | details                                                      | url                                                   |
|:---------|:-------------------------------------------------------------|:------------------------------------------------------|
| bandit0  | Reading a file with 'cat'                                    | https://overthewire.org/wargames/bandit/bandit0.html  |
| bandit1  | Viewing hidden file with a dash prefix                       | https://overthewire.org/wargames/bandit/bandit1.html  |
| bandit2  | Reading a file with spaces in its name                       | https://overthewire.org/wargames/bandit/bandit2.html  |
| bandit3  | Reading a hidden file in a hidden directory                  | https://overthewire.org/wargames/bandit/bandit3.html  |
...

+----------------------------+
| List of: ('user', 'notes') |
+----------------------------+

| user     | notes   |
|:---------|:--------|
| bandit0  |         |
| bandit1  |         |
| bandit2  |         |
...

+---------------------------+
| List of: ('user', 'tags') |
+---------------------------+

| user     | tags                                                  |
|:---------|:------------------------------------------------------|
| bandit0  | file-read, basic, linux-commands                      |
| bandit1  | hidden-files, file-read, linux-commands               |
| bandit2  | file-read, escaping, special-characters               |
| bandit3  | hidden-directories, file-read, navigation             |
...
```

EDIT menu:

```
--- EDIT Info Menu ---      
1️⃣​  Update password 🔑    
2️⃣  Update temp folder ​📁​
3️⃣  Update notes 📝​       
4️⃣  Update sshkey ​🔐​     
5️⃣  List info ​📋​
6️⃣  Back ​🔙​


bandit0:bandit0, bandit1:test321123, bandit2:, bandit3:, ...

Indicate user (or type 'back' to return): bandit1
Enter new password for bandit1: test123321
password: test321123 -> test123321

Confirm changes (y/n)? y
```

DELETE menu:

```
--- DELETE Info Menu ---    
1️⃣  Delete password 🔑     
2️⃣  Delete temp folder ​📁​
3️⃣  Delete notes 📝​       
4️⃣  Delete sshkey ​🔐​     
5️⃣  Back ​🔙​

bandit0:bandit0, bandit1:test123321, bandit2:, bandit3:, ...

Indicate user (or type 'back' to return): bandit1
password: test123321 -> "" (empty)

Confirm changes (y/n)? y
```

2️⃣ Parameters (`main.py edit/delete/list/export/hack`)\

With parameters:

```
PS C:\OWT_Bandit_AutoPwn> python .\main.py -h  
usage: main.py [-h] {menu,edit,delete,list,export,hack} ...

User management tool with advanced options.

positional arguments:
  {menu,edit,delete,list,export,hack}
                        Operation mode
    menu                Menu mode
    edit                Edit user data
    delete              Delete user data
    list                List user data
    export              Export user data
    hack                Special hack mode (for testing)    

options:
  -h, --help            show this help message and exit
```

MENU mode help:

```
PS C:\OWT_Bandit_AutoPwn> python .\main.py menu -h
usage: main.py menu [-h]

options:
  -h, --help  show this help message and exit
```

EDIT mode help:

```
PS C:\OWT_Bandit_AutoPwn> python .\main.py edit -h
usage: main.py edit [-h] [-p PASSWORD] [-t FOLDER] [-n NOTE] [-s SSHKEY] user

positional arguments:
  user                  📜​ Target user (optional)

options:
  -h, --help            show this help message and exit
  -p PASSWORD, --password PASSWORD
                        Change password
  -t FOLDER, --temp-folder FOLDER
                        Change temp folder
  -n NOTE, --notes NOTE
                        Change notes
  -s SSHKEY, --sshkey SSHKEY
                        Change sshkey
```

DELETE mode help:

```
PS C:\OWT_Bandit_AutoPwn> python .\main.py delete -h
usage: main.py delete [-h] [-p] [-t] [-n] user

positional arguments:
  user               📜​ Target user (optional)

options:
  -h, --help         show this help message and exit
  -p, --password     Delete password
  -t, --temp-folder  Delete temp folder
  -n, --notes        Delete notes
```

LIST mode help:

```
PS C:\OWT_Bandit_AutoPwn> python .\main.py list -h  
usage: main.py list [-h] [-s] [-p] [-d] [-t] [-u] [-f] [-n] [user]

positional arguments:
  user               📜​ Target user (optional)

options:
  -h, --help         show this help message and exit
  -s, --users        List users
  -p, --password     List passwords
  -d, --details      List details
  -t, --tags         List tags
  -u, --url          List URLs
  -f, --temp-folder  List temp folders asigned to users
  -n, --notes        List notes
```

EXPORT mode help:

```
PS C:\OWT_Bandit_AutoPwn> python .\main.py export -h
usage: main.py export [-h] [-p PDF_FILE] [-e EXCEL_FILE] [-f FIELDS] [user]

positional arguments:
  user                  📜​ Target user (optional)

options:
  -h, --help            show this help message and exit
  -p PDF_FILE, --pdf PDF_FILE
                        Export to PDF
  -e EXCEL_FILE, --excel EXCEL_FILE
                        Export to Excel
  -f FIELDS, --fields FIELDS
                        Fields to export: "user","password","details","tags","url","sshkey","temp_folder","notes"
```


## 📂 Project Structure

```
📁 OTW_Bandit_AutoPwn
 ├── lib/
 │    ├── arg_utilities.py
 │    ├── check_modules.py
 │    ├── constants.py
 │    ├── data_utilites.py
 │    ├── exploitation_chain.py
 │    ├── export_utilities.py
 │    ├── json_manage.py
 │    ├── local_utilities.py
 │    ├── menu.py
 │    ├── recursive_file_decompressor.py
 │    ├── remote_utilities.py
 │    ├── ssh_utilities.py
 │    └── utilities.py
 ├── utils/
 │    ├── .info.json
 │    ├── bandit21_password.sh
 │    ├── host_scan.sh
 │    └── port_scan.sh
 ├── .gitignore
 ├── main.py
 ├── README.md
 └── requirements.txt
```

## 🧩 Roadmap / TODO

- Improve edit mode
- Improve list menu
- Improve menu

## 📝 License

MIT License — free to use and modify.\

## 🐾 Follow Me / Contact

- 💻 GitHub: [ElCyberCurioso](https://github.com/ElCyberCurioso)
- 🐦 Twitter: [@ElCyberCurioso](https://twitter.com/ElCyberCurioso)
- 🔗 LinkedIn: [ElCyberCurioso](www.linkedin.com/in/sebastian-adrian-craciun-6164439a)

