from tkinter import Label, Image, Button, Entry, StringVar, END, Listbox
from functools import wraps

b_color = '#2C3337'
bf_color = '#F5FFFA'
bh_color = '#e5e7ea'
bfh_color = '#2C3337'
font_family = 'Arial 12'


class Drawer:

    @staticmethod
    def hover_bind_button(*buttons):
        for button in buttons:
            button.bind('<Enter>', lambda e, b=button: Drawer.on_hover(b), '+')
            button.bind('<Leave>', lambda e, b=button: Drawer.on_leave(b), '+')

    @staticmethod
    def on_hover(button):
        button['background'] = bh_color
        button['foreground'] = bfh_color

    @staticmethod
    def on_leave(button):
        button['background'] = b_color
        button['foreground'] = bf_color

    @staticmethod
    def show_start_menu(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_login_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Вход")
            self.t_login_button.place(x=400, y=200, height=30, width=200)
            self.t_register_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Регистрация")
            self.t_register_button.place(x=400, y=250, height=30, width=200)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Выход")
            self.t_exit_button.place(x=400, y=300, height=30, width=200)
            Drawer.hover_bind_button(self.t_login_button, self.t_register_button, self.t_exit_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def remove_start_menu(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            for value in filter(lambda value: value.startswith('t_'), dir(self)):
                getattr(self, value).destroy()
            return func(self, **kwargs)
        return wrapper
    
    @staticmethod
    def show_login_menu(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_login_label = Label(text='Логин', font=font_family)
            self.t_login_label.place(x=400, y=150, height=30, width=200)
            self.t_login_input = Entry(font=font_family)
            self.t_login_input.focus()
            self.t_login_input.place(x=400, y=200, height=30, width=200)
            self.t_password_label = Label(text='Пароль', font=font_family)
            self.t_password_label.place(x=400, y=250, height=30, width=200)
            self.t_password_input = Entry(show="*", font=font_family)
            self.t_password_input.place(x=400, y=300, height=30, width=200)
            self.t_submit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Войти")
            self.t_submit_button.place(x=400, y=400, height=30, width=200)
            self.t_cancel_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Назад")
            self.t_cancel_button.place(x=400, y=450, height=30, width=200)
            Drawer.hover_bind_button(self.t_submit_button, self.t_cancel_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def show_registration_menu(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_login_label = Label(text='Логин', font=font_family)
            self.t_login_label.place(x=275, y=100, height=30, width=200)
            self.t_login_input = Entry(font=font_family)
            self.t_login_input.focus()
            self.t_login_input.place(x=525, y=100, height=30, width=200)

            self.t_password_label = Label(text='Пароль', font=font_family)
            self.t_password_label.place(x=275, y=150, height=30, width=200)
            self.t_password_input = Entry(font=font_family)
            self.t_password_input.place(x=525, y=150, height=30, width=200)

            self.t_email_label = Label(text='Почта', font=font_family)
            self.t_email_label.place(x=275, y=200, height=30, width=200)
            self.t_email_input = Entry(font=font_family)
            self.t_email_input.place(x=525, y=200, height=30, width=200)

            self.t_fn_label = Label(text='ФИО', font=font_family)
            self.t_fn_label.place(x=275, y=250, height=30, width=200)
            self.t_fn_input = Entry(font=font_family)
            self.t_fn_input.place(x=525, y=250, height=30, width=200)

            self.t_phone_label = Label(text='Телефон', font=font_family)
            self.t_phone_label.place(x=275, y=300, height=30, width=200)
            self.t_phone_input = Entry(font=font_family)
            self.t_phone_input.place(x=525, y=300, height=30, width=200)

            self.t_fax_label = Label(text='Факс', font=font_family)
            self.t_fax_label.place(x=275, y=350, height=30, width=200)
            self.t_fax_input = Entry(font=font_family)
            self.t_fax_input.place(x=525, y=350, height=30, width=200)

            self.t_submit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Зарегестрировать")
            self.t_submit_button.place(x=400, y=450, height=30, width=200)
            self.t_cancel_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Назад")
            self.t_cancel_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_submit_button, self.t_cancel_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def remove_prev_tags(func):
        @wraps(func)
        def wrapper(self, *args):
            for value in filter(lambda value: value.startswith('t_'), dir(self)):
                getattr(self, value).destroy()
            return func(self, *args)
        return wrapper

    @staticmethod
    def remove_input_and_labels(func):
        @wraps(func)
        def wrapper(self, *args):
            for value in filter(lambda value: value.startswith('t_') and (value.endswith('_input') or value.endswith('_label')), dir(self)):
                getattr(self, value).destroy()
            return func(self, *args)
        return wrapper

    @staticmethod
    def show_user_menu(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_label = Label(text='User', font=font_family)
            self.t_label.place(x=400, y=200, height=30, width=200)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def show_admin_menu(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_label = Label(text='Меню администратора', font=font_family)
            self.t_label.place(x=400, y=100, height=30, width=200)
            self.t_remove_users_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Удалить пользователей")
            self.t_remove_users_button.place(x=400, y=200, height=30, width=200)
            self.t_manage_goals_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Управление целями")
            self.t_manage_goals_button.place(x=400, y=250, height=30, width=200)
            self.t_manage_experts_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Управление экспертами")
            self.t_manage_experts_button.place(x=400, y=300, height=30, width=200)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Выйти из акканута")
            self.t_exit_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_manage_experts_button, self.t_manage_goals_button, self.t_remove_users_button, self.t_exit_button)
            ret = func(self, **kwargs)
        return wrapper

    @staticmethod
    def show_expert_menu(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_label = Label(text='Expert', font=font_family)
            self.t_label.place(x=400, y=200, height=30, width=200)
            return func(self, **kwargs)
        return wrapper


    @staticmethod
    def show_manage_experts_menu(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_label = Label(text='Управление экспертами', font=font_family)
            self.t_label.place(x=400, y=100, height=30, width=200)
            self.t_show_experts_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Просмотреть экспертов")
            self.t_show_experts_button.place(x=400, y=200, height=30, width=200)
            self.t_add_experts_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Добавить эксперта")
            self.t_add_experts_button.place(x=400, y=250, height=30, width=200)
            self.t_remove_experts_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Удалить эксперта")
            self.t_remove_experts_button.place(x=400, y=300, height=30, width=200)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_add_experts_button, self.t_show_experts_button, self.t_remove_experts_button, self.t_exit_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def show_experts(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_experts_list = Listbox(self.root, width=30, height=15, font=('times', 14))
            self.t_experts_list.place(x=125, y=75)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_exit_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def remove_accounts(func):
        @wraps(func)
        def wrapper(self, *args):
            self.t_accounts_list = Listbox(self.root, width=30, height=15, font=('times', 14))
            self.t_accounts_list.place(x=365, y=75)
            self.t_remove_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Удалить")
            self.t_remove_button.place(x=400, y=450, height=30, width=200)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_remove_button, self.t_exit_button)
            return func(self, *args)
        return wrapper

    @staticmethod
    def show_manage_goals_menu(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_label = Label(text='Управление целями', font=font_family)
            self.t_label.place(x=400, y=100, height=30, width=200)
            self.t_show_goals_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Просмотреть цели")
            self.t_show_goals_button.place(x=400, y=200, height=30, width=200)
            self.t_add_goals_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Добавить цель")
            self.t_add_goals_button.place(x=400, y=250, height=30, width=200)
            self.t_remove_goals_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Удалить цель")
            self.t_remove_goals_button.place(x=400, y=300, height=30, width=200)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_add_goals_button, self.t_show_goals_button, self.t_remove_goals_button, self.t_exit_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def show_goals(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_goals_list = Listbox(self.root, width=45, height=15, font=('times', 13))
            self.t_goals_list.place(x=125, y=75)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_exit_button)
            return func(self, **kwargs)
        return wrapper