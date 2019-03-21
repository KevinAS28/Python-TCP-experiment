import socket

files = "index.html"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
 try:
   client.connect(("10.42.0.60", 80))


   with open(files, "rb") as oke:
    files = oke.read()
    client.send((files))
    client.close()
 except:
  print("ga ada")
