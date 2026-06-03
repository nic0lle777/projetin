import flet as ft

def main(page: ft.Page):
    # Configurações da página
    page.title = "App para Namorada"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    # Carregando uma imagem (coloque a imagem na pasta 'assets')
    imagem = ft.Image(
        src="sua_imagem.png", # Nome da imagem na pasta assets
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
    )

    texto = ft.Text(
        "Texto personalizado aqui!",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.PINK
    )

    # Adicionando os elementos na tela
    page.add(imagem, texto)

ft.app(target=main, assets_dir="assets")
