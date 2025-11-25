import flet as ft


class SearchBar(ft.UserControl):
    def __init__(self, on_search):
        super().__init__()
        self.on_search = on_search

    def build(self):
        self.search_field = ft.TextField(
            hint_text="Buscar ciudad...",
            prefix_icon=ft.icons.SEARCH,
            on_submit=self.search_city,
            expand=True
        )

        self.search_button = ft.IconButton(
            icon=ft.icons.SEARCH,
            on_click=self.search_city,
            tooltip="Buscar"
        )

        return ft.Row([
            self.search_field,
            self.search_button
        ])

    def search_city(self, e):
        city = self.search_field.value.strip()
        if city:
            self.on_search(city)