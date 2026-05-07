import flet as ft

def RegistroView(page: ft.Page, auth_controller):

    nombre_input = ft.TextField(
        label="Nombre",
        width=350,
        border_radius=10
    )

    apellido_input = ft.TextField(
        label="Apellido",
        width=350,
        border_radius=10
    )

    email_input = ft.TextField(
        label="Correo Electrónico",
        width=350,
        border_radius=10
    )

    telefono_input = ft.TextField(
        label="Teléfono",
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

    def registrarse_click(e):

        print("BOTON PRESIONADO")

        try:


            if (
                not nombre_input.value or
                not apellido_input.value or
                not email_input.value or
                not telefono_input.value or
                not pass_input.value
            ):

                print("FALTAN CAMPOS")

                page.snack_bar = ft.SnackBar(
                    ft.Text("Por favor, llene todos los campos")
                )

                page.snack_bar.open = True
                page.update()

                return

            nombre = nombre_input.value
            apellido = apellido_input.value
            email = email_input.value
            telefono = telefono_input.value
            password = pass_input.value

            print(
                nombre,
                apellido,
                email,
                telefono
            )


            success, msg = auth_controller.registrar_usuario(
                nombre,
                apellido,
                email,
                password,
                telefono
            )

            print("RESULTADO:", success, msg)


            if success:

                print("USUARIO REGISTRADO")

                page.snack_bar = ft.SnackBar(
                    ft.Text(msg)
                )

                page.snack_bar.open = True
                page.update()


                page.go("/")

            else:

                print("NO SE REGISTRO")

                page.snack_bar = ft.SnackBar(
                    ft.Text(msg)
                )

                page.snack_bar.open = True
                page.update()

        except Exception as ex:

            print("ERROR REAL:", ex)

            page.snack_bar = ft.SnackBar(
                ft.Text(f"Error: {ex}")
            )

            page.snack_bar.open = True
            page.update()

    registrarse_button = ft.ElevatedButton(
        "Crear cuenta",
        on_click=registrarse_click,
        width=350,
        bgcolor="#F7ADC4",
        color="black"
    )

    volver_button = ft.ElevatedButton(
        "¿Ya tienes una cuenta?",
        on_click=lambda _: page.go("/"),
        width=350,
        bgcolor="#CAA1F8",
        color="black"
    )

    pass_input.on_submit = registrarse_click

    return ft.View(
        route="/registrarse",

        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        appbar=ft.AppBar(
            title=ft.Text("Registro"),
            bgcolor="#CAA1F8"
        ),

        controls=[

            ft.Column(

                [

                    ft.Text(
                        "Crear cuenta",
                        size=25,
                        weight="bold"
                    ),

                    nombre_input,
                    apellido_input,
                    email_input,
                    telefono_input,
                    pass_input,

                    registrarse_button,
                    volver_button

                ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20

            )

        ]
    )
