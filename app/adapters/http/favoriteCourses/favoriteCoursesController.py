from app.adapters.database.database import SessionLocal
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.adapters.database.favoriteCourses.model import FavoriteCourseDTO
from app.adapters.http.util.favoriteCourseUtil import FavoriteCourseUtil
from app.core.logger import logger
from app.domain.favoriteCourses.model.favoriteCourse import FavoriteCourse
from app.domain.favoriteCourses.repository.favoriteCourseRepository import FavoriteCourseRepository
from app.domain.userCategories.model.userCategory import UserCategory
from app.domain.userCategories.repository.userCategoryRepository import UserCategoryRepository
from app.adapters.http.util.categoryUtil import CategoryUtil


router = APIRouter(tags=["favoriteCourses"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.critical("Internal Error: " + e.__str__())
    finally:
        db.close()


@router.post("/users/favorites", response_model=FavoriteCourse)
def add_favorite_course(favoriteCourse: FavoriteCourse, db: Session = Depends(get_db)):
    logger.info("Adding course to favorites")
    if not favoriteCourse.userId or not favoriteCourse.courseId:
        logger.warning("Required fields are not complete")
        raise HTTPException(status_code=400, detail="Required fields are not complete")
    crud = FavoriteCourseRepository(db)
    FavoriteCourseUtil.check_favorite_course(db, favoriteCourse)
    return crud.create_favorite_course(favoriteCourse)


@router.get("/users/favorites/{userId}", response_model=List[FavoriteCourse])
def read_favorite_courses(
    userId, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    logger.info("Getting favorite courses list of user " + str(userId))
    crud = FavoriteCourseRepository(db)
    favorites = crud.get_favorites_by_user(userId, skip=skip, limit=limit)
    logger.debug("Getting " + str(len(favorites)) + " courses")
    return favorites


@router.delete("/users/favorites")
def delete_course_from_favorites(favoriteCourse: FavoriteCourse, db: Session = Depends(get_db)):
    logger.info("Removing course from favorites")
    fc = FavoriteCourseUtil.check_favorite_exists(db, favoriteCourse)
    repo = FavoriteCourseRepository(db)
    repo.delete_favorite_course(fc)
    logger.info("Course removed from favorites")
    return "Course removed from favorites"
