from pydantic import BaseModel
from datetime import datetime


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    is_active: bool

class CreateUserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime