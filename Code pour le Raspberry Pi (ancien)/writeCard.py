import RPi.GPIO as GPIO
from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time 

GPIO.setmode(GPIO.BOARD) #numérotation sur le board
GPIO.setwarnings(False) #plus de messages d'alertes

rfid = RFID()

rfid.openWaitForAttachment(2000)
try:
    while True:
        print("Hold the tag near the reader")
        rfid.write("TAG-1", RFIDProtocol.PROTOCOL_PHIDGETS, False)
        time.sleep(2)
        rfid.close()

finally:
    GPIO.cleanup()