from models.TareaModel import TareaModel

class TareaController:
    def __init__(self):
        self.model = TareaModel
            
    def obtener_lista(self, id_usuario):
        return self.model.listar_por_usuario(id_usuario)
    
    def guardas_nueva(Self, id_usuario, titulo, desc, prio, clas):
        if not titulo:
            return False, "El titulo es obligatorio"
        
        self.model.crear(id_usuario, titulo, desc, prio, clas)
        return True, "Tarea guardada"