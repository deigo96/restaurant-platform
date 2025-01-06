from datetime import datetime
from pydantic import BaseModel

class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

    