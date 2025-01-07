from app.db.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, func, ForeignKey

class OrderDetails(Base):
    __tablename__ = "order_details"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(String, nullable=False, server_default="admin")
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_by = Column(String, nullable=False, server_default="admin")