# Ecrit ton programme ici ;-)
# Etape 1 : activer le protocole SPI pour utiliser le module RFID
#--------------------------------------------------------------------
# 1. sudo raspi-config
# 2. Interfacing options -> SPI -> Yes -> Finish

#Etape 2 : Installer la librairie pi-rc522
#--------------------------------------------------------------------
#ATTENTION, Nous ça changera sûrement si on a un autre lecteur RFID je sais juste pas lequel on a
# sudo pip3 install pi-rc522

#Etape 3 : Ecrire un programme qui lit l'id d'un badge RFID
#------------------------------------------------------------------------
# Aller dans le dossier home/pi/electronics et créer un fichier read_rfid_id.py avec ce code

import RPi.GPIO as GPIO
# à adapter pour nous je suppose
from pirc522 import RFID
import time

GPIO.setmode(GPIO.BOARD) #numérotation sur le board
GPIO.setwarnings(False) #plus de messages d'alertes

#On définit ici quels sont les UID "valides" des badges (ex ici 3 et 5)
RFID_UID = [3, 5]

rc522 = RFID()  #instance de la librairie
print('je suis en attente d une clé')

#Lecture en boucle d'une potentielle clé

while True:
    rc522.wait_for_tag()
    #Si une puce est lue, on récup ses infos
    (error, tag_typ) = rc522.request()

    if not error:
        # utile si plusieurs puces passent en même temps
        (error, uid) = rc522.anticoll()

        if not error :
            # On affiche l'id de la cle lue
            print('Ceci est la cle avec l id : {}'.format(uid))
            if RFID_UID == uid:
                print('Ceci est la bonne cle')
                #On pourrait rajouter du code par exemple allumer une led ou ouvrir le coffre avec le truc
            else :
                print('Ceci n est pas la bonne cle')
            time.sleep(1) #pour pas lire en boucle le même


#Etape 4 : Autoriser l'exécution
#---------------------------------------------------------------
sudo chmod +x /home/pi/electronics/read_rfid_id.py

#Etape 5 : appeler le programme
#----------------------------------------------------------------
/home/pi/electronics/read_rfid_id.py