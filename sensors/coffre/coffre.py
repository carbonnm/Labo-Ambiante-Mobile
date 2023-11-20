from phidgets.motor import Motor
from phidgets.rfid import RFIDReader

import RPi.GPIO as GPIO
import time

class Coffre:
    def __init__(self) :
        self.is_open = False
        
        #self.motor = Motor(11)
        #self.rfid = Rfid()

    def has_to_open(self):
        rfid = RFIDReader()
        if rfid.start() == True:
            print("J'ai trouvé un tag")
            return True
        return False

    def open(self) :
        try:
            servo_motor = Motor(11)
            servo_motor.move_servo(2, 12, 1, 0.1)

        except KeyboardInterrupt:
            servo_motor.stop()
            print("Arrêt manuel du programme.")

        except Exception as e:
            print(f"Une erreur est survenue : {e}")

        finally:
            servo_motor.stop()
            print("Programme terminé.")


coffre = Coffre()
while True:
    if coffre.has_to_open():
        coffre.open()

GPIO.cleanup()