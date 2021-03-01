from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

from baseclass.dashboard import DashBoard
from baseclass.settingsscreen import SettingsScreen



class MyApp(MDApp):
    def build(self):
        self.title = "Mi Primera App"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file("main.kv")


MyApp().run()

