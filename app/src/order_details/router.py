from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from . import service

class OrderRouter:
    def __init__(self):
        self.router = APIRouter(
            prefix="/orders",
            tags=["Orders"]
        )

        @self.router.post("/", status_code=status.HTTP_201_CREATED)
        async def create_order(
            service : service.OrderDetailsService = Depends(self.get_service)
        ):

            return
        


        @staticmethod
        def get_service(db: Session = Depends(get_db)) -> service.OrderDetailsService:
            return service.OrderDetailsService(db)