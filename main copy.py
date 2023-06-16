from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line

Builder.load_file('layout.kv')

class DrawingWidget(Widget):
    def on_touch_down(self, touch):
        if touch.button == 'left':
            with self.canvas:
                touch.ud["line"] = Line(points=(touch.x, touch.y), width=50)

    def on_touch_move(self, touch):
        if touch.button == 'left':
            touch.ud["line"].points += (touch.x, touch.y)

class MyApp(App):
    def build(self):
        # レイアウトの作成
        layout = BoxLayout(orientation='vertical')

        # ヘッダーの作成
        header_label = Label(text='Header', size_hint=(1, 0.1))
        layout.add_widget(header_label)

        # # テキスト領域の作成
        # text_input = TextInput()
        # layout.add_widget(text_input)

        draw_window = DrawingWidget()
        layout.add_widget(draw_window)

        # ボタン1の作成
        button1 = Button(text='Button 1')
        layout.add_widget(button1)

        # ボタン2の作成
        button2 = Button(text='Button 2')
        layout.add_widget(button2)

        # フッターの作成
        footer_label = Label(text='Footer', size_hint=(1, 0.1))
        layout.add_widget(footer_label)

        return layout


if __name__ == '__main__':
    MyApp().run()