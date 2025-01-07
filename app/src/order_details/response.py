from pydantic import BaseModel
from datetime import datetime

class ProductOrderDetails(BaseModel):
    name : str
    price : float

class OrderDetailsResponse(BaseModel):
    id: int
    quantity: int
    created_at: datetime
    product: ProductOrderDetails
