import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target = {"satu": ("192.168.100.3", 443), "dua":("192.168.43.1", 3730), "tiga": ("10.42.0.1", 80)}
client.connect(target["dua"])
client.send("wow banget".encode("utf-8"))
print(client.recv(4096).decode("utf-8"))
client.close()

