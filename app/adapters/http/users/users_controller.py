from app.adapters.database.database import SessionLocal
from app.adapters.database.users.model import UserDTO
from app.domain.exceptions.user_not_found_error import UserNotFoundError
from app.domain.users.model.user import UserCreate, User
from app.domain.email import Email
from app.domain.users.repository.user_repository import UserRepository
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.logger import logger
from app.adapters.http.util.userUtil import UserUtil
from typing import Optional

router = APIRouter(tags=["users"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.critical("Internal Error: " + e.__str__())
    finally:
        db.close()


@router.post("/users", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    logger.info("Creating user " + user.email)
    if not user.isComplete():
        logger.warn("Required fields are not complete")
        raise HTTPException(status_code=400, detail="Required fields are not complete")
    crud = UserRepository(db)
    UserUtil.check_email(crud, user.email)
    UserUtil.check_username(crud, user.userName)
    return crud.create_user(user=user)


@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_updated: UserCreate, db: Session = Depends(get_db)):
    logger.info("Updating user with id " + str(user_id))
    crud = UserRepository(db)

    try:
        user_updated = crud.update_user(user_id, user_updated)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=e.message)

    logger.info("User user with id " + str(user_id) + " updates successfully")
    return user_updated


# @router.get("/users", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logger.info("Getting users list")
    crud = UserRepository(db)
    users = crud.get_users(skip=skip, limit=limit)
    logger.debug("Getting " + str(users.count(UserDTO)) + " users")
    return users


@router.get("/users", response_model=User)
def read_user(
    user_id: Optional[int] = None,
    email: Optional[str] = None,
    skip: Optional[int] = 0,
    limit: Optional[int] = 100,
    db: Session = Depends(get_db),
):
    crud = UserRepository(db)

    if user_id:
        logger.info("Getting user with id = " + str(user_id))
        db_user = UserUtil.check_id_exists(crud, user_id)
    elif email:
        logger.info("Getting user with email = " + email)
        db_user = UserUtil.check_id_exists(crud, user_id)

    return db_user


@router.get("/user", response_model=User)
def read_user_from_email(email: Email, db: Session = Depends(get_db)):
    emailStr = email.email
    logger.info("Getting user " + emailStr)
    crud = UserRepository(db)
    users = UserUtil.check_email_exists(crud, emailStr)
    return users


@router.post("/users/block/{user_id}", response_model=User)
def block_user(user_id: int, db: Session = Depends(get_db)):
    logger.info("Creating user " + str(user_id))
    crud = UserRepository(db)
    db_user = UserUtil.check_id_exists(crud, user_id)
    if db_user.isBlock:
        logger.warn("User " + str(user_id) + " already blocked")
        raise HTTPException(
            status_code=400, detail=("User " + str(user_id) + " already blocked")
        )
    db_user.isBlock = True
    crud.update_user_with_id(db_user)
    return db_user
