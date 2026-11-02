import flet as ft
import httpx

def main(page: ft.Page):
    # Настройки страницы
    page.title = "Flet Фронтенд"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 450
    page.window.height = 400

    # Поля ввода
    name_input = ft.TextField(label="Ваше имя", width=300)
    job_input = ft.TextField(label="Ваша профессия", width=300)
    result_text = ft.Text(value="", color="blue", size=16, weight="bold")

    # Функция обработки клика
    def on_send_click(e):
        if not name_input.value or not job_input.value:
            result_text.value = "Заполните оба поля!"
            result_text.color = "red"
            page.update()
            return

        payload = {
            "name": name_input.value,
            "job": job_input.value
        }

        try:
            # Отправка запроса на бэкенд FastAPI
            response = httpx.post("http://localhost:8000/api/submit", json=payload, timeout=5.0)
            
            if response.status_code == 200:
                result_text.value = response.json()["message"]
                result_text.color = "green"
            else:
                result_text.value = f"Ошибка бэкенда: статус {response.status_code}"
                result_text.color = "red"
                
        except httpx.ConnectError:
            result_text.value = "Ошибка: Не удалось связаться с бэкендом (он запущен?)"
            result_text.color = "red"

        page.update()

    # В Flet 1.0+ вместо ElevatedButton используется просто Button, а вместо text — content
    send_button = ft.Button(content="Отправить на бэкэнд", on_click=on_send_click)

    # Собираем интерфейс
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Форма отправки данных", size=20, weight="bold"),
                        name_input,
                        job_input,
                        send_button,
                        ft.Divider(),
                        result_text
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15
                ),
                padding=20
            )
        )
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
