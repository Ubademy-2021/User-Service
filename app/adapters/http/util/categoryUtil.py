from app.adapters.http.util.courseServiceUtil import CourseServiceUtil
from app.adapters.http.util.userUtil import UserUtil
from app.domain.users.repository.user_repository import UserRepository
from app.domain.userCategories.repository.userCategoryRepository import UserCategoryRepository
from app.domain.userCategories.model.userCategory import UserCategory
from sqlalchemy.orm import Session
from app.core.logger import logger
from fastapi import HTTPException


class CategoryUtil:

    def check_user_category(session: Session, userCategory: UserCategory):

        UserUtil.check_user_exists(session, userCategory.userId)

        CourseServiceUtil.check_category_exists(userCategory.categoryId)

        userCategoryRepository = UserCategoryRepository(session)
        session_user_category = userCategoryRepository.get_user_category(
            userCategory.userId, userCategory.categoryId
        )
        if session_user_category:
            logger.warning("User already has category")
            raise HTTPException(status_code=400, detail="User already has category")
