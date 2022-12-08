"""
Этот файл входит в зону Use Cases или можно назвать Services.
"""

from typing import Optional
from users.models import User
from users.repositories import UserRepositories


class UserServices:
    repositories: UserRepositories

    def __init__(self, repositories) -> None:
        self.repositories = repositories
    
    def create_user(self, username: str, password: str) -> None:
        self.repositories.create_user(username=username, password=password)
        self._send_email_verification(username)
    
    def get_user(self, username: str, password: str) -> Optional[User]:
        return self.repositories.get_user(username=username, password=password)
    
    @staticmethod
    def _send_email_verification(email):
        print(f'send verification letter to {email}')
    
    def change_password(self, username: str, password: str) -> None:
        self.repositories.change_password(username, password)
    
    def change_password(self, correct_user: User, password: str) -> None:
        self.repositories.change_password(correct_user=correct_user, password=password)