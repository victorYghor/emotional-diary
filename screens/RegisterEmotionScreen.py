from datetime import datetime

from kivy.app import App
from kivy.graphics import Canvas, Color
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from colors import white_text, black_text, green_confirm, red_delete
from util.hex_to_float_rgb import hex_to_float_rgb
import sqlite3

class RegisterEmotionScreen(Screen):
    def save_emotion(self, instance):
        # Obter valores dos inputs
        emotion = self.emotion_input.text
        description = self.description_input.text
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Salvar no banco de dados
        conn = sqlite3.connect('emotions.db')
        c = conn.cursor()
        c.execute("INSERT INTO emotions (emotion, description, date) VALUES (?, ?, ?)",
                  (emotion, description, current_date))
        conn.commit()
        conn.close()

        # Limpar os campos após salvar
        self.emotion_input.text = ''
        self.description_input.text = ''

    def delete_emotion(self, instance):
        emotion = self.emotion_input.text
        conn = sqlite3.connect('emotions.db')
        c = conn.cursor()

        # Verificar se o sentimento existe no banco
        c.execute("SELECT * FROM emotions WHERE emotion=?", (emotion,))
        result = c.fetchone()

        if result:
            # Excluir do banco de dados
            c.execute("DELETE FROM emotions WHERE emotion=?", (emotion,))
            conn.commit()
            print(f'Sentimento "{emotion}" excluído.')
        else:
            print(f'Sentimento "{emotion}" não existe no banco de dados.')

        conn.close()

        # Limpar campos e navegar para a tela 'see_emotion'
        self.emotion_input.text = ''
        self.description_input.text = ''
        self.manager.current = 'see_emotion'

    def on_focus_emotion_textInput(self, instance, value):
        self.emotion_input.text = ''


    def on_focus(self, instance, value):
        if value:
            print('User focused', instance)
        else:
            print('User defocused', instance)


    # Layout principal (vertical)
    main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

    # Linha superior (rótulo + entrada para emoção + botões)
    top_label_layout = BoxLayout(orientation='vertical', size_hint_y=0.1, padding=10, spacing=10)
    top_button_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, spacing=34)

    # Rótulo para emoção
    lbl_emotion = Label(text='Sentimento:', size_hint_x=0.2, color=white_text)
    background_top_label = Canvas().add(Color())
    top_label_layout.add_widget(lbl_emotion)

    # Campo de texto para emoção
    emotion_input = TextInput(text='', size_hint_x=0.4,
                                   multiline=False, focus=on_focus_emotion_textInput)

    top_button_layout.add_widget(emotion_input)

    # Botão "Salvar"
    btn_save = Button(text='Salvar', size_hint_x=0.2, background_normal='', color=hex_to_float_rgb(black_text),
                      background_color=hex_to_float_rgb(green_confirm))
    btn_save.bind(on_press=self.save_emotion)
    top_button_layout.add_widget(btn_save)

    # Botão "Excluir"
    btn_delete = Button(text='Excluir', size_hint_x=0.2, background_color=hex_to_float_rgb(red_delete),
                        color=hex_to_float_rgb(black_text),
                        background_normal='')
    btn_delete.bind(on_press=delete_emotion)
    top_button_layout.add_widget(btn_delete)

    # Adiciona a linha superior ao main_layout principal
    main_layout.add_widget(top_label_layout)
    main_layout.add_widget(top_button_layout)
    label_description = Label(text='Detalhe mais sobre como esta se sentindo:', size_hint_y=0.1,
                                   color=white_text)
    main_layout.add_widget(label_description)

    # Caixa de texto para descrição adicional
    description_input = TextInput(
        text='',
        size_hint_y=0.7,
        multiline=True
    )
    main_layout.add_widget(description_input)

    def __init__(self, **kwargs):
        super(RegisterEmotionScreen, self).__init__(**kwargs)

        self.add_widget(self.main_layout)

