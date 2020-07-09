import logging
import os
import time
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('broadcast_event', namespace='/chat')
def chat_broadcast(msg):
    curr_time = time.time_ns()//1000000
    msg_obj = {
        'timestamp': f'{curr_time}',
        'username': msg['username'],
        'data': msg['data']
    }
    logger.info('broadcast msg_obj:', msg_obj)
    emit('my_response', msg_obj, broadcast=True)

@socketio.on('connect', namespace='/chat')
def chat_connect():
    emit('my_response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/chat')
def chat_connect():
    logger.info('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8100, debug=True)
