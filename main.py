from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

Builder.load_file('layout.kv')

class MyWidget(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return MyWidget()
        
if __name__ == '__main__':
    MyApp().run()