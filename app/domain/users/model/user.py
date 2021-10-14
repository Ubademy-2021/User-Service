from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    userName: str
    name: str
    surname: str
    phoneNumber: str
    city: str
    state: str
    country: str
    address: str


class UserCreate(UserBase):
    def isComplete(self):
        isNotComplete = (
            not self.email
            or not self.address
            or not self.userName
            or not self.name
            or not self.surname
            or not self.country
            or not self.city
            or not self.state
        )
        return not isNotComplete


class User(UserBase):
    id: int
    isBlock: bool

    class Config:
        orm_mode = True
