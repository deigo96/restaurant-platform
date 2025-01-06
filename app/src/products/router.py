from . import response, service, schemas
from fastapi import Depends, Response, status, APIRouter
from sqlalchemy.orm import Session
from app.db.database import get_db
from typing import List
from ..utils import response as response_util

class ProductRouter:
    def __init__(self):
        self.router = APIRouter(
            prefix="/products",
            tags=["Products"]
            )

        @self.router.get("/", response_model=List[response.ResponseProduct])
        async def get_products(
            service : service.ProductService = Depends(self.get_service)
        ):
            
            return service.get_products()
        
        @self.router.post("/", status_code=status.HTTP_201_CREATED, response_model=response.ResponseProduct)
        async def create_products(
            payload: schemas.PostValidation,
            service : service.ProductService = Depends(self.get_service)
        ):
            return service.create_product(payload)
        
        @self.router.get("/{product_id}", response_model=response.ResponseProduct)
        async def get_product(
            product_id: int,
            service : service.ProductService = Depends(self.get_service)
        ):
            product = service.get_product(product_id)
            response = response_util.Custom_Response()
            if not product:
                response = response_util.Custom_Response(message=response_util.NOT_FOUND)
            product = response.wrap_error(product)

            return product
        
        @self.router.put("/{product_id}", response_model=response.ResponseProduct)
        async def update_product(
            product_id: int,
            payload: schemas.UpdateValidation,
            service : service.ProductService = Depends(self.get_service)
        ):
            updated_product = service.update_product(product_id, payload)
            response = response_util.Custom_Response()
            if not updated_product:
                response = response_util.Custom_Response(message=response_util.NOT_FOUND)
            updated_product = response.wrap_error(updated_product)

            return updated_product

        @self.router.delete("/{product_id}")
        async def delete_product(
            product_id: int,
            service : service.ProductService = Depends(self.get_service)
        ):
            
            response = response_util.Custom_Response()
            deleted_product = None
            try:
                deleted_product = service.delete_product(product_id)
            except Exception as e:
                response = response_util.Custom_Response(message=str(e))
            deleted_product = response.wrap_error(deleted_product)

            return Response(status_code=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def get_service(db: Session = Depends(get_db)) -> service.ProductService:
        return service.ProductService(db)