import socket

host='127.0.0.1'
port=80

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
print("server listening on port :",port)
s.listen(1)

c,addr=s.accept()

print("connection from :",str(addr))

c.send(b"hellow there, this is server test")
c.send("bye".encode())
c.close()


