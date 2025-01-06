from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

# from .models import products_model as models
from .db.database import engine, get_db
from .src.products import router as product_routers, models as product_models
from .src.users import router as user_routers, models as user_models
from .src.auth import router as auth_routers

product_models.Base.metadata.create_all(bind=engine)
user_models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_routers.UserRouter().router)
app.include_router(product_routers.ProductRouter().router)
app.include_router(auth_routers.AuthRouter().router)

# try:
#     conn = psycopg2.connect(
#         host="localhost",
#         database="fastapi",
#         user="postgres",
#         password="brengsek96",
#         cursor_factory=RealDictCursor
#     )

#     cursor = conn.cursor()
#     print("Database connection successful")
# except Exception as error:
#     print("Error: ", error)
# db = Database
# db.connect()

# user_routers.UserRouter(app=app)
# product_routers.ProductRouter(app=app)

# product_routes.ProductRoutes(app=app, db=get_db)


# @app.get("/products", response_model=List[products_responses.ResponseProduct])
# async def get_products(db: Session = Depends(get_db)):
#     # cursor.execute("""SELECT * FROM products""")
#     # products = cursor.fetchall()
#     products = db.query(models.Product).all()
#     db.query(models.Product)

#     return products


# @app.post("/products", status_code=status.HTTP_201_CREATED, response_model=products_responses.ResponseProduct)
# async def create_products(payload: products.PostValidation, db: Session = Depends(get_db)):
#     # cursor.execute("""INSERT INTO products (name, stock, is_available, price, created_by) VALUES (%s, %s, %s, %s, %s) RETURNING *""",
#     #                 (payload.name, payload.stock, payload.is_available, payload.price, CREATE_BY_ADMIN))

#     # new_product = cursor.fetchone()
#     # conn.commit()

#     new_product = models.Product(**payload.model_dump())

#     db.add(new_product)
#     db.commit()
#     db.refresh(new_product)

    
#     return new_product

# @app.get("/products/{id}", status_code=status.HTTP_200_OK, response_model=products_responses.ResponseProduct)
# def get_product(id: int, db: Session = Depends(get_db)):
#     # cursor.execute("""SELECT * FROM products WHERE id = %s""", (id,))
#     # product = cursor.fetchone()

#     product = db.query(models.Product).filter(models.Product.id == id).first()

#     response = responses.Custom_Response()
#     if not product:
#         response = responses.Custom_Response(message=responses.NOT_FOUND)
#     product = response.wrap_error(product)
#     return product

# @app.put("/products/{id}", response_model=products_responses.ResponseProduct)
# def update_product(id: int, payload: products.UpdateValidation, db: Session = Depends(get_db)):
#     # cursor.execute("""UPDATE products SET is_available = %s WHERE id = %s RETURNING *""", (payload.is_available, id))
#     # updated_product = cursor.fetchone()
#     # conn.commit()

#     query = db.query(models.Product).filter(models.Product.id == id)
#     updated_product = query.first()

#     response = responses.Custom_Response()
#     if not updated_product:
#         response = responses.Custom_Response(message=responses.NOT_FOUND)
#     updated_product = response.wrap_error(updated_product)

#     query.update(payload.model_dump(exclude_unset=True), synchronize_session=False)
#     db.commit()

#     return updated_product

# @app.delete("/products/{id}")
# def delete_product(id: int, db: Session = Depends(get_db)):
#     # cursor.execute("""DELETE FROM products WHERE id = %s RETURNING *""", (id,))
#     # deleted_product = cursor.fetchone()
#     # conn.commit()

#     deleted_product = db.query(models.Product).filter(models.Product.id == id)

#     response = responses.Custom_Response()
#     if not deleted_product.first():
#         response = responses.Custom_Response(message=responses.NOT_FOUND)
#     deleted_product = response.wrap_error(deleted_product)

#     deleted_product.delete(synchronize_session=False)
#     db.commit()

#     return Response(status_code=status.HTTP_204_NO_CONTENT)