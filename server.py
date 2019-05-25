import socket
from threading import Thread
from file_reader import FileReader
from pathlib import Path

HOST = '0.0.0.0'
PORT = 14900
MAX_CLIENTS = 10
ENC_FORMAT = 'utf-8'
STDPATH = "data/"


class SocketServer(Thread):
    def __init__(self, server_host: str, server_port: int, server_max_clients=5):
        Thread.__init__(self)
        print(f'Запущен сервер на хосте: {HOST} и порте: {PORT}. Максимальное кол-во клиентов: {MAX_CLIENTS}')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = server_host
        self.port = server_port
        self.max_clients = server_max_clients
        self.sock.bind((HOST, PORT))
        self.sock.listen(server_max_clients)
        self.sock_threads = []
        self.counter = 0
        self.__stop = False

    def close(self):
        print(f'Сервер остановлен (Хост: {self.host}, Порт: {self.port})')
        for thr in self.sock_threads:
            thr.stop()
            thr.join()
        if self.sock:
            self.sock.close()
            self.sock = None

    def run(self):
        client_addr: str
        while not self.__stop:
            self.sock.settimeout(1)
            try:
                client_sock, client_addr = self.sock.accept()
            except socket.timeout:
                client_sock = None
            if client_sock:
                client_thr = SocketServerThread(client_sock, client_addr, self.counter)
                self.counter += 1
                self.sock_threads.append(client_thr)
                client_thr.start()
        self.close()

    def stop(self):
        self.__stop = True


class SocketServerThread(Thread):
    def __init__(self, client_sock: socket.socket, client_addr, number):
        Thread.__init__(self)
        print(f'Подключён пользователь №{number} - хост: {client_addr[0]}, порт: {client_addr[1]}')
        self.client_sock = client_sock
        self.client_addr = client_addr
        self.number = number
        self.file_manager = FileReader()

    def login(self, data: str) -> str:
        accounts = self.file_manager.get_accounts(Path(STDPATH + 'accounts.txt'))
        if not accounts:
            return ''
        data = data.split('|')
        login_values = list(map(lambda v: v.split(' '), accounts.split('|')))
        for value in login_values:
            if data == value[1:3]:
                return ' '.join(value)
        return ''

    def register(self, data: str) -> bool:
        accounts = self.file_manager.get_accounts(Path(STDPATH + 'accounts.txt'))
        if not accounts:
            return False
        data = data.split('|')
        login_values = list(map(lambda v: v.split(' ')[1:], accounts.split('|')))
        if data not in login_values:
            self.file_manager.append_to_accounts(" ".join(['2'] + data))
        return True

    def run(self):
        self.client_sock.send(f'Хост: {self.client_addr[0]} Порт: {self.client_addr[1]} Ваш номер: {self.number}'.encode(ENC_FORMAT))
        while True:
            choice = self.client_sock.recv(1024).decode(ENC_FORMAT)
            if choice == 'login':
                value = self.client_sock.recv(128).decode(ENC_FORMAT)
                self.client_sock.send(self.login(value).encode(ENC_FORMAT))
            elif choice == 'exit':
                self.close()
                break
            # TODO server work

    def close(self):
        if self.client_sock:
            print(f'Пользователь №{self.number} отключён')
            self.client_sock.close()


def main():
    server = SocketServer(HOST, PORT, MAX_CLIENTS)
    server.start()
    # server.stop()


if __name__ == '__main__':
    main()