import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1337))
s.send(b'GET / HTTP/1.1\r\n\r\n')
data = s.recv(1024)
print(data)
s.close()
