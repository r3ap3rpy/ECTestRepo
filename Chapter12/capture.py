import socket
import struct
from fcntl import ioctl

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
s.bind(("ens33",3))

SOL_PACKET = 263
PACKET_ADD_MEMBERSHIP = 1
PACKET_MR_PROMISC = 1

def get_if(iff, cmd):
    sck = socket.socket()
    ifreq = ioctl(sck, cmd, struct.pack("16s16x",iff.encode("utf8")))
    sck.close()
    return ifreq
def get_if_index(iff):
    mreq = struct.pack("IHH8s",get_if_index(iff), PACKET_MD_PROMISC, 0, b"")
    s.setsockopt(SOL_PACKET, PACKET_ADD_MEMBERSHIP, mreq)
    return int(struct.unpack("I",get_if(iff, SIOCGIFINDEX)[16:20])[0])
pckt = s.recv(4096)

pckt = s.recv(4096)
eth_header = pckt[0:14]
eth_payload = pckt[14:]

dest, src, proto = unpack("!6s6sH", eth_header)