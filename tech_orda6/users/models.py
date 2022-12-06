"""
Доменная зона
В этом файле только храниться сущностей. Оно не кладется не в одну из зон.
Зоны для того чтобы как c этими сущностями взаимодействовать.
"""

import hashlib

class User:
    __password: str

    def __init__(self, username: str):
        self.username = username

    def set_password(self, password: str):
        self.__password = self._hash_password(password)
    
    # def get_password(self):
    #     return(self.__password)

    def check_password(self, password: str) -> bool:
        return self.__password == self._hash_password(password)
    
    @staticmethod
    def _hash_password(password: str):
        return hashlib.sha256(password.encode(encoding='utf-8')).hexdigest()

    def __repr__(self):
        return self.username