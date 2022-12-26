import datetime
import json
from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    password: str

    def __str__(self) -> str:
        return f'ID -> {self.id}\nUSERNAME -> {self.username}\nPASSWORD -> {self.password}'

with open('user.json', mode='r') as f:
    data = json.load(f)
    
    user = User(**data)

with open('user.json', mode='a') as file:
    data = user.dict()
    json.dump(data, file, indent=4)