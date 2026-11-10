from nicegui import ui, app
import httpx

from dotenv import load_dotenv
import os


load_dotenv()
API_URL = f'http://{os.getenv('API_HOST')}:{os.getenv('API_PORT')}'
STORAGE_SECRET = os.getenv('STORAGE_SECRET')


@ui.page('/login')
def login_page():
    if app.storage.user.get('token'):
        ui.navigate.to('/home')
        return

    with ui.column().classes('min-h-screen items-center justify-center w-full'):
        with ui.card().classes('w-full max-w-md p-8 shadow-xl'):
            ui.label('Вход в систему').classes('text-2xl font-bold text-center mb-6')

            login_input = ui.input('Login').classes('w-full')
            pass_input = ui.input('Password', password=True, password_toggle_button=True).classes('w-full')
            error_label = ui.label('').classes('text-red-500 text-sm')

            async def do_login():
                error_label.text = ''
                if not login_input.value or not pass_input.value:
                    error_label.text = 'Заполните все поля'
                    return

                async with httpx.AsyncClient() as client:
                    response = await client.post(
                        f'{API_URL}/login',
                        json={'login': login_input.value, 'password': pass_input.value}
                    )
                    data = response.json()

                    if data.get('ok'):
                        app.storage.user['token'] = data['token']
                        app.storage.user['login'] = login_input.value
                        ui.navigate.to('/home')
                    else:
                        error_label.text = data.get('error', 'Ошибка входа')

            ui.button('Войти', on_click=do_login).classes('w-full mt-4')