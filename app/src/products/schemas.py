from pydantic import BaseModel
from typing import Optional

class PostValidation(BaseModel):
    id: Optional[int] = None
    name: str
    stock: int
    is_available: bool = False
    price: float


class UpdateValidation(BaseModel):
    is_available: Optional[bool] = None
    name: Optional[str] = None