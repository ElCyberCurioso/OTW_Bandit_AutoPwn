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
cd OWT_Bandit_AutoPwn
python otw_bandit_autopwn.py --help
```

## 🎮 Requirements

- Python 3.10+
- Pandas
- Paramiko or SSH libraries (if required)
- Internet connection (for SSH access)

## 🕹️ How to Use

1️⃣ Run `otw_bandit_autopwn.py`\
2️⃣ Use the interactive menu to navigate (`otw_bandit_autopwn.py menu`) or with parameters (`otw_bandit_autopwn.py edit/delete/list/export/hack`)\
3️⃣ Add or edit users as needed (editor mode)\
3️⃣ List saved info\ (list mode)\
4️⃣ Let the tool automate level solving for you (hack mode)\

## 📂 Project Structure

```
📁 OTW_Bandit_AutoPwn
 ├── lib/
 │    ├── check_modules.py
 │    ├── constants.py
 │    ├── data_utilites.py
 │    ├── json_manage.py
 │    ├── recursive_file_decompressor.py
 │    └── utilities.py
 ├── utils/
 │    ├── .info.json
 │    ├── bandit21_password.sh
 │    ├── host_scan.sh
 │    └── port_scan.sh
 ├── .gitignore
 ├── exploitation_chain.py
 ├── menu.py
 ├── otw_bandit_autopwn.py
 └── README.md
```

## 🧩 Roadmap / TODO

- Improve edit mode
- Improve menu

## 📝 License

MIT License — free to use and modify.\

## 🐾 Follow Me / Contact

- 💻 GitHub: [ElCyberCurioso](https://github.com/ElCyberCurioso)
- 🐦 Twitter: [@ElCyberCurioso](https://twitter.com/ElCyberCurioso)
- 🔗 LinkedIn: [ElCyberCurioso](www.linkedin.com/in/sebastian-adrian-craciun-6164439a)

