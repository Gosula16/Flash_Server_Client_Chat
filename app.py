from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username:
            return redirect(f'/chat?username={username}')
    return render_template('login.html')

@app.route('/chat')
def chat():
    username = request.args.get('username')
    if not username:
        return redirect('/login')
    return render_template('chat.html', username=username)

@app.route('/code')
def code():
    return render_template('code.html')

@socketio.on('message')
def handle_message(data):
    # `data` is a dictionary that includes 'username' and 'message'
    username = data.get('username', 'Anonymous')
    msg = data.get('message', '')
    full_message = f"{username}: {msg}"
    emit('message', full_message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
