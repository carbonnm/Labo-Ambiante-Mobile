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

"""
while True:
    rfid.wait_for_tag()
    #Si une puce est lue, on récup ses infos
    (error, tag_typ) = rfid.request()

    if not error:
        # utile si plusieurs puces passent en même temps
        (error, uid) = rfid.anticoll()

        if not error :
            # On affiche l'id de la cle lue
            print('Ceci est la cle avec l id : {}'.format(uid))
            #if RFID_UID == uid:
                #print('Ceci est la bonne cle')
                #On pourrait rajouter du code par exemple allumer une led ou ouvrir le coffre avec le modèle HS-422
            #else :
                #print('Ceci n est pas la bonne cle')
            time.sleep(1) #pour pas lire en boucle le même
"""
if rfid.tagPresent():
    print(rfid.getLastTag())
    
rfid.setAntennaEnabled(False)