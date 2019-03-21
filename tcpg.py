#!/usr/bin/python3

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'www.google.com'
port = 80

client.connect( (host, port) )

client.send('GET / HTTP/1.1\r\nHost: google.com\r\n\r\n ')

respon = client.recv(4096)

print(respon)


