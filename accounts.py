class Account:
    def __init__(self, role: int, login: str, password: str, **kwargs):
        self.role = role
        self.login = login
        self.password = password
        self.email = kwargs.get('email', '')
        self.fn = kwargs.get('fn', '')
        self.phone = kwargs.get('phone', '')
        self.fax = kwargs.get('fax', '')

    @property
    def password(self):
        return self.password

    @property
    def email(self):
        return self.email

    @property
    def fn(self):
        return self.fn

    @property
    def phone(self):
        return self.phone

    @property
    def fax(self):
        return self.fax

    @password.setter
    def password(self, new_password: str):
        self.password = new_password

    @email.setter
    def email(self, new_email: str):
        self.email = new_email

    @fn.setter
    def fn(self, new_fn: str):
        self.fn = new_fn

    @phone.setter
    def phone(self, new_phone: str):
        self.email = new_phone

    @fax.setter
    def fax(self, new_fax: str):
        self.email = new_fax

# class Admin(Account):
#     def __init__(self, login: str, password: str, **kwargs):
#         super(Admin, self).__init__(login, password, **kwargs)
#     pass
#
# class Expert(Account):
#     pass
#
# class User(Account):
#     pass
