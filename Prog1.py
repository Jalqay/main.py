from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from kivy.config import Config

Config.set("graphics", "resizable", 0)
Config.set()

class Application(App):


    def click(self, instance):
        self.label.text = "Thanks for press"

    def build(self):

        grid = GridLayout(cols = 1)
        label = Label()
        box_l = BoxLayout()

        my_but = Button(text = "Press ME PLIZ", font_size =30,
                        background_color = "cyan",
                        on_press = self.click)
        my_but2 = Button(text = "DONT PRESS", font_size =30,
                        background_color = "cyan")

        self.label = Label(text = "TEXT", font_size = 50)

        box_l.add_widget(my_but)
        box_l.add_widget( my_but2)

        grid.add_widget(box_l)
        grid.add_widget(self.label)

        return grid


if __name__ == "__main__":
    Application().run()