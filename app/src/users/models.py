from app.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, TIMESTAMP, func

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, server_default='False', nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(String, nullable=False, server_default="admin")
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_by = Column(String, nullable=False, server_default="admin")