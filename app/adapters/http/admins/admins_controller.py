from app.adapters.database.database import SessionLocal
from app.adapters.database.admins.model import AdminDTO
from app.domain.admins.model.admin import Admin
from app.domain.admins.repository.admin_repository import AdminRepository
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from app.core.logger import logger


router = APIRouter(tags=["admins"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.critical("Internal Error: " + e.__str__())
    finally:
        db.close()


@router.get("/admins", response_model=List[Admin])
def read_admins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logger.info("Getting admins list")
    crud = AdminRepository(db)
    admins = crud.get_admins(skip=skip, limit=limit)
    logger.debug("Getting " + str(admins.count(AdminDTO)) + " admins")
    return admins
