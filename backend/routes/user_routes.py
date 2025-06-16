from fastapi import APIRouter

user = APIRouter()

@user.get('/health')
def health_check_user(health:str='Fuck Youser'):
    return {
        'message' : f'EVERYBODY SAY {health}'
    }