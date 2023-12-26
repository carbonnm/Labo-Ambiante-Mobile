from pykka import *
import time
from RFIDReaderActor import RFIDReaderActor
from ServoMotorActor import ServoMotorActor
from LedActor import LedActor
from BookActor import BookActor
from DiceActor import DiceActor
from MapActor import MapActor
from SoundActor import SoundActor

#Lancement des acteurs
servo_actor = ServoMotorActor.start(pin=11)
rfid_actor = RFIDReaderActor.start(servo_actor)
led_actor = LedActor.start()
map_actor = MapActor.start()
sound_actor = SoundActor.star()

#Le livre doit avoir en paramètre les leds, le baffle, la map
book_actor = BookActor(led_actor, sound_actor, map_actor)
#Le dé a accès au baffle et aux lumières
dice_actor = DiceActor.start(led_actor, sound_actor)

#Démarrer la lecture de tags RFID
rfid_actor.tell({'command': 'start_reading'})