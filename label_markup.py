'''
Created on 16-Jul-2020

@author: Toshinee Bhasin
'''
# How to markup the text ?

import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
  
class MyLabelApp(App): 
    def build(self): 
        l2 = Label(text ="[color = ff3333][b]'Label'[/b] is Added [/color]\n [color = 3333ff]Screen !!:):):):)[/color]", 
                  font_size ='20sp', markup = True) 
        return l2 
  

MyLabelApp().run() 
