#!/usr/bin/python3
import socket
import os
from get_values_html import get_file
from threading import Thread
ip = ""
port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen()

with open("file_upload.html", "rb") as oke:
 oke = oke.read()
def tulis(data):
 ber = "thefile"
 try:
  os.remove(ber)
 except:
  pass
 with open(ber, "wb") as tulis:
  tulis.write(data)
def client_handler(client_socket):
 terima = client_socket.recv(1024)
 print(terima)
 if b"Content-Type: multipart/form-data" in terima:
  print("ADA FILE")
  tulis(get_file(terima))
 client_socket.send(oke)
 client_socket.close()

while True:
 client, addr = server.accept()
 Thread(target=client_handler, args=[client]).start()
 
