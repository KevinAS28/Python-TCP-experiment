#!/usr/bin/python3

import socket

host = 'www.google.com'
port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

try:
 client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
except:
 pass

response = client.recv(4096)

print(response)
