from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from app.adapters.database.database import Base
from app.domain.users.model.user import UserCreate
from app.core.logger import logger

# catedra hacen Base=declarative_base()


class UserDTO(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    user_name = Column(String, unique=True)
    name = Column(String)
    last_name = Column(String)
    phone_number = Column(String, nullable=True, default=None)
    street = Column(String)
    street_nbr = Column(Integer)
    floor_appt = Column(String)
    local = Column(String)
    postal_code = Column(String)
    is_active = Column(Boolean, default=True)

    def initWithUserCreate(self, user: UserCreate):

        self.email = user.email
        self.hashed_password = user.password
        self.user_name = user.user_name
        self.name = user.name
        self.last_name = user.last_name
        if user.phone_number:
            self.phone_number = user.phone_number
        self.street = user.street
        self.street_nbr = user.street_nbr
        self.floor_appt = user.floor_appt
        self.local = user.local
        self.postal_code = user.postal_code
