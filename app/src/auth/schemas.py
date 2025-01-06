from pydantic import BaseModel, EmailStr
from typing import Optional

class UserLogin(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: str

class TokenData(BaseModel):
    id: Optional[str] = None