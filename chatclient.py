import socket

def main():
    s = socket.socket()
    s.connect(('123.456.789.012', 1234))
    while True:
        message_to_send = input('msg: ')
        if message_to_send:
            s.send(message_to_send.encode('ascii'))
        print(s.recv(1000))

main()
