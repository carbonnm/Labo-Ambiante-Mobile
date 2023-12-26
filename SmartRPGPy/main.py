from pykka import *
import time
from RFIDReaderActor import RFIDReaderActor
from ServoMotorActor import ServoMotorActor
from LedActor import LedActor

#Lancement des acteurs
servo_actor = ServoMotorActor.start(pin=11)
rfid_actor = RFIDReaderActor.start(servo_actor)
led_actor = LedActor.start()

#Démarrer la lecture de tags RFID
rfid_actor.tell({'command': 'start_reading'})

led_actor.tell({'command': 'volcan'})

time.sleep(10)
led_actor.tell({'command': 'desert'})