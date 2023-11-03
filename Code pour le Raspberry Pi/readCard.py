import RPi.GPIO as GPIO
from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time 

GPIO.setmode(GPIO.BOARD) #numérotation sur le board
GPIO.setwarnings(False) #plus de messages d'alertes

rfid = RFID()
print('je suis en attente d une clé')
rfid.openWaitForAttachment(1000)

try:
    while True:
        print("Hold the tag near the reader")

        # Essayez de lire le tag
        tag_data = rfid.readTag()
        
        if tag_data is not None:
            print("Données lues du tag RFID : " + tag_data)
        else:
            print("Aucune donnée lue sur le tag RFID")

        # Fermez le lecteur RFID
        rfid.close()
finally:
    GPIO.cleanup()