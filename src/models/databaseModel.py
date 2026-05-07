import mysql.connector

class Database:
    @staticmethod
    def get_connection():
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="gestor_tarea",
                port=3306
            )

            print("Conexión a la BD exitosa")
            return conn

        except mysql.connector.Error as err:
            print("Error de conexión a MySQL:", err)
            raise
