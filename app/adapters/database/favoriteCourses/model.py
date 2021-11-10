from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from app.adapters.database.database import Base
from app.domain.favoriteCourses.model.favoriteCourse import FavoriteCourse


class FavoriteCourseDTO(Base):
    __tablename__ = "favoriteCourse"

    userId = Column(Integer, ForeignKey("user.id"), primary_key=True, index=True)
    courseId = Column(Integer, primary_key=True, index=True)

    user = relationship("UserDTO", back_populates="favoriteCourses")

    def initWithFavoriteCourse(self, favoriteCourse: FavoriteCourse):

        self.userId = favoriteCourse.userId
        self.courseId = favoriteCourse.courseId
