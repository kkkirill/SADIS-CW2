import socket
from pickle import loads
from tkinter import Tk, END, DISABLED, Label, Entry
from typing import List

from src.drawer import Drawer
from src.models.feedback import Feedback


class ExpertMenu:
    def __init__(self, server_socket: socket.socket, root: Tk, common_menu):
        self.root = root
        self.sock = server_socket
        self.common_menu = common_menu

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
        self.t_total_amount_label['text'] = str(goals_amount)
        for i, goal in enumerate(goals, start=1):
            self.t_goals_list.insert(END, f'{i}) {goal}')
        self.t_exit_button.bind('<Button-1>', lambda _: self.call_expert_menu(), '+')
        self.draw_table(goals_amount)

    def draw_table(self, amount: int):
        step = 40
        step2 = 30
        for num in range(1, amount + 1):
            setattr(self, f'self.t_{num}_label', Label(text=f"{num}"))
            getattr(self, f'self.t_{num}_label').place(x=500 + step*num, y=75, width=30, height=15)
        print(amount, amount**2)
        for num in range(1, amount + 1):
            setattr(self, f'self.t_{num + amount + 1}_label', Label(text=f"{num}"))
            getattr(self, f'self.t_{num + amount + 1}_label').place(x=500, y=75 + step2*num, width=30, height=15)
        for num in range(1, amount + 1):
            for num1 in range(1, amount + 1):
                setattr(self, f'self.t_{num}{num1}_input', Entry(font='Arial 12'))
                getattr(self, f'self.t_{num}{num1}_input').place(x=500 + step*num1, y=75 + step2*num, width=30, height=15)
                if num == num1:
                    getattr(self, f'self.t_{num}{num1}_input').configure(state='readonly')

        pass
