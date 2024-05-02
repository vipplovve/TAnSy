import kivy
import math
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

lang = ""

class Password(Screen):
    # BestAspectRatio=1.74
    Window.size = (813, 465)

    def check(self, n, p):
        n = self.ids.name.text
        p = self.ids.passw.text
        if n == '' and p == '':
            self.ids.name.text = ''
            self.ids.passw.text = ''
        else:
            print()
            print('YOU ARE NOT AUTHORISED TO ACCESS THIS PROGRAM! ')
            quit()

    def bye(self):
        quit()


class Menu(Screen):
    pass

class Language(Screen):
    
    def SetLanguage(self, input):
        
        lang = input


class Sentence(Screen):
    
    def clear(self):
        self.ids.sentence.text = ''
        self.ids.analysis.text = ''

    def sentenceAnalysis(self):

        import stanza

        nlp = stanza.Pipeline('en', download_method = None) 
        
        sentence = self.ids.sentence.text

        doc = nlp(sentence) # Run the pipeline on the input text
        
        file = "SentenceAnalysis"

        file += ".txt"

        with open(file, 'w') as AF:
            print(doc, file = AF) # Look at the result

        self.ids.analysis.text = "The Analysis of Entered Sentence Has been Saved!"       


class File(Screen):
    
    def clear(self):

        self.ids.file.text = ''
        self.ids.analysis.text = ''

    def FileAnalysis(self):

        import stanza

        nlp = stanza.Pipeline('en', download_method = None) 
        
        name = self.ids.file.text

        information = ""

        with open(name, 'r') as source:

            information = source.read();

        doc = nlp(information) # Run the pipeline on the input text
        
        file = "FileAnalysis.txt"

        with open(file, 'w') as AF:
            print(doc, file = AF) # Look at the result

        self.ids.analysis.text = "The Analysis of Entered File Has been Saved!"

class DataSet(Screen):
    
    def clear(self):
        self.ids.dataset.text = ''
        self.ids.analysis.text = ''


class Manager(ScreenManager):
    pass


a = Builder.load_file('Code.kv')


class MyGrid(Widget):
    pass


class ØX(App):
    def build(self):
        return a


ØX().run()
