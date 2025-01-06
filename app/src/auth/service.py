from . import schemas
from sqlalchemy.orm import Session
from app.db.database import  get_db
from fastapi import   Depends
from .. import constant
from ..utils import auth as authentication
from ..users import repository as users_repository

class AuthService:
    def __init__(self, db : Session = Depends(get_db)): 
        self.repo = users_repository.UserRepository(db)
        self.jwt_token = authentication.JWTToken()

    def login_user(self, payload: schemas.UserLogin):
        if not payload.username and not payload.email:
            raise Exception(constant.BAD_REQUEST)
        
        user = None
        
        if payload.username:
            user = self.repo.get_user_by_username(payload.username)
        else:
            user = self.repo.get_user_by_email(payload.email)

        if not user:
            raise Exception(constant.NOT_FOUND)

        if not authentication.Bcrypt().verify(payload.password, user.password):
            print("invalid password")
            raise Exception(constant.BAD_REQUEST)
        
        access_token = self.jwt_token.create_token({"user_id": user.id})

        user_response = user.__dict__
        user_response["access_token"] = access_token

        return user

    def get_user(self, id: int):
        user =  self.repo.get_user(id)
        if not user:
            raise Exception(constant.NOT_FOUND)

        if not authentication.Bcrypt().verify("password123", user.password):
            print("invalid password")
            raise Exception(constant.BAD_REQUEST)

        return user
    