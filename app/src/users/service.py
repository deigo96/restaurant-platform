from . import repository, schemas
from sqlalchemy.orm import Session
from app.db.database import  get_db
from fastapi import   Depends
from .. import constant
from ..utils import bcrypt

class UserService:
    def __init__(self, db : Session = Depends(get_db)): 
        self.repo = repository.UserRepository(db)

    def login_user(self, payload: schemas.LoginUser):
        if not payload.username and not payload.email:
            raise Exception(constant.BAD_REQUEST)
        
        user = None
        
        if payload.username:
            user = self.repo.get_user_by_username(payload.username)
        else:
            user = self.repo.get_user_by_email(payload.email)

        if not user:
            raise Exception(constant.NOT_FOUND)

        if not bcrypt.Bcrypt().verify(payload.password, user.password):
            print("invalid password")
            raise Exception(constant.BAD_REQUEST)

        return user

    def get_user(self, id: int):
        user =  self.repo.get_user(id)
        if not user:
            raise Exception(constant.NOT_FOUND)

        if not bcrypt.Bcrypt().verify("password123", user.password):
            print("invalid password")
            raise Exception(constant.BAD_REQUEST)

        return user
    
    def create_user(self, payload: schemas.CreateUser):
        user_email = self.repo.get_user_by_email(payload.email)
        if user_email:
            print("user email already exist")
            raise Exception(constant.BAD_REQUEST)

        user_username = self.repo.get_user_by_username(payload.username)
        if user_username:
            print("user username already exist")
            raise Exception(constant.BAD_REQUEST)
        
        hashed_password = bcrypt.Bcrypt().hash(payload.password)
        payload.password = hashed_password

        return self.repo.create_user(payload)