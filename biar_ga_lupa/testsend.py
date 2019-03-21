import socket
import os
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "10.42.0.1"
port = 80

server.bind((ip, port))
server.listen()

def decor(*text):
 symb = "#"
 for i in text:
  print(symb*len(str(i)))
  print(i)
  print(symb*len(str(i)))
def client_handler(client_socket, info):
 terima = client_socket.recv(1024)
 decor("data from %s:%d\n" %(info[0], info[1]), terima.decode("utf-8"))
 with open("login-firewall.html", "rb") as oke:
  yeah = oke.read()
  client_socket.send(yeah)
 client_socket.close()

while True:
 try:
  client, addr = server.accept()
  Thread(target=client_handler, args=[client, addr]).start()
 except KeyboardInterrupt:
  print("OKE, BYE")
 
 
