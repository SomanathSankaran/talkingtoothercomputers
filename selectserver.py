import select
import socket

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', 1234))
server.listen(5)

clients = []

while True:
    ready_to_read, _, _ = select.select(clients + [server], [], [])
    for r in ready_to_read:
        if r is server:
            s, addr = server.accept()
            clients.append(s)
        else:
            msg = r.recv(1000)
            if not msg:
                r.close()
                clients.remove(r)
                continue
            _, ready_to_write, _ = select.select([], clients, [])
            for client in ready_to_write:
                if client is not r:
                    client.send(msg)
