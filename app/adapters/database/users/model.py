from app.adapters.database.database import Base
from app.domain.users.model.user import UserCreate
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class UserDTO(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    userName = Column(String, unique=True)
    name = Column(String)
    surname = Column(String)
    phoneNumber = Column(String, nullable=True, default=None)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    address = Column(String)
    isBlock = Column(Boolean, default=True)

    categories = relationship("UserCategoryDTO", back_populates="user")
    favoriteCourses = relationship("FavoriteCourseDTO", back_populates="user")

    def initWithUserCreate(self, user: UserCreate):

        self.email = user.email
        self.userName = user.userName
        self.name = user.name
        self.surname = user.surname
        if user.phoneNumber:
            self.phoneNumber = user.phoneNumber
        self.city = user.city
        self.state = user.state
        self.country = user.country
        self.address = user.address
        self.isBlock = False
