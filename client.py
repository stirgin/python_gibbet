import socket

HOST = 'localhost'
PORT = 9999

print('Client game of "Death"')
print('Connect to {}:{}'.format(HOST, PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

sock.sendall(bytes('START', 'utf-8'))
received = sock.recv(1024).decode()

data = received.split(';')
if data[0] == 'GUESS':
    print('GUESS, {} to {}'.format(data[1], data[2]))
    while True:
        x = input('Your answer (q - to exit): ')
        if x == 'q':
            sock.sendall(bytes('GOODBYE', 'utf-8'))
            break

        sock.sendall(bytes('TRY;{}'.format(x), 'utf-8'))
        received = sock.recv(1024).decode()

        data = received.split(';')
        if data[0] == 'TRUE':
            print('TURUE')
            break
        elif data[0] == 'FAIL':
            print('FAIL')
            break
        elif data[0] == 'FALSE':
            if data[2] == '<':
                print('FALSE. <, try count: {}'.format(data[1]))
            elif data [2] == '>':
                print('FALSE. >, try count: {}'.format(data[1]))

sock.sendall(bytes('GOODBYE', 'utf-8'))
sock.close()
