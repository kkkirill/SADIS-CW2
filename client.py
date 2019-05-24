import socket
from accounts import Account
from authorization import Authentication


def user_menu():
    pass


def admin_menu():
    pass


def expert_menu():
    pass


def main():
    sock = socket.socket()
    sock.connect(("127.0.0.1", 14900))
    print(sock.recv(1024).decode('utf-8'))


if __name__ == '__main__':
    main()