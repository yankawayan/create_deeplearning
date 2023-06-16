from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget

Builder.load_file('main.kv')

class DrawingWidget(Widget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if touch.button == 'left':
                with self.canvas:
                    Color(1, 0, 0, 1)
                    touch.ud["line"] = Line(points=(touch.x, touch.y), width=50)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            if touch.button == 'left':
                touch.ud["line"].points += (touch.x, touch.y)

class HomeWidget(BoxLayout):
    def button_clicked(self):
        print("Window Size", Window.size)

class FirstApp(App):
    def build(self):
        return HomeWidget()

if __name__ == '__main__':
    FirstApp().run()