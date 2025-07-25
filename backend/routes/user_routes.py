from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.user_crud import create_user, user_login
from database.db import get_db
from routes.schemas.user_schema import UserLogin, UserRegister

user_router = APIRouter()

@user_router.post('/register')
def post_user(user: UserRegister, db: Session=Depends(get_db)):
    '''
    Handling User Registration
    '''
    create_user(db,user)    
    return {
        'message': 'success'
    }

@user_router.post('/login')
def post_user_login(user: UserLogin, db: Session=Depends(get_db)):
    '''
    Handling user login
    '''
    message='Incorrect credentials'
    if(user_login(db,user)):
        message='success'
        
    return {
        'message': message 
    }