from app.adapters.database.database import SessionLocal
from app.adapters.database.users.model import UserDTO
from app.domain.users.model.user import UserCreate, User
from app.domain.users.repository.user_repository import UserRepository
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.logger import logger


router = APIRouter(tags=["users"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.critical("Database connection failed: " + e.__str__)
    finally:
        db.close()


@router.post("/users", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    logger.info("Creating user " + user.email)
    crud = UserRepository(db)
    db_user = crud.get_user_by_email(email=user.email)
    if db_user:
        logger.warn("User " + user.email + " already exsists")
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(user=user)


@router.get("/users", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logger.info("Getting users list")
    crud = UserRepository(db)
    users = crud.get_users(skip=skip, limit=limit)
    logger.debug("Getting " + str(users.count(UserDTO)) + " users")
    return users


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    logger.info("Getting user with id = " + user_id)
    crud = UserRepository(db)
    db_user = crud.get_user(user_id=user_id)
    if db_user is None:
        logger.warning("User with id = " + user_id + " not found")
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
