from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import product_routes, user_routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_headers=['*'],
    allow_methods=['*'],
    allow_credentials=['*']
)

app.include_router(user_routes.user_router, prefix='/user')
app.include_router(product_routes.product_router,prefix='/product')

@app.get('/health')
def health_check(health: str="FUCK YEAH!!"):
    return {
        'message': f'Everybody say {health}'
    }

    
    