from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from progress import ProgressBehavior


class ProgressButton(ProgressBehavior,Button):
    pass


Builder.load_string('''
<Wr>
    Label:
        text: 'ImageWriter'
        font_size : 40
        size_hint_y: 1.9
        Button:
            text: 'ChooseImage'
            font_size: 24
            pos: 1, 400
            size_hint: 1, 1
            width: 200
        Label:
            text:'Image'
            pos: 400, 400
            font_size: 24
            width: 500
        Spinner:
            text:'Devices'
            font_size: 24
            pos: 1, 260
            width: 200
        Label:
            text:'Name of device'
            font_size: 24
            pos: 260,260
            width: 500
        ProgressButton:
            text:'Progress'
            pos: 250 , 150
            width : 500
        Button:
            text:'Stop'
            pos: 260 , 1.0
            width: 150
        Button:
            text:'Write'
            pos: 600, 1.0
            width: 150



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