from socketserver import TCPServer,StreamRequestHandler
import socket
host=socket.gethostname()
class Handler(StreamRequestHandler):
    def handler(self):
        addr=self.request.getpeername()
        print('Got connection from',addr)
        self.wfile.write('Thank you for connecting')
        
server=TCPServer((host,1234),Handler)
print('ini')
server.serve_forever()

