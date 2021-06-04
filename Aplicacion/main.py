from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Window.size = (360, 780)

class MyApp(MDApp):
    def build(self):
        self.title = "CorneApp"
        self.theme_cls.primary_palette = "DeepPurple"
        screen = Builder.load_file("main.kv")
        return screen

class MainMenu(Screen):
    pass
class Notes(Screen):
    pass
class ClosedDoor(Screen):
    pass
class Diet(Screen):
    pass
class Gym(Screen):
    pass

MyApp().run()
