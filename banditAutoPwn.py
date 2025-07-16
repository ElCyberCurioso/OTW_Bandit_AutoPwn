#!/usr/bin/python3

import paramiko, os, time
import lib.recursive_file_decompressor as decompressor

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