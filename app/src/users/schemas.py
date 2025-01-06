from pydantic import BaseModel,EmailStr
from typing import Optional

class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginUser(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: str