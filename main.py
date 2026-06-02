import flet as ft

def main(page: ft.Page):
    page.theme_mode = "dark"
    page.fonts = {"Pixel": "https://fonts.gstatic.com/s/pressstart2p/v14/e3t4euO8T-267oIAQAu6jDQyK0n8-2xTh-o.woff2"}
    page.theme = ft.Theme(font_family="Pixel") # Fonte estilo pixel em todo app

    # Conteúdo das telas
    def ir_para_home(e):
        coluna_principal.controls = [img_gato, texto_boas_vindas, row_botoes]
        page.update()

    # Função simplificada dos botões
    def criar_botao(img, texto, acao):
        return ft.GestureDetector(
            content=ft.Column([ft.Image(src=img, width=80), ft.Text(texto, size=10)], horizontal_alignment="center"),
            on_tap=acao
        )

    # Elementos fixos
    img_gato = ft.Image(src="gato.png", width=150)
    texto_boas_vindas = ft.Text("Olá, Amor!", size=20)
    row_botoes = ft.Row([
        criar_botao("galeria.png", "Fotos", None),
        criar_botao("cartas.png", "Cartas", None),
        criar_botao("engrenagem.png", "Config", None)
    ], alignment="center")

    coluna_principal = ft.Column([img_gato, texto_boas_vindas, row_botoes], alignment="center")
    
    page.add(coluna_principal, ft.Text("Criado por: Nicolle | v1.0", size=8, color="grey"))

ft.app(target=main, assets_dir="assets")
