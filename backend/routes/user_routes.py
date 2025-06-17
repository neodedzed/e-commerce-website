from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.user_crud import create_user
from database.db import get_db
from routes.schemas.user_schema import UserRegister

user = APIRouter()

@user.get('/health')
def health_check_user(health:str='Fuck Youser'):
    return {
        'message' : f'EVERYBODY SAY {health}'
    }
@user.post('/register')
def post_user(user: UserRegister, db: Session=Depends(get_db)):
    create_user(db,user)    
    return {
        'message': 'success'
    }
