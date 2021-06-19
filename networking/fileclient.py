import socket

s=socket.socket()
s.connect(("127.0.0.1",80))

filename=input("enter a file name:  ")
s.send(filename.encode())
content=s.recv(1024)
print(content.decode())
s.close()