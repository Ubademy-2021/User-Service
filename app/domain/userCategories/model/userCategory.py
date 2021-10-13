from pydantic import BaseModel


class UserCategory(BaseModel):
    userId: str
    categoryId: str
