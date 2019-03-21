import socket
import os
from threading import Thread
import time
spab = lambda x: [print(" ") for i in range(x)]
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#special 80
ip = "192.168.43.173"
server_socket.bind((ip, 80))
server_socket.listen()

#ayo tambahkan beberapa port dengan socket baru
sockobjct = ["socket.socket(socket.AF_INET, socket.SOCK_STREAM)", "socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)", "socket.socket(socket.AF_INET, socket.SOCK_DGRAM)"]
port = [443, 445, 5901, 21, 22, 23]
"""
for i in sockobjct:
 for a in port:
  to_bind = "%s.bind((ip, %d))" %(i, a)
  to_listen = "%s
"""
  
#tcp_ip, ping, udp






def client_handler(client_socket, info):
 terima = client_socket.recv(1024).decode("utf-8")
 print(info)
 print(terima)
 with open("/root/programming/html_saya/index.html", "rb") as oke:
  with open("/root/programming/html_saya/index.css", "rb") as eko:#with open("/root/programming/html_saya/index_files/index.css", "rb") as eko:
   with open("/root/programming/html_saya/index_files/kacang.jpg", "rb") as gm:
   
    wow = oke.read()
    oww = eko.read()
    gmm = gm.read()
    try:
     terima = terima.split()
     if "index.css" in (terima[(terima.index("GET")) + 1]):
      print("kirim css")
      client_socket.send(oww)
      client_socket.close()
      return
    except: 
     print("error saat css")
    if True:#try:
     #terima = terima.split()
     if "kacang.jpg" in (terima[(terima.index("GET")) + 1]):
      print("kirim jpg")
      client_socket.send(gmm)
      client_socket.close()
      return
    #except: 
    # print("error saat jpg")
    client_socket.send(wow)
    #client_socket.send(gmm)
    client_socket.close()
    #client_socket.send(oww)






while True:
   client, addr = server_socket.accept()
   print("*"*10)
   print(client)
   print("*"*10)
   if True:#for i in range(2):
    Thread(target=client_handler, args=[client, addr]).start()
   
 

#	 print("dapat koneksi dari %s:%d" %(addr[0], addr[1]))

  #Thread(target=client_handler1, args=[client, addr]).start()
 
