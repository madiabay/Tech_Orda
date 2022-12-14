"""
Этот файл входит в зону Entities или можно назвать Repositories.
"""

from typing import List
from .exceptions import ChildrenNotFound
from users.models import User


class UserRepositories:
    users: List[User] = []

    def create_user(self, username: str, password: str) -> None:
        user = User(username=username)
        user.set_password(password=password)

        self.users.append(user)
    
    def get_user(self, username: str, password: str) -> User:
        user = next(
            (u for u in self.users if username == u.username and u.check_password(password)), 
            None
        )

        if not user:
            raise ChildrenNotFound

        return user
    
    def change_password(self, correct_user: User, password: str) -> None:
        correct_user.set_password(password)