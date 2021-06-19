import socket

host='127.0.0.1'
port=80

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
print("server listening on port :",port)
s.listen(1)

c,addr=s.accept()

filename=c.recv(1024)

try:
    f=open(filename,'rb')
    content=f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    c.send(b"file does not exist ")

c.close()

