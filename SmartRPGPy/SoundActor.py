from pykka import *
import keyboard

class SoundActor(ThreadingActor):

    def __init__(self):
        super(SoundActor, self).__init__()

    def on_receive(self, message):
        """
        Cette fonction intercepte les messages et fait jouer un son par le bafle 
        Il y a un son par ambiance 
        Ainsi que des sons supplémentaires à jouer si jets critiques
        """

        if message.get('command') == 'desert':
            keyboard.press_and_release('c')

        elif message.get('command') == 'volcan':
            keyboard.press_and_release('v')

        elif message.get('command') == 'montagne':
            keyboard.press_and_release('x')

        elif message.get('command') == 'foret':
            keyboard.press_and_release('w')

        elif message.get('command') == 'critique':
            keyboard.press_and_release('s')

        elif message.get('command') == 'excellent':
            keyboard.press_and_release('q')