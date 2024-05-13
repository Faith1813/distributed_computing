#Nomes: Júlia Rampani, Lucas Kenzo Kawamoto
#TIA: 42119529, 42145651

import socket
import threading

alias = input("Coloque seu nome de usuario: ")
port = 5000
host = '127.0.0.1'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))  

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'Nome de usuario?':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            client.close()
            break

def client_send():
    while True:
        message = input("")
        if message == "QUIT":
            print("Conversa foi finalizada")
            client.send(message.encode('utf-8'))
            break
        message = f'{alias}: {message}'
        client.send(message.encode('utf-8'))
    client.close()

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()

