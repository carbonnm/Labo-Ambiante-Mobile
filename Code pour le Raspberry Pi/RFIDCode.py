import RPi.GPIO as GPIO
from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time 

GPIO.setmode(GPIO.BOARD) #numérotation sur le board
GPIO.setwarnings(False) #plus de messages d'alertes

rfid = RFID()
print('je suis en attente d une clé')
rfid.openWaitForAttachment(1000)

rfid.setAntennaEnabled(True)

#Write 
#rfid.write("0x0000000000", RFIDProtocol.PROTOCOL_EM4100, False)

time.sleep(1)

rfid.getTagPresent()
print(rfid.getLastTag())

time.sleep(1)

rfid.setAntennaEnabled(False)