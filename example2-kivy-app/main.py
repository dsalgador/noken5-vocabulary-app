from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import pandas as pd
import random

Builder.load_file('design.kv')


class MyWidget(BoxLayout):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.vocab = pd.read_csv("database/vocabularydb.csv", encoding='utf-8')
        print(self.vocab.head())
        self.current_index = None

    def showquestion(self):
        self.ids['label2'].text = ""
        self.current_index = random.choice(self.vocab.index)

        filetext = self.vocab.english[self.current_index]
        self.ids['label1'].text = filetext

    def showanswer(self):
        filetext = self.vocab.kanji[self.current_index]
        self.ids['label2'].text = filetext


class myApp(App):
    """

    """
    def build(self):
        return MyWidget()

    def on_pause(self):
        return True

    def on_resume(self):
        pass


if __name__ in ('__main__', '__android__'):
    myApp().run()