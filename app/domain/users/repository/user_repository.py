from sqlalchemy.orm import Session
from app.domain.users.model.user import User, UserCreate
from app.adapters.database.users.model import UserDTO


class UserRepository():
    def __init__(self, session: Session):
        self.session: Session = session

    def get_user(self, user_id: int):
        return self.session.query(UserDTO).filter(UserDTO.id == user_id).first()

    def get_user_by_email(self, email: str):
        return self.session.query(UserDTO).filter(UserDTO.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.session.query(UserDTO).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        session_user = UserDTO(email=user.email, hashed_password=fake_hashed_password)
        self.session.add(session_user)
        self.session.commit()
        self.session.refresh(session_user)
        return session_user
