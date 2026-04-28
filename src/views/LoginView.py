import flet as ft

def LoginView(page: ft.Page, auth_controller):
    email_input = ft.TextField(
        label="Correo Electronico",
        width=350,
        border_radius=10
    )

    pass_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        border_radius=10
    )

    def login_click(e):
        print("CLICK LOGIN") 

        if not email_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, llene todos los campos"))
            page.snack_bar.open = True
            page.update()
            return

        usuario = email_input.value
        contrasena = pass_input.value

        try:
            user, msg = auth_controller.login(usuario, contrasena)

            print("RESULTADO:", user, msg)  

            if user:
                print("LOGIN CORRECTO → REDIRIGIENDO")
                page.session.set("user", user)
                page.go("/dashboard")
            else:
                print("LOGIN FALLÓ:", msg)
                page.snack_bar = ft.SnackBar(ft.Text(msg))
                page.snack_bar.open = True

        except Exception as ex:
            print("ERROR:", ex)
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {ex}"))
            page.snack_bar.open = True

        page.update()

    login_button = ft.ElevatedButton(
        "Entrar",
        on_click=login_click,
        width=350,
        bgcolor="#F7ADC4",
        color="black"
    )

    registrar = ft.ElevatedButton(
        "Crear una nueva cuenta",
        bgcolor="#F7ADC4",
        color="black",
        width=350,
        on_click=lambda _: page.go("/registro")
    )

    pass_input.on_submit = login_click

    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("SIGE-Login"),
            bgcolor="#CAA1F8",
            color="black"
        ),
        controls=[
            ft.Column(
                [
                    ft.Text("Acceso al sistema", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    login_button,
                    registrar,
                    ft.TextButton(
                        "¿Olvidaste la contraseña?",
                        on_click=lambda _: page.go("/registro")
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]
    )
