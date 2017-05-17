import select
import socket
import sys

s = socket.socket()
s.connect(('thomasballinger.com', 1234))

while True:
    ready_to_read, _, _ = select.select([sys.stdin, s], [], [])
    for stream in ready_to_read:
        if stream is sys.stdin:
            msg = sys.stdin.readline()
            s.send(msg.encode('utf-8'))
        else:  # stream is the socket
            print(s.recv(1000))
            

