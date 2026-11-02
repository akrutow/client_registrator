import flet as ft


class LoginView(ft.View):
    def init(self, page: ft.Page):
        return super().__init__(
            route='/',
            controls=[
                ft.SafeArea(
                    content=ft.Column(
                        controls=[
                            ft.Text('R E G I S T R A T O R', ft.TextThemeStyle.HEADLINE_SMALL),
                        ],
                    ),
                ),
            ],
        )