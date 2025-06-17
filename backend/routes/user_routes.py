from fastapi import APIRouter

from routes.schemas.user_schema import UserRegister

user = APIRouter()

@user.get('/health')
def health_check_user(health:str='Fuck Youser'):
    return {
        'message' : f'EVERYBODY SAY {health}'
    }
@user.post('/register')
def post_user(user: UserRegister):
    print(user)
    return {
        'message': 'success'
    }
