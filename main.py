import flet as ft
import time

def main(page: ft.Page):
    page.title = "App Nicolle"
    page.theme_mode = "dark"
    page.bgcolor = "#121212"
    page.padding = 0

    def mostrar_transicao():
        page.add(ft.Container(
            content=ft.Column([
                ft.Text("Bem-vindo(a)!", size=24, color="pink"),
                ft.Text("De: Nicolle para: Jessica", size=18, color="white")
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            alignment=ft.alignment.center, expand=True
        ))
        page.update()
        time.sleep(2)
        carregar_home()

    def carregar_home():
        page.clean()
        
        header = ft.Row([ft.Text("ONLINE", size=10, color="green"), ft.Icon(ft.icons.CIRCLE, color="green", size=8)], alignment="end", padding=15)
        
        # O Flet busca os arquivos na pasta 'assets' automaticamente
        gato = ft.Image(src="gato.png", width=180, error_content=ft.Text("Gato sumiu!"))
        
        def criar_btn(img_nome):
            return ft.Container(
                content=ft.Image(src=img_nome, width=120),
                bgcolor="#202020", border_radius=15, width=150, height=150, alignment=ft.alignment.center
            )

        layout = ft.Column([
            header,
            gato,
            ft.Row([criar_btn("galeria.png"), criar_btn("cartas.png")], alignment="center", spacing=10),
            ft.Row([criar_btn("controle.png"), criar_btn("engrenagem.png")], alignment="center", spacing=10)
        ], horizontal_alignment="center")
        
        page.add(layout)
        page.update()

    mostrar_transicao()

ft.app(target=main, assets_dir="assets")
