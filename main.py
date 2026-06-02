import flet as ft

def main(page: ft.Page):
    page.title = "App Customizado"
    page.theme_mode = "dark"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 20

    # Criando os botões com as imagens que você enviou
    def criar_botao(nome_imagem, texto):
        return ft.Column(
            [
                ft.Image(src=nome_imagem, width=100, height=100),
                ft.Text(texto, color="white", weight="bold")
            ],
            alignment="center",
            horizontal_alignment="center"
        )

    # Exibindo suas imagens como botões
    # O Flet buscará exatamente esses arquivos na pasta assets
    botoes = ft.Row(
        [
            criar_botao("gato.png", "Home"),
            criar_botao("galeria.png", "Fotos"),
            criar_botao("cartas.png", "Jogos"),
            criar_botao("engrenagem.png", "Config"),
        ],
        alignment="center",
        wrap=True
    )

    page.add(botoes)

ft.app(target=main, assets_dir="assets")
