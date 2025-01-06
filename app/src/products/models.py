from app.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, TIMESTAMP, func

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    is_available = Column(Boolean, server_default='False', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(String, nullable=False, server_default="admin")
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_by = Column(String, nullable=False, server_default="admin")

