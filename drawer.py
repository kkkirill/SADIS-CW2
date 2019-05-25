from tkinter import Label, Image, Button, Entry
from functools import wraps

b_color = '#2C3337'
bf_color = '#F5FFFA'
font_family = 'Arial'


class Drawer:

    @staticmethod
    def show_start_menu(func):
        def wrapper(self, **kwargs):
            self.t_login_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Вход")
            self.t_login_button.place(x=400, y=200, height=30, width=200)
            self.t_register_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Регистрация")
            self.t_register_button.place(x=400, y=250, height=30, width=200)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Выход")
            self.t_exit_button.place(x=400, y=300, height=30, width=200)
            ret = func(self, **kwargs)
            return ret
        return wrapper

    @staticmethod
    def remove_start_menu(func):
        def wrapper(self, **kwargs):
            for value in filter(lambda value: value.startswith('t_'), dir(self)):
                getattr(self, value).destroy()
            ret = func(self, **kwargs)
            return ret
        return wrapper
    
    @staticmethod
    def show_login_menu(func):
        def wrapper(self, **kwargs):
            self.t_login_input = Entry()
            self.t_login_input.place(x=400, y=200, height=30, width=200)
            self.t_password_input = Entry(show="*")
            self.t_password_input.place(x=400, y=250, height=30, width=200)
            self.t_submit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Войти")
            self.t_submit_button.place(x=400, y=400, height=30, width=200)
            self.t_cancel_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Назад")
            self.t_cancel_button.place(x=400, y=450, height=30, width=200)
            ret = func(self, **kwargs)
            return ret
        return wrapper

    @staticmethod
    def show_registration_menu(func):
        def wrapper(self, **kwargs):
            self.t_login_input = Entry()
            self.t_login_input.place(x=400, y=200, height=30, width=200)
            self.t_password_input = Entry()
            self.t_password_input.place(x=400, y=250, height=30, width=200)
            self.t_submit_password_input = Entry()
            self.t_submit_password_input.place(x=400, y=300, height=30, width=200)
            self.t_submit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Зарегестрироваться")
            self.t_submit_button.place(x=400, y=400, height=30, width=200)
            self.t_cancel_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Назад")
            self.t_cancel_button.place(x=400, y=450, height=30, width=200)
            ret = func(self, **kwargs)
            return ret
        return wrapper

    @staticmethod
    def remove_prev_tags(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            for value in filter(lambda value: value.startswith('t_'), dir(self)):
                getattr(self, value).destroy()
            ret = func(self, **kwargs)
            return ret
        return wrapper

    @staticmethod
    def show_user_menu(func):
        def wrapper(self, **kwargs):
            self.t_label = Label(text='Hello', font=font_family)
            self.t_label.place(x=400, y=200, height=30, width=200)
            ret = func(self, **kwargs)
        return wrapper