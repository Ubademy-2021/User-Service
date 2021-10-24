from app.domain.users.repository.user_repository import UserRepository
from app.domain.userCategories.repository.userCategoryRepository import UserCategoryRepository
from app.domain.categories.repository.category_repository import CategoryRepository
from app.domain.userCategories.model.userCategory import UserCategory
from sqlalchemy.orm import Session
from app.core.logger import logger
from fastapi import HTTPException


class CategoryUtil:

    def check_category(categoryRepository: CategoryRepository, category_name):
        db_category = categoryRepository.get_category_by_name(category_name)
        if db_category:
            logger.warn("Category " + category_name + " already exists")
            raise HTTPException(
                status_code=400, detail="Category " + category_name + " already exists"
            )

    def check_user_category(db: Session, userCategory: UserCategory):
        userCategoryRepository = UserCategoryRepository(db)
        db_user_category = userCategoryRepository.get_user_category(
            userCategory.userId, userCategory.categoryId
        )
        if db_user_category:
            logger.warn("User already has category")
            raise HTTPException(status_code=400, detail="User already has category")
        userRepository = UserRepository(db)
        db_user = userRepository.get_user(userCategory.userId)
        if not db_user:
            logger.warn("User " + str(userCategory.userId) + " does not exist")
            raise HTTPException(
                status_code=400,
                detail="User " + str(userCategory.userId) + " does not exist",
            )
        categoryRepository = CategoryRepository(db)
        db_category = categoryRepository.get_category(userCategory.categoryId)
        if not db_category:
            logger.warn("Category " + str(userCategory.categoryId) + " does not exist")
            raise HTTPException(
                status_code=400,
                detail="Category " + str(userCategory.categoryId) + " does not exist",
            )
