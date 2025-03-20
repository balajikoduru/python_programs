import socket
c=socket.socket()
c.connect(("localhost",8080))
name=input("enter the client name:")
c.send(bytes(name,"utf-8"))
print(c.recv(1024).decode())

