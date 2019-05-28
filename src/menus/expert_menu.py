import socket
from pickle import loads
from tkinter import Tk, END, DISABLED
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
        self.t_expert_mark_button.bind()
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
