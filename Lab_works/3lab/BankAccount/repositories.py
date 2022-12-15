from typing import List, Optional

from BankAccount.models import BankAccount, AccountType



class BankAccountRepositories:
    users: List[BankAccount] = []

    def create_user(self, name: str, surname: str, account: AccountType) -> None:
        user = BankAccount(name=name, surname=surname, account=account)
        self.users.append(user)
        print('\033[32m' + f'Пользователь успешно создан!\nВаше имя пользователя --> {name.lower()}{surname.lower()}')
        print(user)
    
    def get_user(self, username: str) -> Optional[BankAccount]:
        user = next(
            (u for u in self.users if username == u.username), 
            None
        )

        if not user:
            print('\033[31m' + 'Пользователь не найден!')
            return

        print('\033[32m' + 'Пользователь успешно найден!')
        print(user)
        return user