from sqlalchemy.orm import Session
from app.domain.users.model.user import UserCreate
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

    def create_user(self, user: UserCreate):
        session_user = UserDTO()
        session_user.initWithUserCreate(user)
        self.session.add(session_user)
        self.session.commit()
        self.session.refresh(session_user)
        return session_user
