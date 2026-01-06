import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print("\nFriend:", message)
        except:
            break

thread = threading.Thread(target=receive_messages)
thread.start()

while True:
    message = input("You: ")
    client_socket.send(message.encode())

    if message.lower() == "exit":
        break

client_socket.close()
