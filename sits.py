from kivy.uix.label import Label
from kivy.clock import Clock

class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.current = 0
        self.total = total
        my_text = 'Осталось приседаний:'

    def next(self, *args):
        pass