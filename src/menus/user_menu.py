import datetime
import socket
import time
from copy import copy
from pickle import dumps, load, loads
from tkinter import Tk, END, messagebox, DISABLED
from typing import List

from src.models.accounts import Account
from src.drawer import Drawer
from src.models.feedback import Feedback
from src.models.order import Order


class UserMenu:
    def __init__(self, account: Account, server_socket: socket.socket, root: Tk, common_menu, autorization):
        self.root = root
        self.sock = server_socket
        self.common_menu = common_menu
        self.account = account
        self.autorization = autorization

    @Drawer.remove_prev_tags
    @Drawer.show_user_menu
    def call_user_menu(self):
        self.t_make_order_button.bind('<Button-1>', lambda _: self.make_order(), '+')
        self.t_my_orders_button.bind('<Button-1>', lambda _: self.my_orders(), '+')
        self.t_my_account_button.bind('<Button-1>', lambda _: self.my_account(), '+')
        self.t_leave_feedback_button.bind('<Button-1>', lambda _: self.leave_feedback(), '+')
        self.t_exit_button.bind('<Button-1>', lambda _: self.exit(), '+')

    @Drawer.remove_prev_tags
    def exit(self):
        self.common_menu()

    @Drawer.remove_prev_tags
    @Drawer.add_order
    def make_order(self):
        self.t_make_order_button.bind('<Button-1>', lambda _: self.real_make_order(), '+')
        self.t_exit_button.bind('<Button-1>', lambda _: self.call_user_menu(), '+')

    def real_make_order(self):
        self.sock.send('add_orders'.encode())
        try:
            datetime.datetime.strptime(self.t_deadline_input.get(), '%d.%m.%Y')
        except ValueError:
            messagebox.showerror(message='Введена неправильная дата. Формат даты: ##.##.####')
            return
        order = Order(self.account,
              self.t_platform_input.get(),
              self.t_deadline_input.get(),
              self.t_topic_input.get(),
              self.t_description_input.get(1.0, END),
              self.is_promotion_enabled.get() == 0)
        self.sock.send(dumps(order))
        self.call_user_menu()

    @Drawer.remove_prev_tags
    @Drawer.show_orders
    def my_orders(self):
        self.sock.send('get_orders'.encode())
        self.sock.send(dumps(self.account))
        temp = loads(self.sock.recv(8196))
        if temp != 'None':
            orders = list(temp)
            total_sum = 0
            for order in orders:
                self.t_orders_list.insert(END, order.topic)
                total_sum += order.cost
            self.t_total_sum_label['text'] = str(total_sum)
            self.t_orders_list.bind('<<ListboxSelect>>', lambda e: self.on_order_choosed(orders[e.widget.curselection()[0]]) if e.widget.curselection().__len__() else None)
            self.t_delete_button.bind('<Button-1>', lambda _: self.on_order_delete(self.t_orders_list.curselection()[0]) if self.t_orders_list.curselection().__len__() else None)
        self.t_exit_button.bind('<Button-1>', lambda _: self.call_user_menu(), '+')

    @Drawer.remove_promotion_buttons
    @Drawer.remove_input_and_labels
    @Drawer.show_order
    def on_order_choosed(self, order):
        self.t_platform_input.insert(0, order.platform)
        self.t_platform_input.configure(state=DISABLED)
        self.t_deadline_input.insert(0, order.deadline)
        self.t_deadline_input.configure(state=DISABLED)
        self.t_topic_input.insert(0, order.topic)
        self.t_topic_input.configure(state=DISABLED)
        self.t_description_input.insert(1.0, order.description)
        self.t_description_input.configure(state=DISABLED)
        self.is_promotion_enabled.set(order.is_promoted)

    def on_order_delete(self, index: int):
        self.sock.send('remove_orders'.encode())
        time.sleep(0.000000001)
        self.sock.send(dumps(self.account))
        self.sock.send(str(index).encode())
        self.t_orders_list.delete(index)
        self.call_user_menu()

    @Drawer.remove_prev_tags
    @Drawer.show_my_account
    def my_account(self):
        self.t_login_input.insert(0, self.account.login)
        self.t_login_input.configure(state='readonly')
        self.t_password_input.insert(0, self.account.password)
        self.t_email_input.insert(0, self.account.email)
        self.t_fn_input.insert(0, self.account.fn.replace('_', ' '))
        self.t_phone_input.insert(0, self.account.phone)
        self.t_fax_input.insert(0, self.account.fax)
        self.t_edit_button.bind('<Button-1>', lambda _: self.save_changes_to_account_and_close(), '+')
        self.t_cancel_button.bind('<Button-1>', lambda _: self.call_user_menu(), '+')

    def save_changes_to_account_and_close(self):
        temp = [self.t_login_input.get(), self.t_password_input.get(),
                            self.t_email_input.get(), self.t_fn_input.get(), self.t_phone_input.get(), self.t_fax_input.get()]
        prev_acc = copy(self.account)
        prev_acc.fn = prev_acc.fn.replace(' ', '_')
        if self.autorization.registration_validation(self, role=0, autorization=self.autorization, flag=True):
            self.sock.send('change_accounts'.encode())
            time.sleep(0.000000001)
            self.sock.send(dumps(prev_acc))
            new_acc = [str(self.account.role), *temp]
            new_acc = '|'.join(new_acc)
            self.sock.send(new_acc.encode())
            self.call_user_menu()
        else:
            self.t_password_input.delete(0, END)
            self.t_password_input.insert(0, self.account.password)
            self.t_email_input.delete(0, END)
            self.t_email_input.insert(0, self.account.email)
            self.t_fn_input.delete(0, END)
            self.t_fn_input.insert(0, self.account.fn)
            self.t_phone_input.delete(0, END)
            self.t_phone_input.insert(0, self.account.phone)
            self.t_fax_input.delete(0, END)
            self.t_fax_input.insert(0, self.account.fax)

    @Drawer.remove_prev_tags
    @Drawer.add_feedbacks
    def leave_feedback(self):
        self.t_make_feedback_button.bind('<Button-1>', lambda _: self.real_leave_feedback(), '+')
        self.t_exit_button.bind('<Button-1>', lambda _: self.call_user_menu(), '+')


    def real_leave_feedback(self):
        feedbacks = [self.t_first_input.get(), self.t_second_input.get(), self.t_third_input.get(), self.t_forth_input.get()]
        feedback = Feedback(self.account, feedbacks)
        self.sock.send('add_feedbacks'.encode())
        self.sock.send(dumps(feedback))
        self.call_user_menu()