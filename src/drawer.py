from tkinter import Label, Image, Button, Entry, StringVar, END, Listbox, Text, BooleanVar, Radiobutton, DISABLED
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
    def remove_promotion_buttons(func):
        @wraps(func)
        def wrapper(self, *args):
            for value in filter(lambda value: value.startswith('t_promotion') and (value.endswith('_button')), dir(self)):
                getattr(self, value).destroy()
            return func(self, *args)
        return wrapper


    @staticmethod
    def remove_input_and_labels(func):
        @wraps(func)
        def wrapper(self, *args):
            for value in filter(lambda value: value.startswith('t_') and (value.endswith('_input') or value.endswith('_label') and value != 't_total_sum_label'), dir(self)):
                getattr(self, value).destroy()
            return func(self, *args)
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
            self.t_goals_list.place(x=300, y=75)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_exit_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def add_goal(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_goal_label = Label(text='Введите цель', font=font_family, width=40)
            self.t_goal_label.place(x=325, y=200)
            self.t_goal_input = Entry(font=font_family, width=40)
            self.t_goal_input.place(x=325, y=250)
            self.t_submit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Добавить")
            self.t_submit_button.place(x=400, y=450, height=30, width=200)
            self.t_cancel_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Назад")
            self.t_cancel_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_submit_button, self.t_cancel_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def remove_goal(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_goals_list = Listbox(self.root, width=45, height=15, font=('times', 13))
            self.t_goals_list.place(x=300, y=75)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=550, height=30, width=200)
            self.t_remove_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Удалить")
            self.t_remove_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_remove_button, self.t_exit_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def show_user_menu(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_label = Label(text='Меню клиента', font=font_family)
            self.t_label.place(x=400, y=100, height=30, width=200)
            self.t_make_order_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Сделать заказ")
            self.t_make_order_button.place(x=400, y=200, height=30, width=200)
            self.t_my_orders_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Мои заказы")
            self.t_my_orders_button.place(x=400, y=250, height=30, width=200)
            self.t_my_account_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Аккаунт")
            self.t_my_account_button.place(x=400, y=300, height=30, width=200)
            self.t_leave_feedback_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Оставить отзыв о фирме ")
            self.t_leave_feedback_button.place(x=400, y=350, height=30, width=200)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Выйти из акканута")
            self.t_exit_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_make_order_button, self.t_my_orders_button, self.t_my_account_button, self.t_leave_feedback_button, self.t_exit_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def show_my_account(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_label = Label(text='Мой аккаунт', font=font_family)
            self.t_label.place(x=400, y=50, height=30, width=200)
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

            self.t_edit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Изменить")
            self.t_edit_button.place(x=400, y=450, height=30, width=200)
            self.t_cancel_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3, font=font_family, text="Назад")
            self.t_cancel_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_edit_button, self.t_cancel_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def show_orders(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_orders_list = Listbox(self.root, width=30, height=15, font=('times', 14))
            self.t_orders_list.place(x=125, y=75)
            self.t_total_sum_label = Label(self.root)
            self.t_total_sum_label.place(x=125, y=450, height=30, width=100)
            self.t_delete_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Удалить")
            self.t_delete_button.place(x=400, y=450, height=30, width=200)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_delete_button, self.t_exit_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def add_order(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            # self.t_label = Label(text='Меню заказа', font=font_family)
            # self.t_label.place(x=400, y=50, height=30, width=200)
            self.t_platform_label = Label(text='Язык программирования', font=font_family)
            self.t_platform_label.place(x=275, y=100, height=30, width=200)
            self.t_platform_input = Entry(font=font_family)
            self.t_platform_input.focus()
            self.t_platform_input.place(x=525, y=100, height=30, width=300)

            self.t_deadline_label = Label(text='Срок выполнения', font=font_family)
            self.t_deadline_label.place(x=275, y=150, height=30, width=200)
            self.t_deadline_input = Entry(font=font_family)
            self.t_deadline_input.place(x=525, y=150, height=30, width=300)

            self.t_topic_label = Label(text='Тема', font=font_family)
            self.t_topic_label.place(x=275, y=200, height=30, width=200)
            self.t_topic_input = Entry(font=font_family)
            self.t_topic_input.place(x=525, y=200, height=30, width=300)

            self.t_description_label = Label(text='Описание', font=font_family)
            self.t_description_label.place(x=275, y=250, height=30, width=200)
            self.t_description_input = Text(font=font_family, height=12, width=33)
            self.t_description_input.place(x=525, y=250)

            self.t_promotion_label = Label(text='Продвижение сайта', font=font_family)
            self.t_promotion_label.place(x=275, y=400, height=30, width=200)
            self.is_promotion_enabled = BooleanVar(value=0)
            self.t_promotion_enabled_button = Radiobutton(text='Да', width=5, variable=self.is_promotion_enabled, value=0)
            self.t_promotion_enabled_button.place(x=310, y=450)
            self.t_promotion_disabled_button = Radiobutton(text='Нет', width=5, variable=self.is_promotion_enabled, value=1)
            self.t_promotion_disabled_button.place(x=380, y=450)

            self.t_make_order_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Сделать заказ")
            self.t_make_order_button.place(x=400, y=500, height=30, width=200)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=550, height=30, width=200)
            Drawer.hover_bind_button(self.t_make_order_button, self.t_exit_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def show_order(func):
        @wraps(func)
        def wrapper(self, *args):
            self.t_platform_label = Label(text='Язык программирования', font=font_family)
            self.t_platform_label.place(x=450, y=100, height=30, width=200)
            self.t_platform_input = Entry(font=font_family)
            self.t_platform_input.place(x=700, y=100, height=30, width=240)

            self.t_deadline_label = Label(text='Срок выполнения', font=font_family)
            self.t_deadline_label.place(x=450, y=150, height=30, width=200)
            self.t_deadline_input = Entry(font=font_family)
            self.t_deadline_input.place(x=700, y=150, height=30, width=240)

            self.t_topic_label = Label(text='Тема', font=font_family)
            self.t_topic_label.place(x=450, y=200, height=30, width=200)
            self.t_topic_input = Entry(font=font_family)
            self.t_topic_input.place(x=700, y=200, height=30, width=240)

            self.t_description_label = Label(text='Описание', font=font_family)
            self.t_description_label.place(x=450, y=250, height=30, width=200)
            self.t_description_input = Text(font=font_family, background='#f0f0f0', foreground='#7f7186', height=12, width=26)
            self.t_description_input.place(x=700, y=250)

            self.t_promotion_label = Label(text='Продвижение сайта', font=font_family)
            self.t_promotion_label.place(x=450, y=300, height=30, width=200)
            self.is_promotion_enabled = BooleanVar(value=1)
            self.t_promotion_enabled_button = Radiobutton(text='Да', width=5, variable=self.is_promotion_enabled, value=1, state=DISABLED)
            self.t_promotion_enabled_button.place(x=485, y=350)
            self.t_promotion_disabled_button = Radiobutton(text='Нет', width=5, variable=self.is_promotion_enabled, value=0, state=DISABLED)
            self.t_promotion_disabled_button.place(x=565, y=350)
            return func(self, *args)
        return wrapper

    @staticmethod
    def add_feedbacks(func):
        @wraps(func)
        def wrapper(self, *args):
            self.t_first_label = Label(text='Удовлетворённость сайтом', font=font_family)
            self.t_first_label.place(x=350, y=50, height=30, width=300)
            self.t_first_input = Entry(font=font_family)
            self.t_first_input.place(x=350, y=100, height=30, width=300)

            self.t_second_label = Label(text='Качество выполнения', font=font_family)
            self.t_second_label.place(x=350, y=150, height=30, width=300)
            self.t_second_input = Entry(font=font_family)
            self.t_second_input.place(x=350, y=200, height=30, width=300)

            self.t_third_label = Label(text='Быстрота выполнения', font=font_family)
            self.t_third_label.place(x=350, y=250, height=30, width=300)
            self.t_third_input = Entry(font=font_family)
            self.t_third_input.place(x=350, y=300, height=30, width=300)

            self.t_forth_label = Label(text='Квалифицированность персонала', font=font_family)
            self.t_forth_label.place(x=350, y=350, height=30, width=300)
            self.t_forth_input = Entry(font=font_family)
            self.t_forth_input.place(x=350, y=400, height=30, width=300)

            self.t_make_feedback_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                              font=font_family, text="Оставить отзыв")
            self.t_make_feedback_button.place(x=400, y=500, height=30, width=200)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                        font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=550, height=30, width=200)
            Drawer.hover_bind_button(self.t_make_feedback_button, self.t_exit_button)
            return func(self, *args)
        return wrapper

    @staticmethod
    def show_expert_menu(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_label = Label(text='Меню экспертов', font=font_family)
            self.t_label.place(x=400, y=100, height=30, width=200)
            self.t_expert_mark_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Оценка экспертов")
            self.t_expert_mark_button.place(x=400, y=200, height=30, width=200)
            self.t_show_feedbacks_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Просмотреть отзывы")
            self.t_show_feedbacks_button.place(x=400, y=250, height=30, width=200)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Выйти из аккаунта")
            self.t_exit_button.place(x=400, y=450, height=30, width=200)
            Drawer.hover_bind_button(self.t_expert_mark_button, self.t_show_feedbacks_button, self.t_exit_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def show_feedbacks(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_feedbacks_list = Listbox(self.root, width=30, height=15, font=('times', 14))
            self.t_feedbacks_list.place(x=125, y=75)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_exit_button)
            return func(self, **kwargs)
        return wrapper

    @staticmethod
    def show_feedback(func):
        @wraps(func)
        def wrapper(self, *args):
            self.t_first_label = Label(text='Удовлетворённость сайтом', font=font_family)
            self.t_first_label.place(x=430, y=100, height=30, width=250)
            self.t_first_input = Entry(font=font_family)
            self.t_first_input.place(x=700, y=100, height=30, width=240)

            self.t_second_label = Label(text='Качество выполнения', font=font_family)
            self.t_second_label.place(x=430, y=150, height=30, width=250)
            self.t_second_input = Entry(font=font_family)
            self.t_second_input.place(x=700, y=150, height=30, width=240)

            self.t_third_label = Label(text='Быстрота выполнения', font=font_family)
            self.t_third_label.place(x=430, y=200, height=30, width=250)
            self.t_third_input = Entry(font=font_family)
            self.t_third_input.place(x=700, y=200, height=30, width=240)

            self.t_forth_label = Label(text='Квалифицированность персонала', font=font_family)
            self.t_forth_label.place(x=430, y=250, height=30, width=250)
            self.t_forth_input = Entry(font=font_family)
            self.t_forth_input.place(x=700, y=250, height=30, width=240)
            return func(self, *args)
        return wrapper

    @staticmethod
    def draw_marks(func):
        @wraps(func)
        def wrapper(self, **kwargs):
            self.t_goals_list = Listbox(self.root, width=30, height=15, font=('times', 14))
            self.t_goals_list.place(x=125, y=75)
            self.t_total_amount_label = Label(font=font_family)
            self.t_total_amount_label.place(x=130, y=430, width=30, height=15)
            self.t_exit_button = Button(self.root, background=b_color, foreground=bf_color, width=50, height=3,
                                  font=font_family, text="Назад")
            self.t_exit_button.place(x=400, y=500, height=30, width=200)
            Drawer.hover_bind_button(self.t_exit_button)
            return func(self, **kwargs)
        return wrapper