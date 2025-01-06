from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from app import configuration
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from ..auth import schemas
from typing import Annotated

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")


class Bcrypt(CryptContext):
    def __init__(self):
        super().__init__(
            schemes=["bcrypt"],
            deprecated="auto",
        )

    def verify(self, plain_password, hashed_password):
        return super().verify(plain_password, hashed_password)
    
    def hash(self, password):
        return super().hash(password)
    
class JWTToken:
    def __init__(self):
        self.config = configuration.Config

    def create_token(self, payload: dict, expires_delta: int = None):
        to_encode = payload.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + timedelta(seconds=expires_delta)
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=self.config.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        access_token = jwt.encode(to_encode, self.config.SECRET_KEY, algorithm=self.config.ALGORITHM)
        return access_token
    
    def verify_access_token(self, token, credentials_exception):
        try:
            payload = jwt.decode(token, self.config.SECRET_KEY, algorithms=[self.config.ALGORITHM])
            id = payload.get("user_id")
            if id is None:
                raise credentials_exception
            token_data = schemas.TokenData(id=str(id))
        except InvalidTokenError:
            raise credentials_exception
        
        return token_data
    
    def get_current_user(self, token: Annotated[str, Depends(oauth2_schema)]):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Could not validate credentials", 
            headers={"WWW-Authenticate": "Bearer"}
        )

        user_id = self.verify_access_token(token, credentials_exception)
        return user_id