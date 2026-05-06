import bcrypt
from models.databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()
    
    def registrar(self, usuario_data):
        conn = None
        cursor = None
        
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)

            # ✔️ tabla correcta: usuarios
            cursor.execute("SELECT id_usuario FROM usuarios WHERE email=%s", (usuario_data.email,))
            if cursor.fetchone():
                return False

            # ✔️ Encriptar contraseña
            hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), bcrypt.gensalt())

            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO usuarios 
                (nombre, apellido, email, password, telefono) 
                VALUES (%s, %s, %s, %s, %s)""",
                (
                    usuario_data.nombre,
                    usuario_data.apellido,
                    usuario_data.email,
                    hashed_pw.decode('utf-8'),
                    usuario_data.telefono
                )
            )

            conn.commit()
            return True

        except Exception as e:
            print(f"Error al registrar: {e}")
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
    def validar_login(self, email, password):
        conn = None
        cursor = None

        try:
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT * FROM usuarios WHERE email=%s", (email,))
            user = cursor.fetchone()

            if not user:
                return None

            # ✔️ campo correcto: password
            if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):

                update_cursor = conn.cursor()
                update_cursor.execute(
                    "UPDATE usuarios SET ultimo_acceso = NOW() WHERE id_usuario = %s",
                    (user["id_usuario"],)
                )
                conn.commit()
                update_cursor.close()

                return user
            else:
                return None

        except Exception as err:
            print(f"Error en login: {err}")
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
