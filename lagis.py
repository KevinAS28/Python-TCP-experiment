#!/usr/bin/python

import socket
import time
import random
from random import random

#membuat socket object
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#membuat port dan hostname
hostn = socket.gethostname()
print(hostn)
port = 8888

#membuat buta port dan hostname

ser.bind( (hostn, port) )
ser.listen()
print("""


mendengarkan port dan hostname""")

while True:
 client,addr = ser.accept()
 print("wow dapat koneksi dari %s" %str(addr))
 oke = "balok"
 client.send(oke.encode("ascii"))
 
