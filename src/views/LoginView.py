import flet as ft
USUARIO_VALIDO="admin"
CONTRASEñA_VALIDA = "123456"

def LoginView(page: ft.Page, auth_controller):
    email_input = ft.TextField(label="Correo Electronico", width = 350, border_radius=10)
    pass_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=350, border_radius=10)
    
    def login_click(e):
        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, llene todos los campos"))
            page.snack_bar.open = True
            page.update()
        usuario = email_input.value
        contrasena = pass_input.value
        
        if usuario == USUARIO_VALIDO and contrasena == CONTRASEñA_VALIDA:
            page.show_dialog(ft.SnackBar(ft.Text("Inicio de sesion exitoso.")))
            page.go("/dashboard")
        else:
            page.show_dialog(ft.SnackBar(ft.Text("Usuario o contraseña erronea.")))
            return

        user, msg = auth_controller.login(email_input.value, pass_input.value)
        
        if user:
            page.session.set("user", user)
            page.go("/dashboard")
        else: 
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            page.update()
            
    login_button = ft.ElevatedButton("Entrar", on_click=login_click, width=350, bgcolor="cyan", color = "white")
    registrar = ft.ElevatedButton("Crear una nueva cuenta", bgcolor="cyan", color = "white", width=350, on_click=lambda _: page.go("/registro"))
    pass_input.on_submit = login_click
        
    
    return ft.View(
        route = "/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(title=ft.Text("Bienvenido"), bgcolor="bluegrey900", color= "white"),
        controls=[
            ft.Column(
                [
                    ft.Text("Acceso al sistema", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    login_button,
                    registrar,
                    ft.TextButton("¿Olvidaste la contraseña?", on_click=lambda _: page.go("/registro"))
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=20
            )
        ]
    )