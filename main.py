import flet as ft

def main(page: ft.Page):
    # Recupera preferências salvas
    page.theme_mode = page.client_storage.get("theme") or "dark"
    nome_usuario = page.client_storage.get("user_name") or "Visitante"
    
    # Carrega a fonte apenas se não estiver no ambiente de build do GitHub
    try:
        page.fonts = {"Pixel": "https://fonts.gstatic.com/s/pressstart2p/v14/e3t4euO8T-267oIAQAu6jDQyK0n8-2xTh-o.woff2"}
        page.theme = ft.Theme(font_family="Pixel")
    except:
        pass

    page.padding = 0

    def mudar_tema(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.client_storage.set("theme", page.theme_mode)
        page.update()

    def salvar_nome(e):
        page.client_storage.set("user_name", e.control.value)

    # --- TELAS ---
    def ir_para_album(e):
        page.clean()
        # Galeria fofa que ocupa a tela toda
        page.add(
            ft.Row([ft.IconButton(ft.icons.ARROW_BACK, on_click=carregar_home)]),
            ft.GridView(
                controls=[ft.Image(src=f"foto{i}.png", fit="cover", border_radius=15) for i in range(1, 5)],
                runs_count=2, spacing=5, run_spacing=5, expand=True
            )
        )

    def carregar_home(e=None):
        page.clean()
        # Header "Online"
        header = ft.Row([ft.Text("ONLINE", size=8), ft.Icon(ft.icons.CIRCLE, color="green", size=10)], alignment="end", padding=10)
        
        # Grid de botões proporcionais
        botoes = ft.GridView(
            controls=[
                ft.Container(content=ft.Column([ft.Image("galeria.png", width=50), ft.Text("FOTOS")], alignment="center"), bgcolor="#333333", border_radius=20, on_click=ir_para_album),
                ft.Container(content=ft.Column([ft.Image("cartas.png", width=50), ft.Text("CARTAS")], alignment="center"), bgcolor="#333333", border_radius=20),
                ft.Container(content=ft.Column([ft.Image("controle.png", width=50), ft.Text("JOGOS")], alignment="center"), bgcolor="#333333", border_radius=20),
                ft.Container(content=ft.Column([ft.Image("engrenagem.png", width=50), ft.Text("CONFIG")], alignment="center"), bgcolor="#333333", border_radius=20, on_click=ir_para_config)
            ],
            runs_count=2, max_extent=200, child_aspect_ratio=1.0, padding=20
        )
        
        page.add(header, ft.Image("gato.png", width=200), botoes)

    def ir_para_config(e):
        page.clean()
        page.add(
            ft.Text("CONFIGURAÇÕES"),
            ft.TextField(label="Apelido", value=nome_usuario, on_change=salvar_nome),
            ft.Switch(label="Modo Noturno", value=(page.theme_mode=="dark"), on_change=mudar_tema),
            ft.ElevatedButton("Voltar", on_click=carregar_home)
        )

    carregar_home()

ft.app(target=main, assets_dir="assets")
