from datetime import datetime
from pydantic import BaseModel

class UserLoginResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    is_active: bool
    access_token: str
    token_type: str = "Bearer "

    