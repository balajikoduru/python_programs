import socket
s=socket.socket()
print("socket created successfully")
s.bind(("localhost",8080))
s.listen(3)
print("waiting for the connection")
while True:
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print("connected from",addr,name)
    c.send(bytes("welocome to balaji server",'utf-8'))
    c.close()

