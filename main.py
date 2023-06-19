from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Line
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
# 784(28,28)  800,600->

class DrawingWidget(Widget):
    def on_touch_down(self, touch):
        x, y = touch.pos
        print(f"Clicked at ({x}, {y})")
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(0, 0, 0, 1)  # 黒色で描画
                touch.ud["line"] = Line(points=(touch.x, touch.y), width=20)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            touch.ud["line"].points += (touch.x, touch.y)

    def capture_image(self,filename):
        filename = filename + ".png"
        self.export_to_png(filename)

class SavePopup(Popup):
    def __init__(self, main_layout):
        self.main_layout = main_layout
        super(SavePopup, self).__init__()

    def save(self):
        filename = self.ids.filename_input.text
        if filename:
            self.main_layout.ids.drawing_widget.capture_image(filename)
            self.dismiss()
        else:
            popup = Popup(title='Error', content=Label(text='Please enter a filename.'), size_hint=(None, None),
                          size=(200, 150))
            popup.open()

class MainLayout(ButtonBehavior, BoxLayout):
    def save_image(self):
        save_popup = SavePopup(self)
        save_popup.open()

    def clear_canvas(self):
        self.ids.drawing_widget.canvas.clear()

    def show_window_size(self):
        if self.ids.check_button.text == 'check':
            popup = Popup(title='window size', content=Label(text=str(Window.size)), size_hint=(None, None),
                            size=(200, 150))
            popup.open()
            self.ids.check_button.text = str(Window.size)
        else:
            self.ids.check_button.text = 'check'

class HandwritingApp(App):   
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    HandwritingApp().run()