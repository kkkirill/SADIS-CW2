from copy import copy
from dataclasses import dataclass
from typing import List

from src.models.accounts import Account


@dataclass
class Feedback:
    _account: Account
    _feedbacks: List[str]

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, new_account: Account):
        self._account = new_account

    @property
    def feedbacks(self):
        return self._feedbacks

    @feedbacks.setter
    def feedbacks(self, new_feedbacks: List[str]):
        self._feedbacks = copy(new_feedbacks)