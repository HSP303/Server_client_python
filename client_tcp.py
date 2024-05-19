import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)

try:

    client.connect(("10.0.2.15", 4433))

    client.send(b"HELLO\n")

    pacotes_recebidos = client.recv(1024).decode()

    print(pacotes_recebidos)

except:
    print('Um erro ocorreu!!!')
