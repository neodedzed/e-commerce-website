from pydantic import BaseModel

class UserRegister(BaseModel):
    name: str
    address: str
    phone: str
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str
