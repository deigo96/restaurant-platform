from . import repository, schemas
from sqlalchemy.orm import Session
from app.db.database import  get_db
from fastapi import   Depends
from .. import constant
from ..utils import auth as authentication

class UserService:
    def __init__(self, db : Session = Depends(get_db)): 
        self.repo = repository.UserRepository(db)

    def get_user(self, id: int):
        user =  self.repo.get_user(id)
        if not user:
            raise Exception(constant.NOT_FOUND)


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
        
        hashed_password = authentication.Bcrypt().hash(payload.password)
        payload.password = hashed_password

        return self.repo.create_user(payload)