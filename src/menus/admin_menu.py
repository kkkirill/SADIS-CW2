import socket
from tkinter import Tk, END, Entry, Label, StringVar
from src.drawer import Drawer


class AdminMenu:
    def __init__(self, server_socket: socket.socket, root: Tk, common_menu, autorization):
        self.root = root
        self.sock = server_socket
        self.common_menu = common_menu
        self.autorization = autorization

    @Drawer.remove_prev_tags
    @Drawer.show_admin_menu
    def call_admin_menu(self):
        self.t_remove_users_button.bind('<Button-1>', lambda _: self.remove_account('0'), '+')
        self.t_manage_goals_button.bind('<Button-1>', lambda _: self.manage_goals(), '+')
        self.t_manage_experts_button.bind('<Button-1>', lambda _: self.manage_experts(), '+')
        self.t_exit_button.bind('<Button-1>', lambda _: self.exit(), '+')

    @Drawer.remove_prev_tags
    def exit(self):
        self.common_menu()

    @Drawer.remove_prev_tags
    @Drawer.show_manage_experts_menu
    def manage_experts(self):
        self.t_show_experts_button.bind('<Button-1>', lambda _: self.show_experts(), '+')
        self.t_add_experts_button.bind('<Button-1>', lambda _: self.add_expert(), '+')
        self.t_remove_experts_button.bind('<Button-1>', lambda _: self.remove_account('1'), '+')
        self.t_exit_button.bind('<Button-1>', lambda _: self.call_admin_menu(), '+')

    @Drawer.remove_prev_tags
    @Drawer.show_experts
    def show_experts(self):
        self.sock.send('get_accounts'.encode())
        self.sock.send('1'.encode())
        experts = self.sock.recv(512).decode().split('|')
        self.t_experts_list.bind('<<ListboxSelect>>', lambda e: self.on_expert_choosed(experts[e.widget.curselection()[0]]) if e.widget.curselection().__len__() else None)
        self.t_exit_button.bind('<Button-1>', lambda _: self.manage_experts(), '+')
        for expert in experts:
            self.t_experts_list.insert(END, expert.split(' ')[1])

    @Drawer.remove_input_and_labels
    def on_expert_choosed(self, value: str):
        if hasattr(self, 'prev_value') and self.prev_value == value:
            return
        self.prev_value = value
        value = value.split(' ')
        self.t_username_label = Label(text='Логин', font='Arial 12')
        self.t_username_label.place(x=500, y=75, height=30, width=200)
        self.t_username_input = Entry(textvariable=StringVar(value=value[1]), state='readonly')
        self.t_username_input.place(x=750, y=75, height=30, width=200)
        self.t_password_label = Label(text='Пароль', font='Arial 12')
        self.t_password_label.place(x=500, y=125, height=30, width=200)
        self.t_password_input = Entry(textvariable=StringVar(value=value[2]), state='readonly')
        self.t_password_input.place(x=750, y=125, height=30, width=200)
        self.t_email_label = Label(text='Почта', font='Arial 12')
        self.t_email_label.place(x=500, y=175, height=30, width=200)
        self.t_email_input = Entry(textvariable=StringVar(value=value[3]), state='readonly')
        self.t_email_input.place(x=750, y=175, height=30, width=200)
        self.t_fn_label = Label(text='ФИО', font='Arial 12')
        self.t_fn_label.place(x=500, y=225, height=30, width=200)
        self.t_fn_input = Entry(textvariable=StringVar(value=value[4]), state='readonly')
        self.t_fn_input.place(x=750, y=225, height=30, width=200)
        self.t_phone_label = Label(text='Телефон', font='Arial 12')
        self.t_phone_label.place(x=500, y=275, height=30, width=200)
        self.t_phone_input = Entry(textvariable=StringVar(value=value[5]), state='readonly')
        self.t_phone_input.place(x=750, y=275, height=30, width=200)
        self.t_fax_label = Label(text='Факс', font='Arial 12')
        self.t_fax_label.place(x=500, y=325, height=30, width=200)
        self.t_fax_input = Entry(textvariable=StringVar(value=value[6]), state='readonly')
        self.t_fax_input.place(x=750, y=325, height=30, width=200)

    @Drawer.remove_prev_tags
    @Drawer.show_registration_menu
    def add_expert(self):
        self.t_submit_button.bind('<Button-1>', lambda _: self.manage_experts() if self.autorization.registration_validation(self, '1', self.autorization) else None, '+')
        self.t_cancel_button.bind('<Button-1>', lambda _: self.manage_experts(), '+')

    @Drawer.remove_prev_tags
    @Drawer.remove_accounts
    def remove_account(self, role: str):
        self.sock.send('get_accounts'.encode())
        self.sock.send(role.encode())
        accounts = self.sock.recv(512).decode()
        if accounts and accounts != 'None':
            accounts = accounts.split('|')
            for account in accounts:
                self.t_accounts_list.insert(END, account.split(' ')[1])
            self.t_remove_button.bind('<Button-1>', lambda _: self.real_remove_account(role, self.t_accounts_list.curselection()[0]) if self.t_accounts_list.curselection().__len__() else None, '+')
        self.t_exit_button.bind('<Button-1>', lambda _: self.manage_experts() if role == '1' else self.call_admin_menu(), '+')

    def real_remove_account(self, role: str, number: int):
        self.sock.send('remove_accounts'.encode())
        self.sock.send(f'{role}|{number}'.encode())
        self.sock.recv(512).decode()
        self.t_accounts_list.delete(self.t_accounts_list.curselection())

    @Drawer.remove_prev_tags
    @Drawer.show_manage_goals_menu
    def manage_goals(self):
        self.t_show_goals_button.bind('<Button-1>', lambda _: self.show_goals(), '+')
        self.t_add_goals_button.bind('<Button-1>', lambda _: self.add_goal(), '+')
        self.t_remove_goals_button.bind('<Button-1>', lambda _: self.remove_goal(), '+')
        self.t_exit_button.bind('<Button-1>', lambda _: self.call_admin_menu(), '+')

    @Drawer.remove_prev_tags
    @Drawer.show_goals
    def show_goals(self):
        self.t_exit_button.bind('<Button-1>', lambda _: self.manage_goals(), '+')
        self.sock.send('get_goals'.encode())
        goals = self.sock.recv(512).decode().split('|')
        for goal in goals:
            self.t_goals_list.insert(END, goal)

    @Drawer.remove_prev_tags
    @Drawer.add_goal
    def add_goal(self):
        self.t_cancel_button.bind('<Button-1>', lambda _: self.manage_goals(), '+')
        self.t_submit_button.bind('<Button-1>', lambda _: True, '+')


    @Drawer.remove_prev_tags
    def remove_goal(self):
        pass
