from pydantic import BaseModel
from typing import List

class ResponseProduct(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    is_available: bool

    # class Config:
    #     from_attributes  = True

class ResponseProducts(BaseModel):
    products: List[ResponseProduct]