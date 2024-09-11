import sqlite3

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.EmotionsScreen import EmotionsScreen
from screens.RegisterEmotionScreen import RegisterEmotionScreen  # Assuming RegisterScreen is in RegisterEmotionScreen.py


# Definir a conexão com o banco de dados
conn = sqlite3.connect('emotions.db')
c = conn.cursor()

# Criar tabela no banco de dados se não existir
c.execute('''CREATE TABLE IF NOT EXISTS emotions 
             (id INTEGER PRIMARY KEY, emotion TEXT, description TEXT, date TEXT)''')
conn.commit()

class EmotionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegisterEmotionScreen(name='register_emotion'))  # Add RegisterScreen to ScreenManager
        sm.add_widget(EmotionsScreen(name='see_emotions'))
        sm.current = 'register_emotion'  # Set the initial screen to 'emotion'
        return sm

if __name__ == '__main__':
    EmotionApp().run()

