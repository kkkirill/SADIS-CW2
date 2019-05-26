import socket
from tkinter import Tk, PhotoImage, Label, Image
from src.authorization import AuthorizationMixin
from src.drawer import Drawer
from src.menus.user_menu import UserMenu
from src.menus.admin_menu import AdminMenu
from src.menus.expert_menu import ExpertMenu
ENC_FORMAT = 'utf-8'


class Interface(AuthorizationMixin):
    def __init__(self):
        self.sock = socket.socket()
        self.admin_menu, self.expert_menu, self.user_menu = None, None, None
        super(Interface, self).__init__(self.sock)
        self.sock.connect(("127.0.0.1", 14900))
        print(self.sock.recv(64).decode(ENC_FORMAT))
        self.root = Tk()
        self.root.title("Клиент")
        self.root.geometry("1020x620")

        self.root.update_idletasks()
        width = self.root.winfo_width()
        frm_width = self.root.winfo_rootx() - self.root.winfo_x()
        win_width = width + 2 * frm_width
        height = self.root.winfo_height()
        titlebar_height = self.root.winfo_rooty() - self.root.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.root.winfo_screenwidth() // 2 - win_width // 2
        y = self.root.winfo_screenheight() // 2 - win_height // 2
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.deiconify()

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
        self.admin_menu = AdminMenu(self.sock, self.root, self.common_menu, super(Interface, self))
        self.admin_menu.call_admin_menu()

    @Drawer.remove_prev_tags
    @Drawer.show_expert_menu
    def call_expert_menu(self):
        pass

    def show_any_menu(self):
        if hasattr(self, 'account') and self.account:
            print(self.account.role)
            if self.account.role == 0:
                self.call_user_menu()
            elif self.account.role == 1:
                self.call_expert_menu()
            elif self.account.role == 2:
                self.call_admin_menu()

    @Drawer.remove_prev_tags
    @Drawer.show_login_menu
    def login_wrapper(self):
        self.t_submit_button.bind('<Button-1>', lambda _: self.show_any_menu() if self.login_validation() else None, '+')
        self.t_cancel_button.bind('<Button-1>', lambda _: self.common_menu(), '+')

    @Drawer.remove_prev_tags
    @Drawer.show_registration_menu
    def register_wrapper(self):
        self.t_submit_button.bind('<Button-1>', lambda _: self.show_any_menu() if self.registration_validation(self) else None, '+')
        self.t_cancel_button.bind('<Button-1>', lambda _: self.common_menu(), '+')

    @Drawer.remove_prev_tags
    @Drawer.show_start_menu
    def common_menu(self):
        self.t_login_button.bind('<Button-1>', lambda _: self.login_wrapper())
        self.t_register_button.bind('<Button-1>', lambda _: self.register_wrapper())
        self.t_exit_button.bind('<Button-1>', lambda _: self.close())

    @staticmethod
    def mainloop():
        Image.core.eventloop()

    @Drawer.remove_prev_tags
    def close(self):
        self.sock.send('exit'.encode(ENC_FORMAT))
        exit(0)


if __name__ == '__main__':
    interface = Interface()
