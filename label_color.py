'''
Created on 16-Jul-2020

@author: Toshinee Bhasin
'''
# How to do Styling in label ?
# color =[0.41, 0.42, 0.74, 1] - blue
# color =[0.51, 0, 0.38, 10] -pink

import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
  
class MyLabelApp(App): 
    def build(self): 
        l2 = Label(text ="Money can buy anything !!:) and its Multi\nLine", font_size ='20sp', 
            color =[0.51, 0, 0.38, 10]) 
        return l2 
  

MyLabelApp().run() 
