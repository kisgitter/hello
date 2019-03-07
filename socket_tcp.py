#coding = utf-8
import socket
import threading
from time import sleep

#socket server
def tcplink( sock,adr):
    print('Accept new connection from %s:%s...' % addr)
    print(sock)
    sock.send(b'Welcome!')
    while True:
        data =sock.recv( 1024 )
        sleep(1)
        if not data or data.decode('utf-8') =='exit':
            break
        sock.send(('Hello ,%s!'% data.decode( 'utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
addr = ('127.0.0.1',19890)
s.bind(addr)
s.listen(5)
print('waitting for connect......')
while True:
    sock ,adr = s.accept()
    t =threading.Thread( target=tcplink , args=(sock,adr) )
    t.start()

#socket client
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
addr = ('127.0.0.1',19890)
s.connect(addr)
print(s.recv(1024).decode('utf-8'))
for data in [b'Huskey',b'Cat',b'Monkey',b'Ebaoer']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()









