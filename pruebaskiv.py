from kivy.lang import Builder
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
import matplotlib.pyplot as plt

KV = '''
MDScreen:
    orientation: "vertical"

    MDToolbar:
        title: "MDToolbar"
        left_action_items: [["menu", lambda x: app.callback(x)]]

    MDRaisedButton:
        id: button
        text: "PRESS ME"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: app.menu.open()
    
    FloatLayout:
        MyFigure:
            pos: (400, 20)
            size: (300, 200)
            size_hint: (None, None)
    
'''

plt.plot([1, 23, 2, 4,7,8,4434,5])
plt.ylabel('some numbers')

class MyFigure(FigureCanvasKivyAgg):
    def __init__(self, **kwargs):
        super().__init__(plt.gcf(), **kwargs)

class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                "text": f"Item {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.button,
            items=menu_items,
            width_mult=4,
        )

    def menu_callback(self, text_item):
        print(text_item)

    def build(self):
        return self.screen


Test().run()