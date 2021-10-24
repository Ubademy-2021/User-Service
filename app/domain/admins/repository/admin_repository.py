from sqlalchemy.orm import Session
from app.domain.admins.model.admin import AdminBase
from app.adapters.database.admins.model import AdminDTO


class AdminRepository:
    def __init__(self, session: Session):
        self.session: Session = session

    def get_admin_by_email(self, email: str):
        return self.session.query(AdminDTO).filter(AdminDTO.email == email).first()

    def get_admins(self, skip: int = 0, limit: int = 100):
        return self.session.query(AdminDTO).offset(skip).limit(limit).all()

    def create_user(self, admin: AdminBase):
        session_admin = AdminDTO()
        session_admin.initWithUserCreate(admin)
        self.session.add(session_admin)
        self.session.commit()
        self.session.refresh(session_admin)
        return session_admin
