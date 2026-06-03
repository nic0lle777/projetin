import flet as ft

def main(page: ft.Page):
    page.title = "App Nicolle"
    page.theme_mode = "dark"
    page.fonts = {"Pixel": "https://fonts.gstatic.com/s/pressstart2p/v14/e3t4euO8T-267oIAQAu6jDQyK0n8-2xTh-o.woff2"}
    page.theme = ft.Theme(font_family="Pixel")
    page.horizontal_alignment = "center"

    # --- FUNÇÕES DAS TELAS ---

    def ir_para_jogos(e):
        page.clean()
        page.add(
            ft.Text("JOGOS", size=20),
            ft.ListView([ft.ListTile(title=ft.Text(f"Jogo {i}")) for i in range(1, 4)], expand=True),
            ft.ElevatedButton("Voltar", on_click=carregar_home)
        )

    def ir_para_album(e):
        page.clean()
        grid = ft.GridView(expand=True, max_extent=150, spacing=10)
        for _ in range(4): # 4 espaços vazios
            grid.controls.append(ft.Container(bgcolor="#333333", border_radius=10, height=150))
        page.add(ft.Text("ALBUM"), grid, ft.ElevatedButton("Voltar", on_click=carregar_home))

    def ir_para_config(e):
        page.clean()
        page.add(
            ft.Text("CONFIG"),
            ft.TextField(label="Nome de usuário"),
            ft.Switch(label="Modo Noturno", value=True),
            ft.Text("Versão 1.0"),
            ft.Text("Criado por Nicolle"),
            ft.ElevatedButton("Voltar", on_click=carregar_home)
        )

    # --- TELA HOME (PRINCIPAL) ---

    def carregar_home(e):
        page.clean()
        
        # Botões
        def b(img, txt, acao):
            return ft.Container(
                content=ft.Row([ft.Image(src=img, width=30), ft.Text(txt, size=10)]),
                bgcolor="#333333", padding=15, border_radius=20, width=140, height=70, on_click=acao
            )

        conteudo = ft.Stack([
            ft.Column([
                ft.Container(height=100), # Espaço para o Gato
                ft.Row([b("galeria.png", "FOTOS", ir_para_album), b("cartas.png", "CARTAS", None)], alignment="center", spacing=10),
                ft.Row([b("controle.png", "JOGOS", ir_para_jogos), b("engrenagem.png", "CONFIG", ir_para_config)], alignment="center", spacing=10)
            ], horizontal_alignment="center"),
            ft.Image(src="gato.png", width=100, top=0, left=130) # Gato posicionado
        ])
        page.add(conteudo)

    carregar_home(None)

ft.app(target=main, assets_dir="assets")
