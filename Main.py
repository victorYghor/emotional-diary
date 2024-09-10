from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from colors import green_confirm, red_delete, white_text, black_text, gray_background
from util.hex_to_float_rgb import hex_to_float_rgb


class EmotionApp(App):
    def build(self):
        # Layout principal (vertical)
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Linha superior (rótulo + entrada para emoção + botões)
        top_label_layout = BoxLayout(orientation='vertical', size_hint_y=0.1, padding=10, spacing=10)
        top_button_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=34)

        # Rótulo para emoção
        lbl_emotion = Label(text='Sentimento:', size_hint_x=0.2, color=white_text)
        top_label_layout.add_widget(lbl_emotion)

        # Campo de texto para emoção
        self.emotion_input = TextInput(text='', size_hint_x=0.4,
                                       multiline=False, focus=self.on_focus_emotion_textInput)

        top_button_layout.add_widget(self.emotion_input)

        # Botão "Salvar"
        btn_save = Button(text='Salvar', size_hint_x=0.2, background_normal='', color=hex_to_float_rgb(black_text),
                          background_color=hex_to_float_rgb(green_confirm))
        btn_save.bind(on_press=self.save_emotion)
        top_button_layout.add_widget(btn_save)

        # Botão "Excluir"
        btn_delete = Button(text='Excluir', size_hint_x=0.2, background_color=hex_to_float_rgb(red_delete),
                            color=hex_to_float_rgb(black_text),
                            background_normal='')
        btn_delete.bind(on_press=self.on_focus)
        top_button_layout.add_widget(btn_delete)

        # Adiciona a linha superior ao main_layout principal
        main_layout.add_widget(top_label_layout)
        main_layout.add_widget(top_button_layout)
        self.label_description = Label(text='Detalhe mais sobre como esta se sentindo:', size_hint_y=0.1, color=white_text)
        main_layout.add_widget(self.label_description)

        # Caixa de texto para descrição adicional
        self.description_input = TextInput(
            text='',
            size_hint_y=0.7,
            multiline=True
        )
        main_layout.add_widget(self.description_input)

        return main_layout

    def save_emotion(self, instance):
        print('test')
        self.emotion_input.text = ''

    def on_focus_emotion_textInput(self, instance, value):
        self.emotion_input.text = ''

    def on_focus(self, instance, value):
        if value:
            print('User focused', instance)
        else:
            print('User defocused', instance)

    def delete_emotion(self, instance):
        self.emotion_input.text = ''
        self.description_input.text = ''


if __name__ == '__main__':
    EmotionApp().run()
