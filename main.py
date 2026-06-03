import flet as ft

def main(page: ft.Page):
    page.title = "App Nicolle"
    page.theme_mode = "dark"
    page.bgcolor = "#121212"
    page.padding = 0

    # Tenta carregar a fonte, se falhar, usa a padrão
    try:
        page.fonts = {"Pixel": "https://fonts.gstatic.com/s/pressstart2p/v14/e3t4euO8T-267oIAQAu6jDQyK0n8-2xTh-o.woff2"}
        page.theme = ft.Theme(font_family="Pixel")
    except:
        pass

    def carregar_interface():
        page.clean()
        
        # Header simples
        header = ft.Row([ft.Text("ONLINE", size=10), ft.Icon(ft.icons.CIRCLE, color="green", size=8)], alignment="end", padding=15)
        
        # Botões (usando ícones do Flet primeiro para não depender de arquivos agora)
        def criar_btn(texto, icone):
            return ft.Container(
                content=ft.Column([ft.Icon(icone, size=40), ft.Text(texto, size=10)], alignment="center"),
                bgcolor="#202020", border_radius=15, width=150, height=150
            )

        layout = ft.Column([
            header,
            ft.Image(src="gato.png", width=180, error_content=ft.Text("Gato sumiu!")),
            ft.Row([criar_btn("FOTOS", ft.icons.PHOTO), criar_btn("CARTAS", ft.icons.MAIL)], alignment="center", spacing=10),
            ft.Row([criar_btn("JOGOS", ft.icons.GAMEPAD), criar_btn("CONFIG", ft.icons.SETTINGS)], alignment="center", spacing=10)
        ], horizontal_alignment="center")
        
        page.add(layout)
        page.update()

    carregar_interface()

ft.app(target=main, assets_dir="assets")
