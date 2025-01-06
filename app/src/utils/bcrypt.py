from passlib.context import CryptContext


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