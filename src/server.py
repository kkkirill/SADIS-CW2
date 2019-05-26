import socket
from threading import Thread
from src.file_reader import FileReader
from pathlib import Path

HOST = '0.0.0.0'
PORT = 14900
MAX_CLIENTS = 10
ENC_FORMAT = 'cp1251'
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

    def login(self, data: str) -> (str or None):
        accounts = self.file_manager.get_content_from_file(Path(STDPATH + 'accounts.txt'))
        if not accounts:
            return None
        data = data.split('|')
        login_values = list(map(lambda v: v.split(' '), accounts.split('|')))
        for value in login_values:
            if data == value[1:3]:
                return ' '.join(value)
        return None

    def register(self, data: str) -> (str or None):
        accounts = self.file_manager.get_content_from_file(Path(STDPATH + 'accounts.txt'))
        if not accounts:
            return None
        data = data.split('|')
        login_values = list(map(lambda v: v.split(' ')[1:], accounts.split('|')))
        if data not in login_values:
            self.file_manager.append_to_file('\n' + ' '.join(data), Path(STDPATH + 'accounts.txt'))
        return ' '.join(data)

    def remove_user(self, role: str, number: str):
        pure_accounts = self.file_manager.get_content_from_file(Path(STDPATH + 'accounts.txt')).split('|')
        accounts: list = list(filter(lambda value: value.startswith(role), pure_accounts))
        other_accounts: list = list(filter(lambda value: not value.startswith(role), pure_accounts))
        accounts.pop(int(number))
        accounts = accounts + other_accounts
        self.file_manager.write_to_accounts('\n'.join(accounts), Path(STDPATH + 'accounts.txt'))
        return '|'.join(accounts)

    def get_users(self, role: str):
        accounts = list(filter(lambda value: value.startswith(role), self.file_manager.get_content_from_file(Path(STDPATH + 'accounts.txt')).split('|')))
        return '|'.join(accounts) if accounts else 'None'

    def get_goals(self):
        goals = self.file_manager.get_content_from_file(Path(STDPATH + 'goals.txt'))
        print(goals)
        return goals if goals else 'None'

    def run(self):
        self.client_sock.send(f'Хост: {self.client_addr[0]} Порт: {self.client_addr[1]} Ваш номер: {self.number}'.encode(ENC_FORMAT))
        while True:
            choice = self.client_sock.recv(1024).decode(ENC_FORMAT)
            if choice == 'login':
                value = self.client_sock.recv(128).decode(ENC_FORMAT)
                self.client_sock.send(str(self.login(value)).encode(ENC_FORMAT))
            elif choice == 'registration':
                value = self.client_sock.recv(256).decode(ENC_FORMAT)
                self.client_sock.send(str(self.register(value)).encode(ENC_FORMAT))
            elif choice == 'get_accounts':
                value = self.client_sock.recv(16).decode(ENC_FORMAT)
                self.client_sock.send(str(self.get_users(value)).encode(ENC_FORMAT))
            elif choice == 'remove_accounts':
                value = self.client_sock.recv(16).decode(ENC_FORMAT).split('|')
                value = str(self.remove_user(value[0], value[1]))
                self.client_sock.send(value.encode(ENC_FORMAT))
            elif choice == 'get_goals':
                value = self.get_goals()
                self.client_sock.send(value.encode(ENC_FORMAT))
            elif choice == 'exit':
                self.close()
                break

    def close(self):
        if self.client_sock:
            print(f'Пользователь №{self.number} отключён')
            self.client_sock.close()


def main():
    server = SocketServer(HOST, PORT, MAX_CLIENTS)
    server.start()


if __name__ == '__main__':
    main()