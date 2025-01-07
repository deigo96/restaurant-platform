from pydantic import BaseModel
from datetime import datetime
from typing import List
from ..order_details.response import OrderDetailsResponse
from ..order_details import model as order_details_model


class GetOrdersResponse(BaseModel):
    id: int
    table: int
    customer_name: str
    total_amount: float
    is_paid: bool
    created_at: datetime

class GetOrderResponse(GetOrdersResponse):
    order_details: List[OrderDetailsResponse]

def order_detail_to_response(order_details: list[order_details_model.OrderDetails]):
    return [OrderDetailsResponse(**order_detail.__dict__) for order_detail in order_details]