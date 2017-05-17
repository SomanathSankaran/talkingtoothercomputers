import socket
# see wsgiref.simple_server for a real implementation of a WSGI server

def serve(app):
    listener = socket.socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(('', 8080))
    listener.listen(5)
    while True:
        s, addr = listener.accept()
        print('server received connection from', addr)
        request = s.recv(10000)
        print('request we received:', request)
        method, rest = request.split(b' ', 1)
        path, rest = rest.split(None, 1)
        def start_response(status, headers):
            print('sending headers')
            headers = b'\r\n'.join([('HTTP/1.1 '+status).encode('ascii')] +
                                 [(k+': '+v).encode('ascii') for k, v in headers])
            print(headers)
            s.send(headers)
            s.send(b'\r\n\r\n')
        environ = {'REQUEST_METHOD': method.decode('ascii'),
                   "PATH_INFO": path.decode('ascii')}
        for data in app(environ, start_response):
            print('sending data')
            s.sendall(data.encode('utf-8'))
        s.close()

def demo_app(environ, start_response):
    start_response("200 OK", [('Content-Type','text/plain')])
    return ['You asked to '+environ['REQUEST_METHOD']+' '+environ['PATH_INFO'], ' and that is what we just did!']

if __name__ == '__main__':
    serve(demo_app)
