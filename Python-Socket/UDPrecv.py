import socket

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.bind(("localhost" , 5005))


while 1:
    data , addr = s.recvfrom(1024)
    print "Friend:\t%s " %data 


s.close()
