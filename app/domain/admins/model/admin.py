from pydantic import BaseModel


class AdminBase(BaseModel):
    email: str
    name: str
    surname: str

    def isComplete(self):
        isNotComplete = (
            not self.email
            or not self.name
            or not self.surname
        )
        return not isNotComplete


class Admin(AdminBase):
    id: int

    class Config:
        orm_mode = True
