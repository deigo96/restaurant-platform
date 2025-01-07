from sqlalchemy.orm import Session
from . import model

class OrderDetailsRepository:
    def __init__(self, db : Session): 
        self.db = db

    def get_order_details(self, order_id: int):
        order_details = self.db.query(model.OrderDetails).filter(model.OrderDetails.order_id == order_id).all()

        return order_details
    
    def create_order_details(self, payload: model.OrderDetails):
        self.db.add(payload)
        self.db.commit()
        self.db.refresh(payload)

        return payload
    
    def update_order_details(self, id: int, payload: model.OrderDetails):
        order_details = self.db.query(model.OrderDetails).filter(model.OrderDetails.id == id).first()

        if not order_details:
            return None

        order_details.order_id = payload.order_id
        order_details.product_id = payload.product_id
        order_details.quantity = payload.quantity

        self.db.commit()
        self.db.refresh(order_details)

        return order_details