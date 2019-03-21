import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '172.217.24.4'
#ip = "127.0.0.1"
port = 80

client.connect((ip, port))
client.send('GET / HTTP/1.1\r\nAccept-Encoding: identity\r\nHost: 127.0.0.1\r\nUser-Agent: Python-urllib/3.5\r\nConnection: close\r\n\r\n'.encode('utf-8'))
print(client.recv(4096).decode('utf-8'))
