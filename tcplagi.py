#!/usr/bin/python

import socket
import random



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1112

server.bind( (host, port) )

server.listen()
print("mendengar...")

while True:
 client,addr = server.accept()
 print("ada koneksi")
 msg = "ini adalah pesan tersembunyi"
 client.send(msg.encode("ascii"))
 server.close()
