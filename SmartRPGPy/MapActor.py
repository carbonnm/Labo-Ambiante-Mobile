from pykka import *

class MapActor(ThreadingActor):

    def __init__(self):
        super(MapActor, self).__init__()

    def on_receive(self, message):
        """
        Cette fonction intercepte les messages qui indiquent un changement de map
        """
        if message.get('command') == 'desert':
            pass

        elif message.get('command') == 'foret':
            pass

        elif message.get('command') == 'volcan':
            pass
        
        elif message.get('command') == 'montagne':
            pass