import socket
import os

spab = lambda x: [print(" ") for i in range(x)]
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
sock.bind(('', 80))

if True:#try:
 while True:
  data = sock.recv(1024)
  ip_header = data[:20]
  ips = ip_header[-8:-4]
  #source = " %i.%i.%i.%i" %(ord(ips[0]), ord(ips[1]), ord(ips[2]). ord(ips[3]))
  #print(source)
  print(ip_header)
  dataa = ""
  for i in data:
   try:
    dataa += i.decode("utf-8")
   except:
    try:
     dataa += i.decode("utf-16")
    except:
     continue

  print(dataa)
  spab(5)
  print(data)
  with open("ping-log", "wb") as oke:
   oke.write(data)


  
#except:
#  print("gagal")
