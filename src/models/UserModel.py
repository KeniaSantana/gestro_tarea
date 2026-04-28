import bcrypt
from .databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()
        
    def registrar(self, usuario_data):
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)
        
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                # 🔥 tabla correcta: usuarios
                "INSERT INTO usuarios (nombre, apellido, email, password) VALUES (%s, %s, %s, %s)",
                (
                    usuario_data.nombre,
                    usuario_data.apellido,   # 🔥 agregado
                    usuario_data.email,
                    hashed_pw.decode('utf-8')
                )
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al registrar: {e}")
            return False
        finally:
            conn.close()
        
    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)

        # 🔥 tabla correcta + parámetro correcto
        cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            print("Usuario encontrado:", user)

            if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
                return user
            else:
                print("Contraseña incorrecta")
        
        else:
            print("Usuario no existe")

        return None
