from . import repository, schemas
from sqlalchemy.orm import Session
from app.db.database import  get_db
from fastapi import   Depends

class ProductService(object):
    def __init__(self, db : Session = Depends(get_db)): 
        self.repo = repository.ProductRepository(db)

    def get_products(self):
        return self.repo.get_products()
    
    def create_product(self, payload: schemas.PostValidation):
        return self.repo.create_product(payload)
    
    def get_product(self, id: int):
        return self.repo.get_product(id)
    
    def update_product(self, id: int, payload: schemas.UpdateValidation):
        updated_product = self.repo.update_product(id, payload)
        return updated_product
    
    def delete_product(self, id: int):
        return self.repo.delete_product(id)