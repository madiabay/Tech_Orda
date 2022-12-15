from dataclasses import dataclass, field
from enum import Enum
from typing import Any, List

class AccountType(Enum):
    KZT = 'KZT'
    USD = 'USD'
    EUR = 'EUR'
    RUB = 'RUB'

    def __str__(self) -> str:
        return self.value

@dataclass
class BankAccount:
    name: str
    surname: str
    account: AccountType
    cash_amount: float = field(init=False, default=0)
    
    def __post_init__(self):
        self.username = f'{self.name.lower()}{self.surname.lower()}'
    
    def check_cash():
        pass

    def __str__(self) -> str:
        return '\033[33m' + f'{self.username}: {self.cash_amount} {self.account}'