import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.connect(("www.py4inf.com", 80))

'''The server uses virtual hosting, i.e. multiple host names on the same IP address. 
Therefore you must specify which host to access using a Host header.
Send takes a bytes parameter, use literal b.
The sequence "CR LF", as defined, will cause the NVT to be positioned at the left 
margin of the next print line (as would, for example, the sequence "LF CR").'''

mysocket.send(b"GET /code/romeo.txt HTTP/1.1\r\nHost: www.py4inf.com\r\n\r\n")

while True:
	data = mysocket.recv(512)
	if (len(data) < 1):
		break
	print(data)

mysocket.close()
