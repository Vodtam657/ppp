from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ScrButton(Button):
    def __init__(self, screen, direction="right", goal="main", **kwargs):
        super()__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class app(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        q1 = Layout(text, "Надпис")
        box_button = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)
        box_button.add_widget(ScrButton(self, direction= "",goal="first", text = 1))
        box_button.add_widget(ScrButton(self, direction="", goal="first", text=2))
        box_button.add_widget(ScrButton(self, direction="", goal="first", text=3))
        box_button.add_widget(ScrButton(self, direction="", goal="first", text=4))


app = App
app.run