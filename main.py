import flet as ft

def main(page: ft.Page):
    # Configurações de layout da página (100% seguras contra quebra de versão)
    page.title = "App Customizado"
    page.theme_mode = "dark"          # Deixa o fundo escuro moderno
    page.horizontal_alignment = "center" # Centraliza na horizontal
    page.vertical_alignment = "center"   # Centraliza na vertical
    page.padding = 20

    # Elemento da Imagem
    imagem_principal = ft.Image(
        src="imagem.png",             # Procura por assets/imagem.png
        width=300,
        height=300,
        fit="contain",
        border_radius=20              # Simplificado e funcional
    )

    # Elemento de Texto
    texto_principal = ft.Text(
        "Coloque sua mensagem aqui!",
        size=24,
        weight="bold",
        color="white"
    )

    # Adiciona os elementos de forma sequencial na tela
    page.add(imagem_principal, texto_principal)

# Executa o app indicando a pasta de arquivos estáticos
ft.app(target=main, assets_dir="assets")
