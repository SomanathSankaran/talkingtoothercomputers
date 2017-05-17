import socket

def serve():
    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(('', 8080))
    listener.listen(5)
    while True:
        s, addr = listener.accept()
        request = s.recv(10000)
        print 'request text:', request
        method, rest = request.split(' ', 1)
        path, rest = rest.split(None, 1)
        print 'method:', method
        print 'path:', path
        s.send('you asked to '+method+' '+path)
        s.close()

if __name__ == '__main__':
    serve()
