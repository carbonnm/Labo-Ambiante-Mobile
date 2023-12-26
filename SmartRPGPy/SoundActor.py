from pykka import *

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
            pass

        elif message.get('command') == 'volcan':
            pass

        elif message.get('command') == 'montagne':
            pass

        elif message.get('command') == 'foret':
            pass

        elif message.get('command') == 'critique':
            pass

        elif message.get('command') == 'excellent':
            pass