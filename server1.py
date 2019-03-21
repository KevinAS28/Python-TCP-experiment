import socket
import os
from threading import Thread

target = '192.168.100.3'
port0 = 443

def listen():
 server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 ip = "192.168.100.3"
 port1 = 443
 server.bind((ip, port1))
 server.listen()

def handler():
 permintaan = client_socket.recv(1024)
 print('kabar: %s' %(permintaan))
 perintah = input('perintah: ')
 perintah = perintah.encode('utf-8')
 server.connect((target, port0))
 server.send(perintah)
 print(server.recv(1024))

listen()
handler()
