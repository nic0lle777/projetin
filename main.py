import flet as ft

def main(page: ft.Page):
    # 1. Configurações explícitas em strings (evita bugs de enumeração no Android)
    page.title = "App para Namorada"
    page.theme_mode = "light"
    page.padding = 20
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 2. Proteção contra falta de imagem (Se o GitHub não empacotar a foto, o app abre mesmo assim)
    imagem = ft.Image(
        src="gato.png", 
        width=300, 
        height=300, 
        fit=ft.ImageFit.CONTAIN,
        error_content=ft.Container(
            content=ft.Text("Foto não encontrada.\nVerifique a pasta assets!", color="red", text_align="center"),
            alignment=ft.alignment.center
        )
    )

    texto = ft.Text(
        "Texto personalizado aqui!",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.PINK,
        text_align=ft.TextAlign.CENTER
    )

    # 3. Organização estruturada em Column
    layout = ft.Column(
        controls=[imagem, ft.VerticalDivider(height=20), texto],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(layout)
    
    # 4. Gatilho de renderização obrigatório para Android
    page.update()

# 5. Isolamento de escopo para o compilador do GitHub Actions buildar sem travar
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
