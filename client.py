import socket
import time
from tkinter import Tk, PhotoImage, Label

from accounts import Account
from authorization import AuthorizationMixin
from drawer import Drawer
ENC_FORMAT = 'utf-8'


class Interface(AuthorizationMixin):
    def __init__(self):
        self.sock = socket.socket()
        super(Interface, self).__init__(self.sock)
        self.sock.connect(("127.0.0.1", 14900))
        print(self.sock.recv(64).decode(ENC_FORMAT))
        self.root = Tk()
        self.root.title("Клиент")
        self.root.geometry("1020x620")
        bg_image = PhotoImage(file="background1.png")
        label = Label(self.root, image=bg_image)
        label.pack()
        self.common_menu()
        self.root.mainloop()

    @Drawer.remove_prev_tags
    @Drawer.show_user_menu
    def call_user_menu(self):
        pass

    @Drawer.remove_prev_tags
    def call_admin_menu(self):
        pass

    @Drawer.remove_prev_tags
    def call_expert_menu(self):
        pass

    def login_validation(self):
        login = self.t_login_input.get()
        password = self.t_password_input.get()
        self.account = self.login(login, password)
        if self.account:
            print(self.account.role)
        else:
            print('Not success')
        pass

    @Drawer.remove_prev_tags
    @Drawer.show_login_menu
    def login_wrapper(self):
        self.t_submit_button.bind('<Button-1>', lambda _: self.login_validation())
        self.t_cancel_button.bind('<Button-1>', lambda _: self.common_menu())
        # self.authorization.login()
        pass

    @Drawer.remove_prev_tags
    @Drawer.show_registration_menu
    def register_wrapper(self):
        self.t_submit_button.bind('<Button-1>', lambda _: True)
        self.t_cancel_button.bind('<Button-1>', lambda _: self.common_menu())
        pass

    @Drawer.remove_prev_tags
    @Drawer.show_start_menu
    def common_menu(self):
        self.t_login_button.bind('<Button-1>', lambda _: self.login_wrapper())
        self.t_register_button.bind('<Button-1>', lambda _: self.register_wrapper())
        self.t_exit_button.bind('<Button-1>', lambda _: self.close())
        pass

    @staticmethod
    def mainloop():
        Image.core.eventloop()

    @Drawer.remove_prev_tags
    def close(self):
        self.sock.send('exit'.encode(ENC_FORMAT))
        exit(0)


def main():
    interface = Interface()

    # print(sock.recv(1024).decode('utf-8'))


if __name__ == '__main__':
    main()