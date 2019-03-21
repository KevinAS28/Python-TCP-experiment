import socket
import os
from threading import Thread
import time
spab = lambda x: [print(" ") for i in range(x)]
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#special 80
ip = "192.168.43.172"
ipp = ""
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
 with open("/root/programming/python_saya/tcp/biar_ga_lupa/loginnet.html", "rb") as oke:
  with open("/root/programming/python_saya/tcp/biar_ga_lupa/loginnet.css", "rb") as eko:#with open("/root/programming/html_saya/index_files/index.css", "rb") as eko:
   with open("/root/programming/python_saya/tcp/biar_ga_lupa/hell1.jpg", "rb") as gm:
   
    wow = oke.read()
    oww = eko.read()
    gmm = gm.read()
    post = False
    get = False
    the_data = terima.split()
    for i in the_data:
     if "POST" in i:
      post = True
     if "GET" in i:
      get = True
    if post and get:
     print("error. post and get is true")
     client_socket.close()
     

    for i in the_data:
     if "login-firewall.css" in i:
      client_socket.send(oww)
      client_socket.close()
      return
     if "hell1.jpg" in i:
      client_socket.send(gmm)
      client_socket.close()

      return
     if "loginnet.css" in i:
      client_socket.send(oww)
      client_socket.close()

      return

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
 
