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
connections = []
pin = {};
fileData = {};
@sio.on('user.auth')
def user_authReceived(sid, message):

	for i in connections:
		if message.uid in connections[i].uid:
			connections[i].add_device(message.sid,message.deviceType)
			sio.emit('authenicated.linked',sid)
			return
		else:
 			connections.append(Device(messag.uid,sid, message.deviceType))
 			sio.emit("authenicated.new.device",sid)
 			return


@sio.on('pin.request') #start for chain reaction
def start_chain(sid,message):#message has file info and 1 or 0
	if refuse(sid):
		return
	for i in connections:
		if sid in connections[i].devices['computer']: #Only accept sid that is linked with computer
			if message.sid == connections[i].devices['computer']:
				#Send info to both the phone and computer
				 mobSid = connections[i].devices['mobile']
				fileData[moSid] = message;
				pinRequest(connections[i].devices['mobile'])
				pinDisplay(connectionss[i].devices['computer'])
				return

		
	sio.emit('failed-key-request-sid-not-match-connections',sid)
	return

#makeup in

def pinRequest(sid):
	pin[sid] = "1234"




@sio.on('pin.attempt')
def attempt_pin(sid,message):
	if refuse(sid):
		return
	e = message
	if e == pin[sid]:
		del pin[pid]
		data = 
		sio.emit('file.info',data,sid)
	else:
		sio.emit('failed.pin',data,sid)

@sio.on('key.request')
def key_request(sid,data):
	if refuse(sid):
		return
	for i in connections:
		if sid in connections[i].devices['mobile'] or sid in connections[i].devices['computer']:#check for sid in all devices
			if message.sid ==connections[i].devices['mobile']:
				sio.emit('key.request',"Requesting public key from Computer",connections[i].devices['computer'])
			else:
				sio.emit('key.request',"Requesting public key from Computer",connections[i].devices['mobile'])
			return
	#could not communicate with the other device
	sio.emit('failed-to-reach-other',"Failed to communicate to the other device",sid)


@sio.on('key.send')
def send_key(sid,key):
	if refuse(sid):
		return
	for i in connections:
		if sid in connections[i].devices['mobile'] or sid in connections[i].devices['computer']:
			if sid == connections[i].devices['mobile']:
				sio.emit('key.send',key,connections[i].devices['computer'])
			else:
				sio.emit('key.send',key,connections[i].devices['mobile'])
			return
	#could not communicate with the other device
	sio.emit('failed-to-reach-other',"Failed to communicate to the other device",sid)

@sio.on('disconnect')
def disconnect(sid):
	#remove the entries from the connections list
	if refuse(sid):
		return
	for i in connections:
		if sid in connections[i].devices['mobile'] or sid in connections[i].devices['computer']:
			if sid == connections[i].devices['mobile']:
				connections[i].remove_device['mobile'];
			else:
				connections[i].remove_device['computer'];
	print('Client disconnected')


@sio.on('connect')
def connect(sid):
	print('User connected')


def refuse(sid):#if both arent connected, run the refuse
	for i in connections:
		if sid in connections[i].devices['mobile'] or sid in connections[i].devices['computer']:
			if connections[i].devices['computer'] == None and connections[i].devices['mobile'] == None
				emit('refused',data,sid)
	return True

if __name__ == '__main__':
	if sio.async_mode == 'threading':
        # deploy with Werkzeug
        app.run(threaded=True)
    
