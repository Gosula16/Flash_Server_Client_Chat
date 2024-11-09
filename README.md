# Project Structure
Flash_Server_Client_Chat/
├── templates/
│   ├── login.html       # Login page template
│   ├── chat.html        # Chat room template
│   └── code.html        # Code snippets page template
├── app.py               # Main Flask application
└── README.md            # Project documentation


# Flash Server Client Chat

This is a real-time chat application built with Flask and Flask-SocketIO. It allows users to log in with a username and join a chat room where they can send and receive messages instantly.

## Features

- **User Login**: Users can enter a username to access the chat room.
- **Real-Time Messaging**: Messages are broadcast to all connected clients in real time.
- **Code Snippets**: Additional code page available to share or display code snippets (via `/code` route).

## Requirements

- Python 3.6 or higher
- Flask
- Flask-SocketIO

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Gosula16/Flash_Server_Client_Chat.git
   cd Flash_Server_Client_Chat
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install Flask Flask-SocketIO


python app.py


