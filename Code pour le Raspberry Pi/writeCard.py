import RPi.GPIO as GPIO
from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time 

GPIO.setmode(GPIO.BOARD) #numérotation sur le board
GPIO.setwarnings(False) #plus de messages d'alertes

rfid = RFID()

rfid.openWaitForAttachment(1000)
try:
    while True:
        print("Hold the tag near the reader")
        card_id, card_text = rfid.write("0x0000000000", RFIDProtocol.PROTOCOL_EM4100, False)
        print(card_id)
        print(card_text)

finally:
    GPIO.cleanup()