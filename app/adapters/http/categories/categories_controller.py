from app.adapters.database.database import SessionLocal
from app.adapters.database.userCategories.model import UserCategoryDTO
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.logger import logger
from app.domain.userCategories.model.userCategory import UserCategory
from app.domain.userCategories.repository.userCategoryRepository import UserCategoryRepository
from app.adapters.http.util.categoryUtil import CategoryUtil


router = APIRouter(tags=["categories"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.critical("Internal Error: " + e.__str__())
    finally:
        db.close()


@router.get("/categories/{userId}", response_model=List[UserCategory])
def read_categories_from_user(
    userId, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    logger.info("Getting categories list of user " + str(userId))
    crud = UserCategoryRepository(db)
    categories = crud.get_categories_by_user(userId, skip=skip, limit=limit)
    logger.debug("Getting " + str(len(categories)) + " categories")
    return categories


@router.post("/categories/user", response_model=UserCategory)
def create_user_category(userCategory: UserCategory, db: Session = Depends(get_db)):
    logger.info("Adding category to user")
    if not userCategory.userId or not userCategory.categoryId:
        logger.warning("Required fields are not complete")
        raise HTTPException(status_code=400, detail="Required fields are not complete")
    crud = UserCategoryRepository(db)
    CategoryUtil.check_user_category(db, userCategory)
    return crud.create_user_category(userCategory)
