from pykka import *

class DiceActor(ThreadingActor):

    def __init__(self, led_actor, sound_actor):
        super(DiceActor, self).__init__()
        self.led_actor = led_actor
        self.sound_actor = sound_actor

    def on_receive(self, message):
        """
        Lorsqu'un jet critique a lieu, ceci a une incidence sur les leds et sur les baffles
        """
        if message.get('command') == 'critique':
            self.sound_actor.tell({'command': 'critique'})
        
        if message.get('command') == 'excellent':
            self.sound_actor.tell({'command': 'excellent'})