from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from app.adapters.database.database import Base
from app.domain.userCategories.model.userCategory import UserCategory


class UserCategoryDTO(Base):
    __tablename__ = "userCategory"

    userId = Column(Integer, ForeignKey("user.id"), primary_key=True, index=True)
    categoryId = Column(Integer, primary_key=True, index=True)

    user = relationship("UserDTO", back_populates="categories")

    def initWithUserCategory(self, userCategory: UserCategory):

        self.userId = userCategory.userId
        self.categoryId = userCategory.categoryId

    def getCategoryId(self):
        return self.categoryId
