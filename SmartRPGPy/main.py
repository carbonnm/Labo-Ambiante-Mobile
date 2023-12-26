from pykka import *
from RFIDReaderActor import RFIDReaderActor
from ServoMotorActor import ServoMotorActor

#Lancement des acteurs
servo_actor = ServoMotorActor.start()
rfid_actor = RFIDReaderActor.start(servo_actor)

#Démarrer la lecture de tags RFID
rfid_actor.tell({'command': 'start_reading'})
