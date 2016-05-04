import socket


while 1:
    men = raw_input("My:\t")
    s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    s.sendto(men,  ("localhost" , 5005))
    s.close()

while 1:
    wen = raw_input("wtf:\t")
    ss = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
