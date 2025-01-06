from . import response, service, schemas
from fastapi import FastAPI, Depends, APIRouter, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from typing import List
from ..utils import response as response_util

class UserRouter:
    def __init__(self):
        app = None
        self.app = FastAPI()
        self.router = APIRouter(prefix="/users")


        @self.router.get("/")
        async def get_users(
            service : service.UserService = Depends(self.get_service)
        ):
            return "hello world"
        
        @self.app.get("/users/login", response_model=response.UserResponse)
        async def login_user(
            payload: schemas.LoginUser,
            service : service.UserService = Depends(self.get_service)
        ):
            user = None
            response = response_util.Custom_Response()
            try:
                user = service.login_user(payload)
            except Exception as e:
                response = response_util.Custom_Response(message=str(e))
            user = response.wrap_error(user)

            return user
        

        @self.app.get("/user/{user_id}", response_model=response.UserResponse)
        def get_user(
            user_id: int,
            service : service.UserService = Depends(self.get_service)
        ):
            user = None
            response = response_util.Custom_Response()
            try:
                user = service.get_user(user_id)
            except Exception as e:
                response = response_util.Custom_Response(message=str(e))
            user = response.wrap_error(user)

            return user

        @self.app.post("/users", status_code=status.HTTP_201_CREATED, response_model=response.CreateUserResponse)
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