from pydantic import BaseModel
from typing import Optional
from . import model

class CreateOrderDetails(BaseModel):
    order_id: Optional[int] = None
    product_id: int
    quantity: int

def create_order_details(payload: list[CreateOrderDetails]):
    orderDetails = model.OrderDetails

    for item in payload:
        orderDetails = model.OrderDetails(
            order_id = item.order_id,
            product_id = item.product_id,
            quantity = item.quantity
        )

        yield orderDetails