from . import response, service, schemas
from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from ..utils import response as response_util


class AuthRouter:
    def __init__(self):
        self.router = APIRouter(
            prefix="/auth",
            tags=["auth"],
        )

        @self.router.post("/login", response_model=response.UserLoginResponse)
        async def login_user(
            payload: schemas.UserLogin,
            service : service.AuthService = Depends(self.get_service)                    
        ):
            user = None
            response = response_util.Custom_Response()
            try:
                user = service.login_user(payload)
            except Exception as e:
                response = response_util.Custom_Response(message=str(e))
            user = response.wrap_error(user)

            return user
        
    @staticmethod
    def get_service(db: Session = Depends(get_db)) -> service.AuthService:
        return service.AuthService(db)