from sqlalchemy.orm import Session
from . import model

class OrderRepository():
    def __init__(self, db : Session): 
        self.db = db

    def get_orders(self):
        return self.db.query(model.Order).order_by(model.Order.id).all()
    
    def get_order_by_id(self, order_id: int):
        return self.db.query(model.Order).filter(model.Order.id == order_id).first()

    def get_order(self, table : int, customer_name : str):
        query = self.db.query(model.Order)
        
        if table :
            order = query.filter(model.Order.table == table).first()
        if customer_name :
            order = query.filter(model.Order.customer_name == customer_name).first()

        return order
    
    def create_order(self, payload: model.Order):
        self.db.add(payload)

        return payload
    
    def update_order(self, id: int, payload: model.Order):
        order = self.db.query(model.Order).filter(model.Order.id == id).first()

        if not order:
            return None

        order.table = payload.table
        order.customer_name = payload.customer_name

        self.db.commit()
        self.db.refresh(order)

        return order