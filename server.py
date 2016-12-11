
import socketserver
import random

class GibbetHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).decode()
        print('Client {} message {}'.format(self.client_address[0], self.data))

        if self.data == 'START':
            x = random.randint(1, 100)
            try_count = 10
            self.request.sendall(bytes('GUESS;1;100', 'utf-8'))
            while True:
                self.data = self.request.recv(1024).decode()
                resp = self.data.split(';')
                if resp[0] == 'TRY':
                    if int(resp[1]) == x:
                        self.request.sendall(bytes('TRUE', 'utf-8'))
                        print('Client {} win'.format(self.client_address[0]))
                        break
                    else:
                        try_count -= 1
                        if try_count == 0:
                            self.request.sendall(bytes('FAIL', 'utf-8'))
                            print('Client {} fail'.format(self.client_address[0]))
                            break
                        else:
                            if x < int(resp[1]):
                                self.request.sendall(bytes('FALSE;{};<'.format(try_count), 'utf-8'))
                            else:
                                self.request.sendall(bytes('FALSE;{};>'.format(try_count), 'utf-8'))
                            print('Client {}. Try count'.format(self.client_address[0]), try_count)
                elif resp[0] == 'GOODBYE':
                    self.request.sendall(bytes('GOODBYE', 'utf-8'))
                    break

HOST = 'localhost'
PORT = 9999

server = socketserver.TCPServer((HOST, PORT), GibbetHandler)
print('Server is started')
server.serve_forever()