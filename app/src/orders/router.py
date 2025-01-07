from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from . import service, schemas, response
from ..utils import response as response_util, auth as authentication


class OrderRouter:
    def __init__(self):
        self.router = APIRouter(
            prefix="/orders",
            tags=["Orders"]
        )
        self.jwt_middleware = authentication.JWTToken()

        @self.router.get("/", response_model=list[response.GetOrdersResponse])
        async def get_orders(
            service : service.OrderService = Depends(self.get_service),
            get_current_user: int = Depends(self.jwt_middleware.get_current_user)
        ):
            return service.get_orders()
        

        @self.router.get("/{order_id}")
        async def get_order_by_id(
            order_id : int,
            service : service.OrderService = Depends(self.get_service),
            get_current_user: int = Depends(self.jwt_middleware.get_current_user)
        ):

            order = None
            response = response_util.Custom_Response()
            try:
                order = service.get_order_by_id(order_id)
                print(order)
            except Exception as e:
                response = response_util.Custom_Response(message=str(e))
            order = response.wrap_error(order)

            return order

        @self.router.post("/", status_code=status.HTTP_201_CREATED)
        async def create_order(
            payload : schemas.CreateOrder,
            service : service.OrderService = Depends(self.get_service)
        ):
            order =None
            response = response_util.Custom_Response()
            try:
                order = service.create_order(payload)
            except Exception as e:
                response = response_util.Custom_Response(message=str(e))
            order = response.wrap_error(order)
            
            return order


    @staticmethod
    def get_service(db: Session = Depends(get_db)) -> service.OrderService:
        return service.OrderService(db)