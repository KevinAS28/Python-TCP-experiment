import socket
import sys
import time
import os
from threading import Thread

class serv:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        server.bind((ip, port))
        server.listen()
        print('halo... ada orang?')
        self.spab = (lambda x: [print('\n') for i in range(x)])
        
    def penanganan(self, client_socket):
        self.oke = client_socket.recv(1024)
        if (self.oke.decode('utf-8')) == 'start':
            asal = []
            for cba in range(12):
                while True:
                    lasa = random.randint(0, 53)
                    if lasa not in asal:
                        break
            print(asal)
        print(self.oke.decode('utf-8'))
        client_socket.send(b'gotcha')
        
    def run(self):
        while 1:
            client, addr = self.server.accept()
            print('terima ga ya... iya deh %s:%d' %(addr[0], addr[1]))
            wuff = Thread(target = self.penanganan, args=[client,])
            wuff.start()
            
if __name__ == '__main__':
    serv('192.168.100.3', 443).run()
        