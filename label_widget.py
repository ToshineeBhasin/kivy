'''
Label widget 
The Label widget is for rendering text. It supports ascii and unicode strings.
Label is the text which we want to add on our window, give to the buttons and 
so on. On labels, we can apply the styling also i.e increase text, size, color and more.
'''
import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
  
class MyLabelApp(App): 
    def build(self): 
        lbl = Label(text ="Money can buy anything !!:):)",font_size=30) 
        return lbl 
  

MyLabelApp().run() 
