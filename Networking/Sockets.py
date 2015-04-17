import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

print(s)

server = 'pythonprogramming.net'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP1.1\nHost: "+server+"\n\n"

s.connect((server,port))
s.send(request.encode()) #  Encriptamos la infromacion que queremos pasar
result = s.recv(4096) #  Buffer: cantidad de informacion que resivimos

#print(result)

while (len(result) > 0):
	print(result)
	result = s.recv(4096)