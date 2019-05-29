import socket
from itertools import combinations_with_replacement
from math import sqrt
from pickle import loads, dumps
from tkinter import Tk, END, DISABLED, Label, Entry, Spinbox, IntVar, StringVar
from typing import List

from src.drawer import Drawer
from src.models.accounts import Account
from src.models.feedback import Feedback


class ExpertMenu:
    def __init__(self, server_socket: socket.socket, root: Tk, common_menu, account: Account):
        self.root = root
        self.sock = server_socket
        self.common_menu = common_menu
        self.account = account
        self.mark_values = None

    @Drawer.remove_prev_tags
    @Drawer.show_expert_menu
    def call_expert_menu(self):
        self.t_expert_mark_button.bind('<Button-1>', lambda _: self.mark_goals(), '+')
        self.t_show_feedbacks_button.bind('<Button-1>', lambda _: self.show_feedbacks(), '+')
        self.t_exit_button.bind('<Button-1>', lambda _: self.exit(), '+')

    @Drawer.remove_prev_tags
    def exit(self):
        self.common_menu()

    @Drawer.remove_prev_tags
    @Drawer.show_feedbacks
    def show_feedbacks(self):
        self.sock.send('get_feedbacks'.encode())
        feedbacks: List[Feedback] = loads(self.sock.recv(16392))
        for feedback in feedbacks:
            self.t_feedbacks_list.insert(END, f'Отзыв от {feedback.account.login}')
        self.t_feedbacks_list.bind('<<ListboxSelect>>', lambda e: self.on_feedback_choosed(feedbacks[e.widget.curselection()[0]]) if e.widget.curselection().__len__() else None)
        self.t_exit_button.bind('<Button-1>', lambda _: self.call_expert_menu(), '+')

    @Drawer.remove_input_and_labels
    @Drawer.show_feedback
    def on_feedback_choosed(self, feedback: Feedback):
        self.t_first_input.insert(0, feedback.feedbacks[0])
        self.t_first_input.configure(state=DISABLED)
        self.t_second_input.insert(0, feedback.feedbacks[1])
        self.t_second_input.configure(state=DISABLED)
        self.t_third_input.insert(0, feedback.feedbacks[2])
        self.t_third_input.configure(state=DISABLED)
        self.t_forth_input.insert(0, feedback.feedbacks[3])
        self.t_forth_input.configure(state=DISABLED)

    @Drawer.remove_prev_tags
    @Drawer.draw_marks
    def mark_goals(self):
        self.sock.send('get_all_orders'.encode())
        orders: list = loads(self.sock.recv(16392))
        self.sock.send('get_goals'.encode())
        goals: list = self.sock.recv(16392).decode().split('|')
        goals_amount = len(goals)
        self.t_total_amount_label['text'] = f'Кол-во целей: {goals_amount}'
        for i, goal in enumerate(goals, start=1):
            self.t_goals_list.insert(END, f'{i}) {goal}')
        self.t_exit_button.bind('<Button-1>', lambda _: self.exit_from_table(goals_amount), '+')
        self.draw_table(goals_amount)

    @Drawer.remove_prev_tags
    def exit_from_table(self, amount: int):
        self.calculate_table(amount)
        for num in range(1, amount*2):
            getattr(self, f'self.t_{num}_label').destroy()
        try:
            for i, i1 in combinations_with_replacement(range(1, amount + 1), 2):
                getattr(self, f'self.t_{i}{i1}_input').destroy()
                getattr(self, f'self.t_{i1}{i}_input').destroy()
        except AttributeError:
            pass
        self.call_expert_menu()

    def calculate_table(self, amount: int):
        values = []
        keys = []
        try:
            for num in range(1, amount + 1):
                for num1 in range(1, amount + 1):
                    values.append(round(int(getattr(self, f'self.t_{num}{num1}_input').get()) / 900, 3))
                    keys.append(f'{num}{num1}')
        except AttributeError:
            pass
        total = sum(values)
        if total != 0:
            result_marks = [sum(values[i * amount:(i+1)*amount]) / total for i in range(amount)]
        else:
            result_marks = [0] * amount
        self.sock.send('write_marks'.encode())
        self.sock.send(dumps(self.account))
        self.sock.send(dumps(result_marks))

    def draw_table(self, amount: int):
        step = 60
        step2 = 45
        self.mark_values = [''] * (amount**2)
        for num in range(1, amount + 1):
            setattr(self, f'self.t_{num}_label', Label(text=f"{num}"))
            getattr(self, f'self.t_{num}_label').place(x=500 + step*num, y=75, width=40, height=20)
        for num in range(1, amount + 1):
            setattr(self, f'self.t_{num + amount}_label', Label(self.root, text=f"{num}"))
            getattr(self, f'self.t_{num + amount}_label').place(x=500, y=75 + step2*num, width=40, height=20)
        counter = 1
        for num in range(1, amount + 1):
            for num1 in range(1, amount + 1):
                setattr(self, f'self.t_{num}{num1}_input', Spinbox(self.root, from_=0, to=9000, font='Arial 12'))
                getattr(self, f'self.t_{num}{num1}_input').place(x=500 + step*num1, y=75 + step2*num, width=40, height=20)
                counter += 1
                if num == num1:
                    getattr(self, f'self.t_{num}{num1}_input').configure(state=DISABLED)

    def set_mark_value(self, i1: int, i2: int, counter: int):
        counter -= 1
        try:
            value = getattr(self, f'self.t_{i1}{i2}_input').get()
            self.mark_values[counter].set(value)
        except AttributeError:
            pass
        # print(self.mark_values[i1*i2])
