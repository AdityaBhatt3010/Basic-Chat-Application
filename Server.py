import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}  # Dictionary to store clients {nickname: socket}

def broadcast(message, sender=None):
    # Broadcast messages to all clients except sender (for leave messages).
    for nickname, client in clients.items():
        if client != sender:
            try:
                client.send(message.encode('ascii'))
            except:
                remove_client(nickname)

def remove_client(nickname):
    # Remove client and notify others.
    client = clients.pop(nickname, None)
    if client:
        client.close()
        broadcast(f"{nickname} left the chat.")

def handle_client(client, nickname):
    # Handle messages from a single client.
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if not message:
                break  # Handle client disconnecting
            broadcast(f"{nickname}: {message}")
        except:
            break  # Handle client disconnecting unexpectedly
    remove_client(nickname)

def receive():
    #Accept and manage new clients.
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')

        if not nickname or nickname in clients:
            client.send("Invalid or duplicate nickname. Try again.".encode('ascii'))
            client.close()
            continue

        clients[nickname] = client
        print(f"Nickname: {nickname}")
        broadcast(f"{nickname} joined the chat.")
        client.send("Connected to the server!".encode('ascii'))

        threading.Thread(target=handle_client, args=(client, nickname), daemon=True).start()

print("Server is running...")
receive()
