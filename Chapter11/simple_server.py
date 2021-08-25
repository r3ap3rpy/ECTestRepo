import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.6',8888))
s.listen()
connection, address = s.accept()
