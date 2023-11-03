import RPi.GPIO as GPIO
from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

rfid = RFID()

def onTagHandler(e):
    tag_data = e.Tag
    print("Tag RFID lu : " + tag_data)

# Définissez la fonction de rappel pour la lecture du tag
rfid.setOnTagHandler(onTagHandler)

try:
    rfid.openWaitForAttachment(2000)
    
    # On doit activer l'antenne pour pouvoir lire les tags
    rfid.setAntennaEnabled(True)

    while True:
        time.sleep(1)

except PhidgetException as e:
    print("Erreur Phidget : " + str(e))

finally:
    GPIO.cleanup()
