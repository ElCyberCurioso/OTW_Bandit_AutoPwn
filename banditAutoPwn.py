#!/usr/bin/python3

import paramiko, os

import zipfile
import tarfile
import gzip
import bz2
import lzma
import py7zr
import shutil

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

def detect_compression_type(filepath):
    with open(filepath, 'rb') as f:
        file_start = f.read(264)

    if file_start.startswith(b'\x50\x4B\x03\x04'):
        return 'zip'
    if file_start.startswith(b'\x1F\x8B'):
        return 'gz'
    if file_start.startswith(b'\x42\x5A\x68'):
        return 'bz2'
    if file_start.startswith(b'\xFD\x37\x7A\x58\x5A\x00'):
        return 'xz'
    if file_start.startswith(b'\x37\x7A\xBC\xAF\x27\x1C'):
        return '7z'
    if len(file_start) >= 264 and file_start[257:262] == b'ustar':
        return 'tar'
    return None

def extract_zip(filepath, output_dir):
    with zipfile.ZipFile(filepath, 'r') as archive:
        archive.extractall(output_dir)

def extract_tar(filepath, output_dir, mode='r:*'):
    with tarfile.open(filepath, mode) as archive:
        archive.extractall(output_dir)

def extract_gz(filepath, output_dir):
    out_file = os.path.join(output_dir, os.path.splitext(os.path.basename(filepath))[0])
    with gzip.open(filepath, 'rb') as f_in, open(out_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

def extract_bz2(filepath, output_dir):
    out_file = os.path.join(output_dir, os.path.splitext(os.path.basename(filepath))[0])
    with bz2.open(filepath, 'rb') as f_in, open(out_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

def extract_xz(filepath, output_dir):
    out_file = os.path.join(output_dir, os.path.splitext(os.path.basename(filepath))[0])
    with lzma.open(filepath, 'rb') as f_in, open(out_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

def extract_7z(filepath, output_dir):
    with py7zr.SevenZipFile(filepath, mode='r') as archive:
        archive.extractall(path=output_dir)

def extract_file(filepath, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    filetype = detect_compression_type(filepath)

    if filetype == 'zip':
        extract_zip(filepath, output_dir)
    elif filetype == 'tar':
        extract_tar(filepath, output_dir, 'r:')
    elif filetype == 'tar.gz':
        extract_tar(filepath, output_dir, 'r:gz')
    elif filetype == 'tar.bz2':
        extract_tar(filepath, output_dir, 'r:bz2')
    elif filetype == 'tar.xz':
        extract_tar(filepath, output_dir, 'r:xz')
    elif filetype == 'gz':
        extract_gz(filepath, output_dir)
    elif filetype == 'bz2':
        extract_bz2(filepath, output_dir)
    elif filetype == 'xz':
        extract_xz(filepath, output_dir)
    elif filetype == '7z':
        extract_7z(filepath, output_dir)
    else:
        raise ValueError(f"❌ Tipo de archivo no soportado o no comprimido: {filepath}")

    print(f"✅ Extraído: {filepath} → {output_dir}")

def find_next_compressed_file(path):
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            if detect_compression_type(full_path):
                return full_path
    return None

def decompress_until_plain_text(initial_path, work_dir="temp_output"):
    current_path = os.path.abspath(initial_path)
    iteration = 0

    while True:
        filetype = detect_compression_type(current_path)

        if not filetype:
            print(f"🏁 Archivo final no comprimido detectado: {current_path}")
            break

        extract_dir = os.path.join(work_dir, f"step_{iteration}")
        extract_file(current_path, extract_dir)

        next_file = find_next_compressed_file(extract_dir)
        if not next_file:
            print(f"🏁 Archivo final extraído sin más compresión en: {extract_dir}")
            break

        current_path = next_file
        iteration += 1

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

    resources_path = createResourcesFolder()
    subfolder_path = createSubfolderOnResourcesFolder(resources_path, 'bandit12_13')
    
    # Funciona, descomentar al terminar el flujo
    # stdin, stdout, stderr = client.exec_command("mktemp -d")
    # temp_dir = stdout.read().decode().strip()
    
    # TEMPORAL, quitar antes de commitear
    # temp_dir = '/tmp/tmp.dOsroA9Mbo' # Sustituir por lo de arriba
    
    # client.exec_command('cat ~/data.txt | xxd -r > '+temp_dir+'/data')
    
    # sftp = client.open_sftp()
    # sftp.get(temp_dir+'/data',os.path.join(subfolder_path,'data.gz'))
    
    decompress_until_plain_text(os.path.join(subfolder_path,'data.gz'))
    
    next_password = 'PENDIENTE'

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