from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from baseclass.banner import Banner

class DashBoard(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.sub_title = "Convertidor de Números Binarios"
        self.hint_binary_number = "Ingresar un numero Binario"


    def on_pre_enter(self, *args):
        self.app.title = "Dash Board"


    def on_kiyv_pos(self,base_widget):
        print("Hola")
        
        grid = self.ids["grid_banner"]
        for i in range(6):
            banner = Banner()
            grid.add_widget(banner)

    def is_binary(self,binary_number):
        
        try:
            decimal = int(binary_number, 2)
            self.ids["solution"].text = f"Resultado: {decimal}"
            self.ids["solution"].theme_text_color = "Primary"
        except ValueError:
            self.ids["solution"].text = "Número Incorrecto"
            self.ids["solution"].theme_text_color = "Error"
