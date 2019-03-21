#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 1112

if True:
 s.connect( (host, port) )
 tm = s.recv(1024)
 s.close()
 print("waktu %s" % tm.decode('ascii'))
