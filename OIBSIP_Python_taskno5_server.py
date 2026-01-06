import socket
import threading

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen()

print("Server started. Waiting for clients...")

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)
        except:
            break

    clients.remove(client)
    client.close()

while True:
    client_socket, address = server_socket.accept()
    print("Client connected from", address)
    clients.append(client_socket)

    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
