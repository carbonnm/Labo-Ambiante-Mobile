from pykka import *
import time
from mqtt_subscriber import MQTTSubscriber

class BookActor(ThreadingActor, MQTTSubscriber):

    def __init__(self, led_actor, sound_actor, map_actor):
        super(BookActor, self).__init__()
        self.led_actor = led_actor
        self.sound_actor = sound_actor
        self.map_actor = map_actor

    def on_message(self, client, userdata, message):
        print(f"marie est trop belle {message}")

    def on_receive(self, message):
        """
        Cette fonction va réagir à ce qui est envoyé au Book (comme des boutons)
        """
        if message.get('command') == 1:
            #Il faut setup toute l'ambiance montagne ici
            self.led_actor.tell({'command': 'montagne'})
            self.sound_actor.tell({'command': 'montagne'})
            self.map_actor.tell({'command': 'montagne'})

        if message.get('command') == 2:
            #Il faut setup toute l'ambiance foret ici
            self.led_actor.tell({'command': 'foret'})
            self.sound_actor.tell({'command': 'foret'})
            self.map_actor.tell({'command': 'foret'})

        if message.get('command') == 3:
            #Il faut setup toute l'ambiance desert ici
            self.led_actor.tell({'command': 'desert'})
            self.sound_actor.tell({'command': 'desert'})
            self.map_actor.tell({'command': 'desert'})

        if message.get('command') == 4:
            #Il faut setup toute l'ambiance volcan ici
            self.led_actor.tell({'command': 'volcan'})
            self.sound_actor.tell({'command': 'volcan'})
            self.map_actor.tell({'command': 'volcan'})