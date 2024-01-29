from socket import *


class client:
    def __init__(self, ip, port):
        self.cli = socket(AF_INET, SOCK_STREAM)
        self.cli.connect((ip, port))


    def connect_to_serv(self):
        msg = self.cli.recv(1024).decode('utf-8')
        if msg == 'connected':
            self.listen()
        else:
            exit()


    def sender(self, text):
        self.cli.send(text.encode('utf-8'))
        while self.cli.recv(1024).decode('utf-8') != 'getted':
            self.cli.send(text.encode('utf-8'))


    def listen(self):
        is_work = True
        while is_work:
            req = input('впишите сообщение')
            if req == 'disconnect':
                self.sender(req)
                print(self.cli.recv(1024).decode('utf-8'))
            else:
                self.sender(req)


client('192.168.0.83', 7000).connect_to_serv()