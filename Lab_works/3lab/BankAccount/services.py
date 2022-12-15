from typing import Optional
from BankAccount.models import BankAccount, AccountType
from BankAccount.repositories import BankAccountRepositories


class BankAccountServices:
    repositories: BankAccountRepositories

    def __init__(self, repositories) -> None:
        self.repositories = repositories
    
    def create_user(self, name: str, surname: str, account: AccountType) -> None:
        self.repositories.create_user(name=name, surname=surname, account=account)
    
    def get_user(self, username: str) -> Optional[BankAccount]:
        return self.repositories.get_user(username)