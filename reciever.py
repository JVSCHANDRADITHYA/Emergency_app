import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 5000))

while True:
    data, addr = server.recvfrom(1024)
    print("Received:", data.decode())
