import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line


class Touch(Widget):

    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 5)
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))

    def on_touch_down(self, touch):
        print("Mouse Down")
        self.rect.pos = touch.pos

    def on_touch_move(self,touch):
        print("Mouse Move", touch)


    def on_touch_up(self, touch):
        print("Mouse Up", touch)

class MyApp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    MyApp().run()
