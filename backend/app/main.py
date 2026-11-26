from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
import os

from backend.app.routers import users
from backend.app import models


app = FastAPI()
load_dotenv()

app.include_router(users.router, prefix='/api')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
async def root():
    '''Корневой маршрут, подтверждающий, что API работает.'''
    return {'message': 'Добро пожаловать в API'}


# @app.post('/login', response_model=LoginResponse)
# def login(data: LoginRequest):
#     if data.login == 'admin' and data.password == 'admin':
#         return LoginResponse(ok=True, token='fake-jwt-token-12345')
#     return LoginResponse(ok=False, error='Неверный логин или пароль')
# тут пришел запрос с фронта с введенным логином и паролем. 
# далее идет логика и ответ на фронт


if __name__ == '__main__':
    uvicorn.run(
        app,
        host=os.getenv('API_HOST', '127.0.0.1'),
        port=int(os.getenv('API_PORT', 8000))
    )