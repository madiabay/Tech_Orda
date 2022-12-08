"""
Этот файл входит в зону Controllers или можно назвать Handlers.Handlers переводятся как обработчики.
"""

from typing import Optional
from users.services import UserServices
from users.models import User

class UserHandlers:
    services: UserServices

    def __init__(self, services: UserServices) -> None:
        self.services = services

    def sign_up(self, username: str, password: str) -> None:
        username = username.strip().lower()
        password = password.strip()

        if not self._validate_username_and_password(username, password):
            return None
        
        self.services.create_user(username=username, password=password)

    def sign_in(self, username: str, password: str) -> Optional[User]:
        username = username.strip().lower()
        password = password.strip()

        if not self._validate_username_and_password(username, password):
            return None
        
        return self.services.get_user(username=username, password=password)
    
    @staticmethod
    def _validate_username_and_password(username: str, password: str) -> bool:
        if username.startswith('z'):
            print('UserName is invalid')
            return False
        
        if len(password) < 8:
            print('Password is too short')
            return False
        
        return True
    
    def change_password(self, correct_user: User, password: str) -> None:
        if not len(password) < 8:
            self.services.change_password(correct_user=correct_user, password=password)
            print('SUCCESSFULLY CHANGED YOUR PASSWORD')
            return
        print('Password is too short, YOUR password has not changed')
        return    