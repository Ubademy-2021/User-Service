from app.adapters.database.database import SessionLocal
from app.adapters.database.categories.model import CategoryDTO
from app.adapters.database.userCategories.model import UserCategoryDTO
from app.domain.categories.model.category import Category, CategoryBase
from app.domain.categories.repository.category_repository import CategoryRepository
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.logger import logger
from app.domain.userCategories.model.userCategory import UserCategory
from app.domain.userCategories.repository.userCategoryRepository import (
    UserCategoryRepository,
)
from app.domain.users.repository.user_repository import UserRepository


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


@router.get("/categories", response_model=List[Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logger.info("Getting categories list")
    crud = CategoryRepository(db)
    categories = crud.get_categories(skip=skip, limit=limit)
    logger.debug("Getting " + str(categories.count(CategoryDTO)) + " categories")
    return categories


@router.post("/categories", response_model=Category)
def create_category(category: CategoryBase, db: Session = Depends(get_db)):
    logger.info("Creating " + category.name + " category")
    if not category.name:
        logger.warn("Required fields are not complete")
        raise HTTPException(status_code=400, detail="Required fields are not complete")
    crud = CategoryRepository(db)
    check_category(crud, category.name)
    return crud.create_category(category=category)


@router.get("/categories/{userId}", response_model=List[Category])
def read_categories_from_user(
    userId, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    logger.info("Getting categories list of user " + str(userId))
    crud = UserCategoryRepository(db)
    categories = crud.get_categories_by_user(userId, skip=skip, limit=limit)
    logger.debug("Getting " + str(categories.count(UserCategoryDTO)) + " categories")
    return list(map(UserCategoryDTO.getCategory, categories))


@router.post("/categories/user", response_model=UserCategory)
def create_user_category(userCategory: UserCategory, db: Session = Depends(get_db)):
    logger.info("Adding category to user")
    if not userCategory.userId or not userCategory.categoryId:
        logger.warn("Required fields are not complete")
        raise HTTPException(status_code=400, detail="Required fields are not complete")
    crud = UserCategoryRepository(db)
    check_user_category(db, userCategory)
    return crud.create_user_category(userCategory)


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