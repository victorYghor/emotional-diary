from datetime import datetime

from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from colors import white_text, green_confirm, red_delete, black_text
from util.hex_to_float_rgb import hex_to_float_rgb


class EmotionBox(BoxLayout):
    def __init__(self, emotion, description, date_time, on_edit, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = 200
        self.orientation = 'horizontal'
        self.padding = [32, 120, 32, 0]  # [left, top, right, bottom]
        self.spacing = 20


        # Emotion Label (left)
        emotion_label = Label(text=emotion, size_hint_x=0.2, color=hex_to_float_rgb(white_text), halign='center', valign='middle')
        emotion_label.bind(size=emotion_label.setter('text_size'))

        box_description = BoxLayout(orientation='vertical', size_hint_x = 0.8)
        # Description Label (right)
        desc_label = Label(text=description, size_hint_x=0.6, color=hex_to_float_rgb(white_text), halign='left', valign='middle')
        desc_label.bind(size=desc_label.setter('text_size'))
        # Date and Time Label (below description)
        date_label = Label(text=date_time, size_hint_x=0.2, color=hex_to_float_rgb(white_text), halign='right', valign='middle')
        date_label.bind(size=date_label.setter('text_size'))

        box_description.add_widget(desc_label)
        box_description.add_widget(date_label)

        edit_btn = Button(text='Editar', size_hint_x=0.2, background_color=hex_to_float_rgb(green_confirm),
                        color=hex_to_float_rgb(black_text))
        edit_btn.bind(on_press=on_edit)
        # Adding to layout
        self.add_widget(emotion_label)
        self.add_widget(box_description)
        self.add_widget(edit_btn)



class EmotionsScreen(Screen):
    def on_edit(self, instance):
        print('funciona')

    def __init__(self, **kwargs):
        super(EmotionsScreen, self).__init__(**kwargs)
        # ScrollView
        scroll_view = ScrollView()

        # Layout principal
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint_y=None)
        main_layout.bind(minimum_height=main_layout.setter('height'))  # Ajustar a altura com base no conteúdo


        # Adicionar o layout principal ao ScrollView
        scroll_view.add_widget(main_layout)
        self.add_widget(scroll_view)