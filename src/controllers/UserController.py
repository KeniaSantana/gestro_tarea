from models.UserModel import UsuarioModel
from models.schemasModel import UsuarioSchema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        
    def registrar_usuario(self, nombre, apellido, email, password):
        try:
            nuevo_usuario = UsuarioSchema(
                nombre=nombre,
                apellido=apellido,
                email=email,
                password=password
            )
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            return False, e.errors()[0]['msg']

    def login(self, email, password):
        user = self.model.validar_login(email, password)

        if user:
            return user, "Inicio correcto"
        else:
            return None, "Credenciales incorrectas"
