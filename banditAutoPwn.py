#!/usr/bin/python3

import paramiko 

otw_bandit_ssh_url = "bandit.labs.overthewire.org"
otw_bandit_ssh_port = 2220

user = "bandit0"
password = "bandit0"

def ssh_connection(username, password):
	client = paramiko.SSHClient()
	
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.load_system_host_keys()

	client.connect(hostname=otw_bandit_ssh_url, port=otw_bandit_ssh_port, username=username, password=password)

	return client

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

def bandit12_13(client):

	next_user = "bandit12"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit13_14(client):

	next_user = "bandit13"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit14_15(client):

	next_user = "bandit14"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit15_16(client):

	next_user = "bandit15"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit16_17(client):

	next_user = "bandit16"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit17_18(client):

	next_user = "bandit17"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit18_19(client):

	next_user = "bandit18"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit19_20(client):

	next_user = "bandit19"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit20_21(client):

	next_user = "bandit20"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit21_22(client):

	next_user = "bandit21"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit22_23(client):

	next_user = "bandit22"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit23_24(client):

	next_user = "bandit23"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit24_25(client):

	next_user = "bandit24"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit25_26(client):

	next_user = "bandit25"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit26_27(client):

	next_user = "bandit26"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit27_28(client):

	next_user = "bandit27"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit28_29(client):

	next_user = "bandit28"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit29_30(client):

	next_user = "bandit29"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit30_31(client):

	next_user = "bandit30"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit31_32(client):

	next_user = "bandit31"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def bandit32_33(client):

	next_user = "bandit32"

	# Process to obtain the password
	stdin, stdout, stderr = client.exec_command("")
	next_password = stdout.read().decode().strip()

	client.close()

	return next_user, next_password

def printCredentials():
	print(f"[+] Credentials for {user}: {password}")

if __name__ == '__main__':
	# DEBUG
	user = "bandit12"
	password = "7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4"

	# user, password = bandit11_12(ssh_connection(user,password))
	# printCredentials()

	user, password = bandit12_13(ssh_connection(user,password))
	printCredentials()

	# user, password = bandit13_14(ssh_connection(user,password))
	# printCredentials()

	# user, password = bandit14_15(ssh_connection(user,password))
	# printCredentials()

	# user, password = bandit15_16(ssh_connection(user,password))
	# printCredentials()

	# user, password = bandit16_17(ssh_connection(user,password))
	# printCredentials()

	# user, password = bandit17_18(ssh_connection(user,password))
	# printCredentials()

	# user, password = bandit18_19(ssh_connection(user,password))
	# printCredentials()

	# user, password = bandit19_20(ssh_connection(user,password))
	# printCredentials()

	# user, password = bandit20_21(ssh_connection(user,password))
	# printCredentials()

	# user, password = bandit21_22(ssh_connection(user,password))
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