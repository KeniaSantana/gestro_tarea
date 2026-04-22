import flet as ft
from controllers.UserController import AuthController
from controllers.TareasController import TareaController
from views.LoginView import LoginView
from views.dashboard import DashboardView

#uv sync
def start(page: ft.Page):
    page.title="Sistema de inicio de sesion"
    page.window_width = 450
    page.window_height = 700
    
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(e):
        page.views.clear()
        
        # caso 1: login
        if page.route == "/":
            page.views.append(LoginView(page, task_ctrl))
            
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
        
        #caso de seguridad    
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error: Ruta no encontrada o vista vacia")])
            )
            
        page.update()
        
        
    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.view[-1]
            page.go(top_view.route)
    
    #1. asignar los manejadores de evento primero
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    #2. IMPORTANTE, no fuerces page.route = ""
    print("Iniciando navegacion....")
    if page.route=="/":
        route_change(None)
    else:
        page.go("/")

def main():
    #ejecucion de la app
    ft.app(target=start)
    
if __name__ == "__main__":
    main()