from pydantic import BaseModel

class UserRegister(BaseModel):
    name: str
    username: str
    address: str
    phone: str
    password: str