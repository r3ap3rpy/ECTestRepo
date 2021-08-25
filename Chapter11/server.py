import http.server
import socketserver
import signal
#python3.8 -m http.server 8000
port = 8000

signal.signal(signal.SIGINT, signal.SIG_DFL)

Handler = http.server.SimpleHTTPRequestHandler

def server_init():
	http_daemon = socketserver.TCPServer(('192.168.1.6',port), Handler)
	print(f"The server is now listening on the port: {port}")
	http_daemon.serve_forever()

if __name__ == '__main__':
	server_init()
