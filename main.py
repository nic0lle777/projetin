import flet as ft
import time

def main(page: ft.Page):
    page.title = "App Nicolle"
    page.theme_mode = "dark"
    page.bgcolor = "#121212"
    page.padding = 0

    # --- TELA DE TRANSIÇÃO (Abertura Fofa) ---
    def mostrar_transicao():
        container = ft.Container(
            content=ft.Column([
                ft.Text("Bem-vindo(a)!", size=20, color="pink"),
                ft.Text("De: Nicolle para: Jessica", size=15, color="white")
            ], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor="#121212",
            alignment=ft.alignment.center,
            expand=True
        )
        page.add(container)
        page.update()
        time.sleep(2) # Segura a mensagem por 2 segundos
        carregar_home()

    # --- TELA HOME (Com todas as funções) ---
    def carregar_home():
        page.clean()
        
        header = ft.Row([ft.Text("ONLINE", size=10), ft.Icon(ft.icons.CIRCLE, color="green", size=8)], alignment="end", padding=15)
        
        # Botões funcionais
        def criar_btn(texto, icone, destino):
            return ft.Container(
                content=ft.Column([ft.Icon(icone, size=40), ft.Text(texto, size=10)], alignment="center"),
                bgcolor="#202020", border_radius=15, width=150, height=150,
                on_click=destino
            )

        layout = ft.Column([
            header,
            ft.Image(src="gato.png", width=180),
            ft.Row([
                criar_btn("FOTOS", ft.icons.PHOTO, lambda e: print("Abrir fotos")), 
                criar_btn("CARTAS", ft.icons.MAIL, lambda e: print("Abrir cartas"))
            ], alignment="center", spacing=10),
            ft.Row([
                criar_btn("JOGOS", ft.icons.GAMEPAD, lambda e: print("Abrir jogos")), 
                criar_btn("CONFIG", ft.icons.SETTINGS, lambda e: print("Abrir config"))
            ], alignment="center", spacing=10)
        ], horizontal_alignment="center")
        
        page.add(layout)
        page.update()

    # Inicia o app pela transição
    mostrar_transicao()

ft.app(target=main, assets_dir="assets")
