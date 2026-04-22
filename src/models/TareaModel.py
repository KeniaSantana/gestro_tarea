from .databaseModel import Database

class TareaModel:
    def __init__(self):
        self.db=Database()
        
    def listar_por_usuario(self, id_usuario):
        conn = self.deb.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM tareas, WHERE id_usuario = %s ODER BY fecha_limite ASC"
        cursor.execute(query, (id_usuario))
        resultado = cursor.fecthall()
        conn.close()
        return resultado
    
    def crear(self, id_usuario, titulo, descripcion, prioridad, clasificacion):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = """INSERT INTO tareas (id_usuario, titulo, descripcion, prioridad, clasificacion)
                    VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, (id_usuario, titulo, descripcion, prioridad, clasificacion))
        conn.commit()
        conn.close()