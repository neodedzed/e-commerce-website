from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import user_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_headers=['*'],
    allow_methods=['*'],
    allow_credentials=['*']
)

app.include_router(user_routes.user, prefix='/user')

@app.get('/health')
def health_check(health: str="FUCK YEAH!!"):
    return {
        'message': f'Everybody say {health}'
    }

    
    