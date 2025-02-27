# Multi-Client Chat Application

A simple multi-client chat application using Python's `socket` and `threading` modules. This application allows multiple users to communicate in real-time over a local network.

## Features
✅ **Multi-Client Support** - Multiple users can join and chat simultaneously. <br/>
✅ **Nickname System** - Each user chooses a unique nickname. <br/>
✅ **Broadcast Messaging** - Messages are sent to all connected users. <br/>
✅ **Graceful Disconnection Handling** - Clients and server handle disconnects properly. <br/>
✅ **No Explicit Exit Break** - Supports the `/exit` command for graceful disconnection. <br/>
✅ **Optimized Performance** - Uses threading for concurrent handling. <br/>

## Installation
### Prerequisites
- Python 3.x installed

### Steps
1. **Clone this repository** (or download the files manually):
   ```bash
   git clone https://github.com/your-repo/chat-app.git
   cd chat-app
   ```
2. **Run the server**:
   ```bash
   python server.py
   ```
3. **Run the client** (open multiple terminals for multiple clients):
   ```bash
   python client.py
   ```
4. Enter a username when prompted, and start chatting!

## How It Works
### Server (`server.py`)
- Starts a TCP server on `127.0.0.1:55555`.
- Accepts connections and assigns nicknames.
- Manages message broadcasting.
- Removes disconnected clients and notifies others.

### Client (`client.py`)
- Connects to the server.
- Sends and receives messages in real-time.
- Allows users to type and send messages.
- Supports the `/exit` command for graceful disconnection.

## Example Usage
```
Client 1:
Choose your nickname: Alice
Alice joined the chat.
Alice: Hello everyone!

Client 2:
Choose your nickname: Bob
Bob joined the chat.
Bob: Hi Alice!
```
