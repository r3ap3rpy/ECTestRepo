import socket

class MySocket:
    """ This is a basic socket class demo!
    """
    def __init__(self, sock = None):
        self.is_alive = False
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
    def connect(self, host, port):
        try:
            self.sock.connect((host,int(port)))
            self.is_alive = True
        except Exception as e:
            self.is_alive = False
            print("Could not connect to host: {host} on port: {port}, because: {e}")
    def send(self, msg):
        if self.is_alive:
            totalsent = 0
            MSGLEN = len(msg)
            while totalsent < MSGLEN:
                sent = self.sock.send(msg[totalsent:])
                if sent == 0:
                    raise RuntimeError(f"Socket is broken!")
                totalsent += sent
        else:
            print(f"The socket is not connected, cannot send the message!")
    def recieve(self):
        if self.is_alive:
            chunks = []
            bytes_recvd = 0
            while bytes_recvd < MSGLEN:
                chunk = self.sock.recv(min(MSGLEN -bytes_recvd,2048))
                if chunk == b"":
                    raise RuntimeError("The connection is broken!")
                chunks.append(chunk)
                bytes_recvd += len(chunk)
        else:
            print(f"The socket is not connected, cannot recieve!")