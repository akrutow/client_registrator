from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Мой Пет-Бэкенд")

# НАСТРОЙКА CORS: разрешаем фронтенду общаться с бэкендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешает запросы с любых портов и адресов
    allow_credentials=True,
    allow_methods=["*"],  # Разрешает GET, POST, OPTIONS и т.д.
    allow_headers=["*"],  # Разрешает любые заголовки
)

# Описываем структуру данных, которую ожидаем получить от фронтенда
class UserData(BaseModel):
    name: str
    job: str

# Эндпоинт, который принимает данные и возвращает JSON ответ
@app.post("/api/submit")
async def handle_submit(data: UserData):
    # Здесь в реальном проекте была бы логика сохранения в базу данных
    processing_message = f"Привет, {data.name}! Бэкенд успешно обработал твою профессию: {data.job}."
    
    return {
        "status": "success",
        "message": processing_message
    }
