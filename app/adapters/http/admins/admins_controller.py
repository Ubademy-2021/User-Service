from starlette.exceptions import HTTPException
from app.adapters.database.database import SessionLocal
from app.adapters.database.admins.model import AdminDTO
from app.domain.admins.model.admin import Admin, AdminBase
from app.domain.admins.repository.admin_repository import AdminRepository
from app.adapters.http.util.adminUtil import AdminUtil
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
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
def read_admin(
    admin_id: Optional[int] = None,
    email: Optional[str] = None,
    skip: Optional[int] = 0,
    limit: Optional[int] = 100,
    db: Session = Depends(get_db),
):
    crud = AdminRepository(db)
    admins = []

    if admin_id:
        logger.info("Getting admin with id = " + str(admin_id))
        admins.append(AdminUtil.check_admin_exists(db, admin_id))
    elif email:
        logger.info("Getting admin with email = " + email)
        admins.append(AdminUtil.check_email_exists(db, email))
    else:
        admins = crud.get_admins(skip=skip, limit=limit)
        logger.debug("Getting all admins")
        return admins

    return admins


@router.post("/admins", response_model=Admin)
def create_admin(admin: AdminBase, db: Session = Depends(get_db)):
    logger.info("Creating admin " + admin.email)
    if not admin.isComplete():
        logger.warning("Required fields are not complete")
        raise HTTPException(status_code=400, detail="Required fields are not complete")
    crud = AdminRepository(db)
    AdminUtil.check_email(db, admin.email)
    return crud.create_admin(admin=admin)
