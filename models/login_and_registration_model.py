from typing import List
from pydantic import BaseModel


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UserList(BaseModel):
    user_list: List[User]
