from pydantic import BaseModel
from typing import List
from . import model
from ..order_details import model as order_details_model, schemas as order_details_schemas

class CreateOrder(BaseModel):
    table: int
    customer_name: str
    order_details: List[order_details_schemas.CreateOrderDetails]

def create_order(payload: CreateOrder):
    orderModel = model.Order(
        table = payload.table,
        customer_name = payload.customer_name
    )

    return orderModel