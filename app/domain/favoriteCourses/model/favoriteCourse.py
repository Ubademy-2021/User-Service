from pydantic import BaseModel


class FavoriteCourse(BaseModel):
    userId: int
    courseId: int

    class Config:
        orm_mode = True
