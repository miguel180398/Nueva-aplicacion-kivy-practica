from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.button import MDIconButton
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle
import kivy.utils

class Banner(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__()

        with self.canvas.before:
            Color(rgba = (0,.4,0,0.1))
            self.rect = RoundedRectangle(radius = [(40.0,40.0),(40.0,40.0),(40.0,40.0),(40.0,40.0)])
        self.bind(pos = self.update_rect,size =self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
