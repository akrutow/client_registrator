import flet as ft


def main(page: ft.Page):
    page.title = "Text theme styles"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    ft.Text(
                        'R E G I S T R A T O R',
                        theme_style=ft.TextThemeStyle.HEADLINE_SMALL,
                    ),
                    ft.TextField(label='Login', width=300),
                    ft.TextField(label='Password', width=300, password=True, can_reveal_password=True),
                    ft.Container(
                        content=ft.Checkbox(label='Запомнить меня'),
                        width=300,
                        alignment=ft.Alignment.CENTER_LEFT,
                    ),
                    ft.Button(content='Войти', width=150),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            ),
        ),
    )


if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)