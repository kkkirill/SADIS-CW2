import socket
from validate_email import validate_email
from tkinter import messagebox

from src.accounts import Account

ENC_FORMAT = 'utf-8'


def from_list_to_account_dict(values: list) -> dict:
    account_titles = ('email', 'email', 'fn', 'phone', 'fax')
    return {account_titles[i]: value for i, value in enumerate(values)}


class AuthorizationMixin:
    def __init__(self, server_socket: socket.socket):
        self.socket = server_socket

    def login_validation(self):
        login = self.t_login_input.get()
        password = self.t_password_input.get()
        if login and password:
            self.account = self.login(login, password)
            return True
        messagebox.showerror(message='Введены неправильный логин и пароль')
        return False

    def login(self, login: str, password: str) -> (Account or None):
        self.socket.send('login'.encode(ENC_FORMAT))
        self.socket.send(f'{login}|{password}'.encode(ENC_FORMAT))
        account = self.socket.recv(256).decode(ENC_FORMAT)
        if account != 'None':
            account = account.split(' ')
            return Account(int(account[0]), *account[1:3], **from_list_to_account_dict(account[4:]))
        else:
            return None

    @staticmethod
    def registration_validation(self, role=2, autorization=None):
        login = self.t_login_input.get()
        password = self.t_password_input.get()
        email = self.t_email_input.get()
        fn = self.t_fn_input.get()
        phone = self.t_phone_input.get()
        fax = self.t_fax_input.get()
        if login and password and email and fn and phone and fax:
            if phone[1:].isdigit() and fax[1:].isdigit() and fn.count(' ') == 2 \
                    and validate_email(email) and login.isalnum() and password.isalnum():
                if autorization is None:
                    self.account = self.registration(role='0', login=login, password=password, email=email, fn=fn,
                                                     phone=phone, fax=fax)
                else:
                    self.account = self.autorization.registration(role=role, login=login, password=password, email=email, fn=fn,
                                                     phone=phone, fax=fax)
                if self.account is None:
                    messagebox.showerror(message='Ошибка регистрации! Данный логин занят!')
                else:
                    return True
        messagebox.showerror(message='Введены неправильные данные')
        return False

    def registration(self, **kwargs) -> (Account or None):
        self.socket.send('registration'.encode(ENC_FORMAT))
        value = '|'.join(kwargs.values())
        print(value)
        self.socket.send(value.encode(ENC_FORMAT))
        account = self.socket.recv(256).decode(ENC_FORMAT)
        if account != 'None':
            account = account.split(' ')
            return Account(int(account[0]), *account[1:3], **from_list_to_account_dict(account[4:]))
        else:
            return None

    def logout(self, account: Account):
        pass
