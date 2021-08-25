import socket
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
# 0x0800 -> Only IP captured
# 0x0300 -> Everything captured
s.bind(("ens33",3))
