import hashlib
from typing import Optional

users = []


def hash_password(password: str):
    return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()


class User:
    __password: str

    def __init__(self, username: str):
        self.username = username

    def set_password(self, password: str):
        self.__password = hash_password(password)

    def check_password(self, password: str) -> bool:
        return self.__password == hash_password(password)

    def __repr__(self):
        return self.username


def create_user(username: str, password: str) -> User:
    user = User(username=username)
    user.set_password(password=password)
    users.append(user)
    print(users)

    return user


def get_user(username: str, password: str) -> Optional[User]:
    user = next((u for u in users if username == u.username and u.check_password(password)), None)

    if not user:
        print('User not found')
        return

    return user



username, password = input('Create user: ').split(' ')
user = create_user(username=username, password=password)
print(user)

while True:
    username, password = input('Enter your creds: ').split(' ')
    if (get_user(username=username, password=password)):
        break
