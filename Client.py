import socket
import threading

nickname = input("Choose your nickname: ").strip()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(('127.0.0.1', 55555))
except ConnectionRefusedError:
    print("Unable to connect to the server. Ensure the server is running.")
    exit()

def receive():
    # Listen for messages from the server.
    try:
        while True:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
    except:
        print("Disconnected from server.")
        client.close()

def write():
    # Send messages to the server.
    try:
        while True:
            message = input().strip()
            if message.lower() == "/exit":
                client.close()
                break
            client.send(f"{nickname}: {message}".encode('ascii'))
    except:
        client.close()

receive_thread = threading.Thread(target=receive, daemon=True)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
