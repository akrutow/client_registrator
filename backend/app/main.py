from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from dotenv import load_dotenv
import os


app = FastAPI()
load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

class LoginRequest(BaseModel):
    login: str
    password: str


class LoginResponse(BaseModel):
    ok: bool
    error: str | None = None
    token: str | None = None

@app.post('/login', response_model=LoginResponse)
def login(data: LoginRequest):
    if data.login == 'admin' and data.password == 'admin':
        return LoginResponse(ok=True, token='fake-jwt-token-12345')
    return LoginResponse(ok=False, error='Неверный логин или пароль')


if __name__ == '__main__':
    uvicorn.run(
        app,
        host=os.getenv('API_HOST', '127.0.0.1'),
        port=int(os.getenv('API_PORT', 8000))
    )