from sqlalchemy.orm import Session
from app.db.database import  get_db
from fastapi import Depends 
from . import repository, model, schemas, response
from ..order_details import model as order_details, schemas as order_details_schema, service as order_details_service
from ..products import service as product_service

class OrderService:
    def __init__(self, db : Session = Depends(get_db)): 
        self.repo = repository.OrderRepository(db)
        self.order_details_service = order_details_service.OrderDetailsService(db)
        self.product_service = product_service.ProductService(db)
        self.db = db

    def get_order_by_id(self, order_id : int):
        order_response =  self.repo.get_order_by_id(order_id)
        print(f"order response {order_response}")

        order_detail_response = self.order_details_service.get_order_details(order_id)
        print(f"order detail response {order_detail_response}")

        detail = response.GetOrderResponse(
            id=order_response.id,
            table=order_response.table,
            customer_name=order_response.customer_name,
            total_amount=order_response.total_amount,
            is_paid=order_response.is_paid,
            created_at=order_response.created_at,
            order_details=response.order_detail_to_response(order_detail_response)
        )

        print(f"detail {detail}")

        return response.GetOrdersResponse(
            id=order_response.id,
            table=order_response.table,
            customer_name=order_response.customer_name,
            total_amount=order_response.total_amount,
            is_paid=order_response.is_paid,
            created_at=order_response.created_at,
            order_details=detail)



    def get_orders(self):
        orders =  self.repo.get_orders()

        return orders

    def create_order(self, payload: schemas.CreateOrder):
        try:
            self.db.begin()
            order = self.repo.create_order(schemas.create_order(payload))

            self.db.flush()

            OrderDetailsSchema = order_details_schema.create_order_details(payload.order_details)

            for order_detail in OrderDetailsSchema:
                order_detail.order_id = order.id
                self.order_details_service.create_order_details(order_detail)

            self.db.commit()
            self.db.refresh(order)
        except:
            self.db.rollback()
            raise
        

        return order