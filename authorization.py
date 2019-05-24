import socket
from pickle import dumps
from accounts import Account


enc_format = 'utf-8'


class Authentication:
    def __init__(self, server_socket: socket.socket):
        self.socket = server_socket

    def login(self, login: str, password: str):
        self.socket.send('login'.encode(enc_format))
        self.socket.send(f'{login}|{password}'.encode(enc_format))
        flag = self.socket.recv(64)
        if flag == 'True':
            account = self.socket.recv(1024)
            # TODO parse string to Account
            return account
        else:
            return None

    def registration(self, account: Account):
        self.socket.send('register'.encode(enc_format))
        self.socket.send(dumps(account))
        flag = self.socket.recv(64)
        return True if flag == 'True' else False

    def logout(self, account: Account):
        pass
