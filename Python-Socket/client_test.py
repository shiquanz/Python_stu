#-*- coding:utf-8 -*-

import socket , sys , time
print '这是一个客户端程序'
server = ('localhost' , 50015)

sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.connect(server)

#user = raw_input("My:\t")
msg = ['hello' , 'welsdf' , 'xiaongming ' , 'sdfsdf' , 'lulilu']

#sock.send(user)
for m in msg:
    sock.send(m)
    data = sock.recv(1024)
    print data
    time.sleep(3)
#sock.close()

