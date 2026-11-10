from nicegui import ui, app


@ui.page('/home')
def home_page():
    token = app.storage.user.get('token')
    if not token:
        ui.navigate.to('/login')
        return

    user_login = app.storage.user.get('login', 'Неизвестный')

    with ui.column().classes('min-h-screen items-center justify-center w-full'):
        with ui.card().classes('p-8 shadow-xl text-center'):
            ui.label(f'Hello, {user_login}').classes('text-2xl font-bold')
            ui.label(f'Ваш токен: {token}').classes('text-gray-500 text-sm mt-2')

        def logout():
            app.storage.user.clear()
            ui.navigate.to('/login')

        ui.button('Выйти', on_click=logout).classes('mt-6 bg-red-500 text-white')