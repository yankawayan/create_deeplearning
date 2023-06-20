from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Line
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
import io
from PIL import Image
import numpy as np
import os
from my_net import hand_write_img_to_num

from function import arr_to_img_and_show

class DrawingWidget(Widget):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            with self.canvas:
                Color(1, 1, 1, 1)
                touch.ud["line"] = Line(points=(touch.x, touch.y), width=20)

    def on_touch_move(self, touch):
        if self.collide_point(*touch.pos):
            touch.ud["line"].points += (touch.x, touch.y)

    #要改善(機能を分ける)
    def capture_image(self,filename):
        filename = filename + ".png"
        self.export_to_png(filename)
        with open(filename, 'rb') as f:
            png_data = f.read()
        os.remove(filename)
        image = Image.open(io.BytesIO(png_data))
        resized_image = image.resize((28, 28))
        #grayscale_image = resized_image.convert("L")

        threshold = 128  # しきい値の設定
        bw_image = resized_image.convert("L").point(lambda x: 255 if x >= threshold else 0, mode="1")
        
        pixel_list = list(bw_image.getdata())
        img_arr = np.array(pixel_list)
        num = hand_write_img_to_num(img_arr)

        #arr_to_img_and_show(img_arr,28,28)

        popup = Popup(title='your write num', content=Label(text=str(num)), size_hint=(None, None),
                          size=(200, 150))
        popup.open()


class SavePopup(Popup):
    def __init__(self, main_layout):
        self.main_layout = main_layout
        super(SavePopup, self).__init__()

    def save(self):
        filename = self.ids.filename_input.text
        self.main_layout.ids.drawing_widget.capture_image(filename)
        self.dismiss()
        # if filename:
        #     self.main_layout.ids.drawing_widget.capture_image(filename)
        #     self.dismiss()
        # else:
        #     popup = Popup(title='Error', content=Label(text='Please enter a filename.'), size_hint=(None, None),
        #                   size=(200, 150))
        #     popup.open()

class MainLayout(ButtonBehavior, BoxLayout):
    def save_image(self):
        pass
        #self.ids.drawing_widget.capture_image("test")
        # save_popup = SavePopup(self)
        # save_popup.open()

    def clear_canvas(self):
        self.ids.drawing_widget.canvas.clear()

    def check_img_to_num(self):
        self.ids.drawing_widget.capture_image("test")

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