'use strict';

var io = require('socket.io').listen(5000);

//Connection Example
//{
//	deviceType: "mobile",
//  socket: socket
//}

var users = {};
var connections = {};
var pins = {};
var files = {};

io.on('connection', function(socket) {	
	socket.on('disconnect', function() {
		var userID = users[socket.id];
		var index = -1;
		for(var i = 0; i <connections[userID].length;i++){
			var connection = connections[userID][i];
			if(connect.socket.id == socket.id){
				index = i;
				break;
			}
		}
		if(index != -1){
			delete connections[userID][i];
		}
		console.log('User disconnected');
	});

	socket.on('user.auth', function(message) {
		console.log('User connected', message.userID);
		if(!(message.userID in connections)) {
			connections[message.userID] = []
		}
		connections[message.userID].push({
			deviceType: message.deviceType,
			socket: socket
		});
		users[socket.id] = message.userID;
	});

	socket.on('key.request', function(params) {
		console.log('User requested key', users[socket.id]);
		var userID = users[socket.id];
		connections[userID].forEach(function(connection) {
			if(connection.deviceType == "mobile")
			{
				files[userID] = params.files
				pins[userID] = params.pin
				connection.socket.emit("pin.request", params);
				return;
			}
		});
	});

	socket.on('pin.attempt',function(params){
		
		var userID = users[socket.id];
		connections[userID].forEach(function(connection){
			if(connection.deviceType == "mobile"){
				if (pins[userID] == params){
					console.log('User sent pin attempt', userID);
					connection.socket.emit("key.request",files[userID]);
					return;
				}
			}
		})
	});

	socket.on('key.send',function(params){
		var userID = users[socket.id];
		connections[userID].forEach(function(connection){
			if(connection.deviceType == "computer"){
				console.log('User requested a key to be passed', userID);
				connection.socket.emit("key.send",params.key);
				return;
			}
		})
	});
});