from pydantic import BaseModel


class UserCategory(BaseModel):
    userId: int
    categoryId: int

    class Config:
        orm_mode = True
