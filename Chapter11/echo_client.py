import socket
import argparse

parser = argparse.ArgumentParser(description='Websocket client!')
parser.add_argument('--host','-host',metavar='host',type=str,nargs='?',default=socket.gethostname())
parser.add_argument('--port','-port',metavar='port',type=int,nargs='?',default=9999)
args = parser.parse_args()


print(f"Connecting to the server on IP: {args.host}, and port: {args.port}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sck:
    try:
        sck.connect((args.host, args.port))
    except Exception as e:
        raise SystemExit(f"Failure to connect to the remote host because: {str(e)}")
    while True:
        msg = input("What do you want to say: ")
        sck.sendall(msg.encode('utf-8'))
        if msg=='exit':
            break
        data = sck.recv(1024)
        print(f"The server said: {data.decode()}")