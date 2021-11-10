
from sqlalchemy.orm import Session
from app.domain.users.repository.user_repository import UserRepository
from app.core.logger import logger
from fastapi import HTTPException


class UserUtil:

    def check_username(session: Session, username):
        userRepository = UserRepository(session)
        db_user = userRepository.get_user_by_username(username=username)
        if db_user:
            logger.warning("Username " + username + " already in use")
            raise HTTPException(
                status_code=400, detail="Username " + username + " already in use"
            )

    def check_email(session: Session, email):
        userRepository = UserRepository(session)
        db_user = userRepository.get_user_by_email(email=email)
        if db_user:
            logger.warning("User " + email + " already exsists")
            raise HTTPException(
                status_code=400, detail="Email " + email + " already registered"
            )

    def check_email_exists(session: Session, email):
        userRepository = UserRepository(session)
        db_user = userRepository.get_user_by_email(email)
        if db_user is None:
            logger.warning("User with email = " + email + " not found")
            raise HTTPException(status_code=400, detail="User not found")
        return db_user

    def check_user_exists(session: Session, userId):
        userRepository = UserRepository(session)
        db_user = userRepository.get_user(user_id=userId)
        if db_user is None:
            logger.warning("User with id = " + str(userId) + " not found")
            raise HTTPException(status_code=404, detail="User not found")
        return db_user
