from app.adapters.database.database import Base
from app.domain.admins.model.admin import AdminBase
from sqlalchemy import Column, Integer, String

# catedra hacen Base=declarative_base()


class AdminDTO(Base):
    __tablename__ = "admin"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    surname = Column(String)

    def initWithAdminCreate(self, admin: AdminBase):

        self.email = admin.email
        self.name = admin.name
        self.surname = admin.surname
