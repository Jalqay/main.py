from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton

KV = '''
MDScreen:

    BoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "Экономика сабағы"
            md_bg_color: .35,.11,.40,1
            elevation: 20
            
            
            
        MDLabel:
            

        MDRaisedButton:
            text: "Уроки"
            md_bg_color: "red"
            md_bg_color: .24,.22,.40, 1
            pos_hint: {"center_x": .5, "center_y": .9}
            elevation: 20
            font_size: "30sp"
            
        MDLabel:
            
        MDRaisedButton:
            text: "Тесты"
            md_bg_color: .24,.22,.40, 1
            pos_hint: {"center_x": .5, "center_y": .9}
            elevation: 20
            font_size: "30sp"
        
        MDLabel:
        MDLabel:
        
'''


class Test(MDApp):
    def build(self):
        screen = Builder.load_string(KV)

        return screen



Test().run()