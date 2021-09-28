from sqlalchemy.orm import Session
from app.domain.users.model.user import User, UserCreate
from app.adapters.database.users.model import UserDTO


class UserRepository():
    def __init__(self, session: Session):
        self.session: Session = session

    def get_user(self, user_id: int):
        return db.query(UserDTO).filter(UserDTO.id == user_id).first()

    def get_user_by_email(self, email: str):
        return db.query(UserDTO).filter(UserDTO.email == email).first()

    def get_users(self, skip: int = 0, limit: int = 100):
        return db.query(UserDTO).offset(skip).limit(limit).all()

    def create_user(self, user: UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = UserDTO(email=user.email, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
