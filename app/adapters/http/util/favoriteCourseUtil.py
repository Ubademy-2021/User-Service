from sqlalchemy.orm import Session
from app.adapters.http.util.userUtil import UserUtil
from app.core.logger import logger
from fastapi import HTTPException

from app.domain.favoriteCourses.model.favoriteCourse import FavoriteCourse
from app.domain.favoriteCourses.repository.favoriteCourseRepository import FavoriteCourseRepository


class FavoriteCourseUtil:

    def check_favorite_course(session: Session, favoriteCourse: FavoriteCourse):

        UserUtil.check_user_exists(session, favoriteCourse.userId)

        repo = FavoriteCourseRepository(session)
        fc = repo.get_favorite_course(favoriteCourse.userId, favoriteCourse.courseId)
        if fc:
            logger.warning("Course already added to favorites")
            raise HTTPException(status_code=400, detail="Course already added to favorites")
