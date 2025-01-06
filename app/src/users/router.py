from . import response, service, schemas
from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from typing import List
from ..utils import response as response_util
from ..utils import auth as authentication

class UserRouter:
    def __init__(self):
        self.router = APIRouter(
            prefix="/users",
            tags=["users"],)
        self.jwt_middleware = authentication.JWTToken()

        @self.router.get("/")
        async def get_users(
            service : service.UserService = Depends(self.get_service)
        ):
            return "hello world"
        
        @self.router.get("/{user_id}", response_model=response.UserResponse)
        def get_user(
            user_id: int,
            service : service.UserService = Depends(self.get_service),
            get_current_user: int = Depends(self.jwt_middleware.get_current_user)
        ):
            response = response_util.Custom_Response()
            try:
                user = service.get_user(user_id)
            except Exception as e:
                response = response_util.Custom_Response(message=str(e))
            user = response.wrap_error(user)

            return user

        @self.router.post("/", status_code=status.HTTP_201_CREATED, response_model=response.CreateUserResponse)
        async def create_users(
            payload: schemas.CreateUser,
            service : service.UserService = Depends(self.get_service)
        ):
            created_user = None
            response = response_util.Custom_Response()
            try:
                created_user = service.create_user(payload)
            except Exception as e:
                response = response_util.Custom_Response(message=str(e))
            created_user = response.wrap_error(created_user)

            return created_user


    @staticmethod
    def get_service(db: Session = Depends(get_db)) -> service.UserService:
        return service.UserService(db)