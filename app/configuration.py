from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = getenv("SECRET_KEY")
    ALGORITHM = getenv("ALGORITHM")
    print(f"minutes {getenv("ACCESS_TOKEN_EXPIRE_MINUTES")}")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    
    DATABASE_HOST = getenv("DATABASE_HOST")
    DATABASE_USER = getenv("DATABASE_USER")
    DATABASE_PASSWORD = getenv("DATABASE_PASSWORD")
    DATABASE_NAME = getenv("DATABASE_NAME")
    DATABASE_PORT = getenv("DATABASE_PORT")
