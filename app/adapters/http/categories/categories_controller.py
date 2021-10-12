from app.adapters.database.database import SessionLocal
from app.adapters.database.categories.model import CategoryDTO
from app.domain.categories.model.category import Category, CategoryBase
from app.domain.categories.repository.category_repository import CategoryRepository
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.logger import logger


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
