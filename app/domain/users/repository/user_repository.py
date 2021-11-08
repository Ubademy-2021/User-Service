from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException
from app.domain.exceptions.user_not_found_error import UserNotFoundError
from app.domain.users.model.user import User, UserCreate
from app.adapters.database.users.model import UserDTO


class UserRepository:
    def __init__(self, session: Session):
        self.session: Session = session

    def get_user(self, user_id: int):
        return self.session.query(UserDTO).filter(UserDTO.id == user_id).first()

    def get_user_by_email(self, email: str):
        return self.session.query(UserDTO).filter(UserDTO.email == email).first()

    def get_user_by_username(self, username: str):
        return self.session.query(UserDTO).filter(UserDTO.userName == username).first()

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.session.query(UserDTO).offset(skip).limit(limit).all()

    def get_active_users(self):
        return self.session.query(UserDTO).filter(UserDTO.isBlock == False).all()

    def create_user(self, user: UserCreate):
        session_user = UserDTO()
        session_user.initWithUserCreate(user)
        self.session.add(session_user)
        self.session.commit()
        self.session.refresh(session_user)
        return session_user

    def update_user(self, db_user_id: int, user_updated: UserCreate):
        # Get the existing data
        db_user = (
            self.session.query(UserDTO).filter(UserDTO.id == db_user_id).one_or_none()
        )
        if db_user is None:
            raise UserNotFoundError()

        # Update model class variable from requested fields
        for var, value in vars(user_updated).items():
            setattr(db_user, var, value) if value or str(value) == 'False' else None

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def update_user_with_id(self, user_updated: User):
        # Only use with user gotten from database
        self.session.add(user_updated)
        self.session.commit()
        self.session.refresh(user_updated)
        return user_updated
