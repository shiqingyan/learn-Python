import socket
s=socket.socket()
host=socket.gethostname()
port=1234
print(host)
s.connect((host,port))
print(s.recv(1024).decode())
