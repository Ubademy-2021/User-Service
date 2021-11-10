from sqlalchemy.orm import Session

from app.adapters.database.favoriteCourses.model import FavoriteCourseDTO
from app.domain.favoriteCourses.model.favoriteCourse import FavoriteCourse


class FavoriteCourseRepository:
    def __init__(self, session: Session):
        self.session: Session = session

    def get_favorite_course(self, userId, categoryId):
        return (
            self.session.query(FavoriteCourseDTO)
            .filter(FavoriteCourseDTO.userId == userId)
            .filter(FavoriteCourseDTO.courseId == categoryId)
            .first()
        )

    def get_favorites_by_user(self, userId, skip: int = 0, limit: int = 100):
        return (
            self.session.query(FavoriteCourseDTO)
            .filter(FavoriteCourseDTO.userId == userId)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create_favorite_course(self, favoriteCourse: FavoriteCourse):
        session_favoriteCourse = FavoriteCourseDTO()
        session_favoriteCourse.initWithFavoriteCourse(favoriteCourse)
        self.session.add(session_favoriteCourse)
        self.session.commit()
        self.session.refresh(session_favoriteCourse)
        return session_favoriteCourse

    def delete_favorite_course(self, favoriteCourse: FavoriteCourseDTO):
        self.session.delete(favoriteCourse)
        self.session.commit()
