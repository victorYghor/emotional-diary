from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

Builder.load_string("""
<CustomRoot>:
    canvas:
        Color:
            rgba: root.background_color
        Rectangle:
            pos: self.pos
            size: self.size
            """)


class CustomRoot(BoxLayout):
    background_color = ColorProperty()  # The ListProperty will also work.


class MyApp(App):

    def build(self):
        self.layout = CustomRoot(background_color=(0.5, 0, 0.1, 1))
        textInput_box = BoxLayout(orientation='vertical', padding=10, spacing=100)
        description_input = TextInput(
            text='',
            size_hint_y=0.7,
            multiline=True
        )
        textInput_box.add_widget(description_input)
        self.layout.add_widget(textInput_box)
        return self.layout


MyApp().run()
