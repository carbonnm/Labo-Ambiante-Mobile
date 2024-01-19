from pykka import *
import time

class BookActor(ThreadingActor):

    def __init__(self, led_actor, sound_actor, map_actor, mqtt_subscriber):
        super(BookActor, self).__init__()
        self.led_actor = led_actor
        self.sound_actor = sound_actor
        self.map_actor = map_actor
        self.mqtt_subscriber = mqtt_subscriber
        self.mqtt_subscriber.set_callback(self.on_mqtt_message)

    def on_mqtt_message(self, message):
        """
        Callback function to be called when a message is received from MQTT.
        """
        #command = message.get('command')
        #self.tell({'command': message})  # Tell itself the received command
        print(message)
        self.on_receive(message)

    def on_receive(self, message):
        """
        Cette fonction va réagir à ce qui est envoyé au Book (comme des boutons)
        """
        if message == 1:
            #Il faut setup toute l'ambiance montagne ici
            self.led_actor.tell({'command': 'montagne'})
            self.sound_actor.tell({'command': 'montagne'})
            self.map_actor.tell({'command': 'montagne'})

        if message == 2:
            #Il faut setup toute l'ambiance foret ici
            self.led_actor.tell({'command': 'foret'})
            self.sound_actor.tell({'command': 'foret'})
            self.map_actor.tell({'command': 'foret'})

        if message == 3:
            #Il faut setup toute l'ambiance desert ici
            self.led_actor.tell({'command': 'desert'})
            self.sound_actor.tell({'command': 'desert'})
            self.map_actor.tell({'command': 'desert'})

        if message == 4:
            #Il faut setup toute l'ambiance volcan ici
            self.led_actor.tell({'command': 'volcan'})
            self.sound_actor.tell({'command': 'volcan'})
            self.map_actor.tell({'command': 'volcan'})