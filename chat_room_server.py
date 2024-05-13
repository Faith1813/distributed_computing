#Nomes: Júlia Rampani, Lucas Kenzo Kawamoto
#TIA: 42119529, 42145651

import socket
import threading

host = '127.0.0.1'
port = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} saiu da sala!'.encode('utf-8'))
            aliases.remove(alias)
            break

def receive():
    while True:
        print("Server esta rodando e escutando ...")
        client, address = server.accept()
        print(f'Conexao estabelecida com: {str(address)}')
        client.send('Nome de usuario?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'O nome de usuario deste cliente eh: {alias.decode("utf-8")}')
        broadcast(f'{alias.decode("utf-8")} se conectou a sala'.encode('utf-8'))
        client.send('Voce agora esta conectado!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client, ))
        thread.start()  # Inicie a thread aqui

if __name__ == '__main__':
    receive()



