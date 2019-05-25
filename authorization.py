import socket
from pickle import dumps
from accounts import Account
from drawer import Drawer

ENC_FORMAT = 'utf-8'


def from_list_to_account_dict(values: list) -> dict:
    account_titles = ('email', 'email', 'fn', 'phone', 'fax')
    return {account_titles[i]: value for i, value in enumerate(values)}


class AuthorizationMixin:
    def __init__(self, server_socket: socket.socket):
        self.socket = server_socket

    def login(self, login: str, password: str) -> (Account or None):
        self.socket.send('login'.encode(ENC_FORMAT))
        self.socket.send(f'{login}|{password}'.encode(ENC_FORMAT))
        account = self.socket.recv(64).decode(ENC_FORMAT)
        if account:
            account = account.split(' ')
            return Account(int(account[0]), *account[1:3], **from_list_to_account_dict(account[4:]))
        else:
            return None

    def registration(self, account: Account):
        self.socket.send('register'.encode(ENC_FORMAT))
        self.socket.send(dumps(account))
        flag = self.socket.recv(64)
        return True if flag == 'True' else False

    def logout(self, account: Account):
        pass
