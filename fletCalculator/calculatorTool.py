import flet as ft
from fletWidgets import calculatorButton, clearButton

def main(page: ft.Page):
    page.title = "Calculator"
    page.bgcolor = "#232B2B"
    page.window_width = 300  
    page.window_height = 500  
    page.window_resizable = False

    result_display = ft.TextField(
        hint_text="000000000",
        value="",
        read_only=True,
        width=280,
        height=50,
        text_align=ft.TextAlign.RIGHT,
        color="white",
        bgcolor="blue",
    )

    def click_calc_btn(e):
        if e.control.text == '=':
            if result_display.value:  
                try:
                    result_display.value = str(eval(result_display.value))  
                except Exception:
                    result_display.value = "Error" 
            result_display.update()  
        else:
            result_display.value += e.control.text  
            result_display.update()  

    def clear_calc_screen(e):
        result_display.value = ""
        result_display.update()

    def del_char(e):
        result_display.value = result_display.value[:-1]
        result_display.update()

    display_container = ft.Container(
        content=ft.Row([result_display], alignment=ft.MainAxisAlignment.END, expand=True),
        padding=10,
        width=280,
        height=100
    )

    col1_buttons = ['7', '4', '1', '0'] 
    col2_buttons = ['8', '5', '2', '.']
    col3_buttons = ['9', '6', '3', '=']
    col4_buttons = ['/', '*', '-', '+']

    column_1 = ft.Column([calculatorButton(btn, on_click=click_calc_btn) for btn in col1_buttons], spacing=7)
    column_2 = ft.Column([calculatorButton(btn, on_click=click_calc_btn) for btn in col2_buttons], spacing=7)
    column_3 = ft.Column([calculatorButton(btn, on_click=click_calc_btn) for btn in col3_buttons], spacing=7)
    column_4 = ft.Column([calculatorButton(btn, on_click=click_calc_btn) for btn in col4_buttons], spacing=7)

    del_btn = calculatorButton("Del", on_click=del_char)
    clear_btn = clearButton(on_click=clear_calc_screen)

    button_row_top = ft.Row([del_btn, clear_btn], alignment=ft.MainAxisAlignment.END, width=280)
    button_row = ft.Row([column_1, column_2, column_3, column_4], alignment=ft.MainAxisAlignment.CENTER, spacing=7, tight=True)

    layout = ft.Column(
        [display_container, ft.Container(button_row_top, alignment=ft.alignment.center, padding=5, width=280), ft.Container(button_row, alignment=ft.alignment.center, width=280)],
        alignment=ft.MainAxisAlignment.CENTER
    )

    page.add(layout)
    page.update()

ft.app(target=main)
