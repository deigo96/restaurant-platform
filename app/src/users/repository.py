from . import models 
from sqlalchemy.orm import Session
from app.db.database import  get_db
from fastapi import   Depends
from . import schemas
from .. import constant

class UserRepository:
    def __init__(self, db : Session): 
        self.db = db

    def get_user(self, id: int):
        user = self.db.query(models.User).filter(models.User.id == id).first()
        return user
    
    def get_user_by_email(self, email: str):
        return self.db.query(models.User).filter(models.User.email == email).first()
    
    def get_user_by_username(self, username: str):
        return self.db.query(models.User).filter(models.User.username == username).first()

    def create_user(self, payload: schemas.CreateUser):
        new_user = models.User(**payload.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return new_user