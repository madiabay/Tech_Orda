from typing import Optional
from BankAccount.services import BankAccountServices
from BankAccount.models import BankAccount, AccountType


class BankAccountHandlers:
    services: BankAccountServices

    def __init__(self, services: BankAccountServices) -> None:
        self.services = services
    
    def create_user(self, name: str, surname: str, account: str) -> None:
        name = name.title()
        surname = surname.title()

        match account.upper():
            case 'KZT':
                account_type = AccountType.KZT
            case 'USD':
                account_type = AccountType.USD
            case 'EUR':
                account_type = AccountType.EUR
            case 'RUB':
                account_type = AccountType.RUB
            case _:
                account_type = None
        
        if not account_type:
            print('\033[31m' + 'Тип аккаунта введен неправильно. Попробуйте еще раз')
            return 'error'
        
        self.services.create_user(name=name, surname=surname, account=account_type)
    
    def get_user(self, username: str) -> Optional[BankAccount]:
        return self.services.get_user(username)
    
@staticmethod
def moneyConversion(bank_account: BankAccount, ex_to):
    match bank_account.account.value, ex_to:
        # KZT
        case 'KZT', 'USD':
            bank_account.cash_amount /= 450
            bank_account.account = AccountType.USD
        case 'KZT', 'RUB':
            bank_account.cash_amount /= 5
            bank_account.account = AccountType.RUB
        case 'KZT', 'EUR':
            bank_account.cash_amount /= 500
            bank_account.account = AccountType.EUR
        # USD
        case 'USD', 'KZT':
            bank_account.cash_amount *= 450
            bank_account.account = AccountType.USD
        case 'USD', 'RUB':
            bank_account.cash_amount *= 90
            bank_account.account = AccountType.RUB
        case 'USD', 'EUR':
            bank_account.cash_amount *= 0.9
            bank_account.account = AccountType.EUR
        # RUB
        case 'RUB', 'USD':
            bank_account.cash_amount /= 90
            bank_account.account = AccountType.USD
        case 'RUB', 'KZT':
            bank_account.cash_amount *= 5
            bank_account.account = AccountType.RUB
        case 'RUB', 'EUR':
            bank_account.cash_amount /= 100
            bank_account.account = AccountType.EUR
        # EUR
        case 'EUR', 'USD':
            bank_account.cash_amount *= 1.1
            bank_account.account = AccountType.USD
        case 'EUR', 'RUB':
            bank_account.cash_amount *= 100
            bank_account.account = AccountType.RUB
        case 'EUR', 'KZT':
            bank_account.cash_amount *= 500
            bank_account.account = AccountType.EUR
        case _:
            return '\033[31m' + 'Invalid parametres'