class Account:
    def __init__(self, role: int, login: str, password: str, **kwargs):
        self._role = role
        self._login = login
        self._password = password
        self._email = kwargs.get('email', '')
        self._fn = kwargs.get('fn', '')
        self._phone = kwargs.get('phone', '')
        self._fax = kwargs.get('fax', '')

    @property
    def login(self):
        return self._login

    @property
    def role(self):
        return self._role

    @property
    def password(self):
        return self._password

    @property
    def email(self):
        return self._email

    @property
    def fn(self):
        return self._fn

    @property
    def phone(self):
        return self._phone

    @property
    def fax(self):
        return self._fax

    @password.setter
    def password(self, new_password: str):
        self._password = new_password

    @email.setter
    def email(self, new_email: str):
        self._email = new_email

    @fn.setter
    def fn(self, new_fn: str):
        self._fn = new_fn

    @phone.setter
    def phone(self, new_phone: str):
        self._phone = new_phone

    @fax.setter
    def fax(self, new_fax: str):
        self._fax = new_fax
