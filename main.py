from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


Builder.load_string('''
<Wr>
    Label:
        text: 'ImageWriter'
        font_size : 40
        size_hint_y: 1.9
''')

class Wr(BoxLayout):
	pass 


class Writer(App):
    '''
    '''

    def build(self):
        return Wr()

if __name__ == '__main__':
    Writer().run()