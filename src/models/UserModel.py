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

            # Verificar si el usuario ya existe
            cursor.execute("SELECT id_usuario FROM usuario WHERE email=%s", (usuario_data.email,))
            if cursor.fetchone():
                return False

            # Encriptar contraseña
            salt = bcrypt.gensalt()
            hashed_pw = bcrypt.hashpw(usuario_data.password.encode('utf-8'), salt)

            # Insertar usuario
            cursor = conn.cursor()  # cursor normal para insertar
            cursor.execute(
                """INSERT INTO usuario 
                (nombre, apellido, email, contraseña, telefono, fecha_registro) 
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (
                    usuario_data.nombre,
                    usuario_data.apellido,
                    usuario_data.email,
                    hashed_pw.decode('utf-8'),
                    usuario_data.telefono,
                    usuario_data.fecha
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

            cursor.execute("SELECT * FROM usuario WHERE email=%s", (email,))
            user = cursor.fetchone()

            if not user:
                print("Usuario no existe")
                return None

            # Verificar contraseña
            if bcrypt.checkpw(password.encode('utf-8'), user['contraseña'].encode('utf-8')):

                # Actualizar último ingreso
                update_cursor = conn.cursor()
                update_cursor.execute(
                    "UPDATE usuario SET ultimo_ingreso = NOW() WHERE id_usuario = %s",
                    (user["id_usuario"],)
                )
                conn.commit()
                update_cursor.close()

                return user
            else:
                print("Contraseña incorrecta")
                return None

        except Exception as err:
            print(f"Error en login: {err}")
            return False

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
