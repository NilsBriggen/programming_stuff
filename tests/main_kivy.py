import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class Touch(Widget):
    def on_touch_down(self, touch):
        print("working", touch)
        return super().on_touch_down(touch)

class MyApp(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    MyApp().run()