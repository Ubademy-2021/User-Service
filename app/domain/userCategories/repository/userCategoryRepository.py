from sqlalchemy.orm import Session

from app.adapters.database.userCategories.model import UserCategoryDTO
from app.domain.userCategories.model.userCategory import UserCategory


class UserCategoryRepository:
    def __init__(self, session: Session):
        self.session: Session = session

    def get_user_category(self, userId, categoryId):
        return (
            self.session.query(UserCategoryDTO)
            .filter(UserCategoryDTO.userId == userId)
            .filter(UserCategoryDTO.categoryId == categoryId)
            .first()
        )

    def get_categories_by_user(self, userId, skip: int = 0, limit: int = 100):
        return (
            self.session.query(UserCategoryDTO)
            .filter(UserCategoryDTO.userId == userId)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_users_by_category(self, categoryId, skip: int = 0, limit: int = 100):
        return (
            self.session.query(UserCategoryDTO)
            .filter(UserCategoryDTO.categoryId == categoryId)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create_user_category(self, userCategory: UserCategory):
        session_userCategory = UserCategoryDTO()
        session_userCategory.initWithUserCategory(userCategory)
        self.session.add(session_userCategory)
        self.session.commit()
        self.session.refresh(session_userCategory)
        return session_userCategory
