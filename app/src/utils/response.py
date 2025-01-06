from pydantic import BaseModel
from fastapi import HTTPException, status

NOT_FOUND = "data not found"
BAD_REQUEST = "bad request"
SUCCESS = "success"
NO_CONTENT = "no content"
CREATE_BY_ADMIN = "admin"

class ErrorMessage():
    messages = [{
        "status": "error",
        "message": "data not found"
    }]

class Custom_Response(BaseModel):
    message: str = SUCCESS

    
    def wrap_error(self, data: dict):
        if self.message == BAD_REQUEST:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= self.message)
        if self.message != SUCCESS:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= self.message)
        return data