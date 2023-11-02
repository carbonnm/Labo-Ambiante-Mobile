import RPi.GPIO as GPIO
from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time 

GPIO.setmode(GPIO.BOARD) #numérotation sur le board
GPIO.setwarnings(False) #plus de messages d'alertes

rfid = RFID()

try:
    while True:
        text = input("Enter the text to write: ")
        print("Hold the tag near the reader")
        card_id, card_text = rfid.write(text)
        print(card_id)
        print(card_text)

finally:
    GPIO.cleanup()