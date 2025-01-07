from sqlalchemy.orm import Session
from app.db.database import  get_db
from fastapi import Depends
from . import repository, model

class OrderDetailsService:
    def __init__(self, db : Session = Depends(get_db)): 
        self.repo = repository.OrderDetailsRepository(db)
    
    def get_order_details(self, order_id: int):
        return self.repo.get_order_details(order_id)
    
    def create_order_details(self, payload: model.OrderDetails):

        return self.repo.create_order_details(payload)