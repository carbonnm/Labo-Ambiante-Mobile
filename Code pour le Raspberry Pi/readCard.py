import RPi.GPIO as GPIO
from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

rfid = RFID()

rfid.openWaitForAttachment(2000)

#On doit l'enable pour pouvoir lire les tags
rfid.setAntennaEnabled(True)

val = rfid.getLastTag()
print("****")
print(val)

rfid.close()
