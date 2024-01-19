from pykka import *
import keyboard

class MapActor(ThreadingActor):

    def __init__(self):
        super(MapActor, self).__init__()

    def on_receive(self, message):
        """
        Cette fonction intercepte les messages qui indiquent un changement de map
        """
        if message.get('command') == 'desert':
            keyboard.press_and_release('c')

        elif message.get('command') == 'foret':
            keyboard.press_and_release('w')

        elif message.get('command') == 'volcan':
            keyboard.press_and_release('v')
        
        elif message.get('command') == 'montagne':
            keyboard.press_and_release('x')