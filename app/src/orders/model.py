from app.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, TIMESTAMP, func, ForeignKey

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    table = Column(Integer, nullable=False)
    customer_name = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False, default=0.0)
    is_paid = Column(Boolean, server_default='False', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(String, nullable=False, server_default="admin")
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_by = Column(String, nullable=False, server_default="admin")