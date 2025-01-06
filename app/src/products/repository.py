from . import models 
from sqlalchemy.orm import Session
from app.db.database import  get_db
from fastapi import   Depends
from . import schemas
from .. import constant


class ProductRepository:
    def __init__(self, db : Session):
        self.db = db 

    def get_products(self):
        return self.db.query(models.Product).all()

    def create_product(self, payload: schemas.PostValidation):

        new_product = models.Product(**payload.model_dump())
        self.db.add(new_product)
        self.db.commit()
        self.db.refresh(new_product)

        return new_product
    
    def get_product(self, id: int):
        return self.db.query(models.Product).filter(models.Product.id == id).first()
    
    def update_product(self, id: int, payload: schemas.UpdateValidation):

        query = self.db.query(models.Product).filter(models.Product.id == id)
        updated_product = query.first()

        if not updated_product:
            return None

        query.update(payload.model_dump(exclude_unset=True), synchronize_session=False)
        self.db.commit()

        return updated_product
    
    def delete_product(self, id: int):
        deleted_product = self.db.query(models.Product).filter(models.Product.id == id)

        if not deleted_product.first():
            raise Exception (constant.NOT_FOUND)

        deleted_product.delete(synchronize_session=False)
        self.db.commit()