import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


port = 8080

serversocket.bind(('', port))
serversocket.listen(5)


while True:
	connection_object, address = serversocket.accept()
	print("Got connection from", address)
	connection_object.send(b"Thanks for connecting")
	connection_object.close()
	
