import socket

s = socket.socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Note the double parens!
s.bind(('localhost', 4000))
s.listen(10)

while True:
    new_connection, _ = s.accept()
    new_connection.send(b'please enter joke\n')
    msg = new_connection.recv(1000)
    print('got incoming message:', msg)
    new_connection.send(b'ha ha that was funny\n')
