import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

file = open("output.txt", "w")

try:
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print('Listening...')


    client_socket, address = server.accept()
    client_socket.settimeout(30)
   
    data = client_socket.recv(1048).decode()
    file.write(data)

    server.close()
except Exception as error:
    print('Erro de conexão')
    print('ERR: ', error)
    server.close()