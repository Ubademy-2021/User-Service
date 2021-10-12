from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    user_name: str
    name: str
    last_name: str
    phone_number: str
    street: str
    street_nbr: int
    floor_appt: str
    local: str
    postal_code: str


class UserCreate(UserBase):
    password: str

    def isComplete(self):
        isNotComplete = (not self.email or not self.password
                         or not self.user_name or not self.name
                         or not self.last_name or not self.postal_code
                         or not self.street or not self.street_nbr
                         or not self.floor_appt or not self.local)
        return not isNotComplete


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
