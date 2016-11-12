# Writen by FileSec team originally
# at calhacks 2016 


import socketio
import eventlet
import eventlet.wsgi
import time
from flask import Flask, render_template

# establish the socket

sio = socket.Server(logger=True, async_mode=async_mode)
app = Flask(__name__)
app.wsqi_app = socketio.Middleware(sio,app.wsgi_app)
app.config['SECRET_KEY'] = 'secret!'
thread= None

@sio.on('user.auth')
def user_authReceived(sid, message):
	
	sio.emit('my reps', ,
		room=sid)


@sio.on('key.request')
def user_



@sio.on('key.send')
def send_key(sid,key):
	sio.emit('key_send_data', {'data': message})

@sio.on('disconnect')
def disconnect(sid):
	print('Client disconnected')


@sio.on('connect')
def connect(sid):
	print('User connected')


if __name__ == '__main__':
	if sio.async_mode == 'threading':
        # deploy with Werkzeug
        app.run(threaded=True)
    
