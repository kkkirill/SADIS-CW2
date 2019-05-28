from dataclasses import dataclass, field
from src.models.accounts import Account


@dataclass
class Order:
    _account: Account
    _platform: str
    _deadline: str
    _topic: str
    _description: str
    _is_promotion: bool
    _cost: int = field(init=False)

    def __post_init__(self):
        self.cost = (600 if self.is_promoted else 400)

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, new_account: Account):
        self._account = new_account

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, new_platform: str):
        self._platform = new_platform

    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, new_deadline: str):
        self._deadline = new_deadline

    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, new_topic: str):
        self._topic = new_topic

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description

    @property
    def is_promoted(self):
        return self._is_promotion

    @is_promoted.setter
    def is_promoted(self, value: bool):
        self._is_promotion = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, new_cost: int):
        self._cost = new_cost
