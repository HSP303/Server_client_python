import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    while True:
        msg = input("Mensagem: ") + "\n"
        client.sendto(msg.encode(), ("186.209.29.71", 1234))
        
        data, sender = client.recvfrom(1024)

        print(sender[0] + ": " + data.decode())

        if msg == 'exit\n':
            break
    
    client.clese()

except:
    print('Ocorreu algum erro!!!')
    client.clese()