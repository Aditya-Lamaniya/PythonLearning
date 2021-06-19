import socket
s=socket.socket()

s.connect(("127.0.0.1",80))

message=s.recv(1024)

while message:
    print("received :",message.decode())
    message=s.recv(1024)

s.close()