import flet as ft

def main(page: ft.Page):

    page.title = "QR-Generator"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = ft.padding.all(10)
    page.window.height = 500
    page.window.width = 600
    page.window.max_width = 600

    page.update()

    content_string = ft.TextField(label="Conteudo do QRCode", width=600)
    file_name = ft.TextField(label="Nome do novo arquivo", width=400)
    generate_btn = ft.ElevatedButton(
        text="Gerar QRCode",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        width=150
    )

    gen_row = ft.Row(
        controls=[
            file_name,
            generate_btn
        ]
    )

    page.add(
        content_string,
        gen_row
    )


ft.app(target=main)
