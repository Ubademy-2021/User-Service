from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.adapters.database.database import Base
from app.domain.categories.model.category import CategoryBase


class CategoryDTO(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    users = relationship("UserCategoryDTO", back_populates="category")

    def initWithCategoryBase(self, category: CategoryBase):

        self.name = category.name
