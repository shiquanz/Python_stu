#-*- coding:utf-8 -*-
#..

import sys , socket

print '这是一个服务器端层序'
server = ('localhost'  , 50015)

sock =  socket.socket(socket.AF_INET , socket.SOCK_STREAM)
sock.bind(server)
sock.listen(5)
conn , address = sock.accept()  
#accept是一个阻塞的程序 ,只有链接后才会执行下面代码

print 'connetc by ' , address

while True:
    data = conn.recv(1024)
    if not data:
        break
    print data
    conn.send(data)
#sock.close()
