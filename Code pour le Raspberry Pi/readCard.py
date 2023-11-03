import RPi.GPIO as GPIO
from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

rfid = RFID()

def onTagHandler(e):
    print("Tag RFID lu : " + e.Tag)

try:
    rfid.openWaitForAttachment(2000)

    while True:
        print("Hold the tag near the reader")
        rfid.setOnTagHandler(onTagHandler)

        time.sleep(1)

finally:
    GPIO.cleanup()
