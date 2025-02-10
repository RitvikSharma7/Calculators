import flet as ft

# Custom Button Class
class calculatorButton(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__(text=text, bgcolor="#808080", color="white", width=60, height=50, on_click = on_click)

class clearButton(ft.ElevatedButton):
    def __init__(self, on_click):
        super().__init__(text="C", bgcolor="red", color="white", width=125, height=50, on_click= on_click)
