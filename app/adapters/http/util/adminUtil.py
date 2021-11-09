
from sqlalchemy.orm import Session
from app.domain.admins.repository.admin_repository import AdminRepository
from app.core.logger import logger
from fastapi import HTTPException


class AdminUtil:

    def check_email(session: Session, email):
        adminRepository = AdminRepository(session)
        db_admin = adminRepository.get_admin_by_email(email=email)
        if db_admin:
            logger.warn("Admin " + email + " already exsists")
            raise HTTPException(
                status_code=400, detail="Email " + email + " already registered"
            )

    def check_email_exists(session: Session, email):
        adminRepository = AdminRepository(session)
        db_admin = adminRepository.get_admin_by_email(email)
        if db_admin is None:
            logger.warning("Admin with email = " + email + " not found")
            raise HTTPException(status_code=400, detail="Admin not found")
        return db_admin

    def check_admin_exists(session: Session, admin_id):
        adminRepository = AdminRepository(session)
        db_admin = adminRepository.get_admin(admin_id=admin_id)
        if db_admin is None:
            logger.warning("Admin with id = " + str(admin_id) + " not found")
            raise HTTPException(status_code=404, detail="Admin not found")
        return db_admin
