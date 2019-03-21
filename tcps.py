#!/usr/bin/python

import time
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serversocket.TCPServer.allow_reuse_address = True
host = socket.gethostname()

port = 999
serversocket.bind( (host, port) )

serversocket.listen()
print("mendengarkan ip dan port secara berkala")

while True:
 clientsocket,addr = serversocket.accept()
 print("dapat koneksi dari ahhh %s " % str(addr) )
 currentTime = time.ctime(time.time()) + "\r\n"
 clientsocket.send(currentTime.encode('ascii'))
 clientsocket.close()
