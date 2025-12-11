import flet as ft


# 1. Heredar de ft.Row en lugar de ft.UserControl
class SearchBar(ft.Row):
    def __init__(self, on_search):
        super().__init__()
        self.on_search = on_search

        # 2. Configurar controles (Movido desde build a __init__)
        self.search_field = ft.TextField(
            hint_text="Buscar ciudad...",
            prefix_icon=ft.Icons.SEARCH,
            on_submit=self.search_city,
            expand=True
        )

        self.search_button = ft.IconButton(
            icon=ft.Icons.SEARCH,
            on_click=self.search_city,
            tooltip="Buscar"
        )

        # 3. Asignar los controles a la propiedad self.controls de la Fila (Row)
        # En lugar de hacer return ft.Row([...])
        self.controls = [
            self.search_field,
            self.search_button
        ]

    # El método build() se elimina.

    def search_city(self, e):
        city = self.search_field.value.strip()
        if city:
            self.on_search(city)