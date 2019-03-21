import socket

def spab(x, y=" "):
 [print(y) for i in range(x)]
sock0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

sock0.bind(('', 1))
sock1.bind(('', 1))

sock0.listen()
sock1.listen()

def satu():
 
 
