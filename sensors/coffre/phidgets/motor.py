from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
import time
import RPi.GPIO as GPIO

class Motor:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        try:
            self.motor = GPIO.PWM(11, 50)
            self.motor.start(0)
            time.sleep(1)
            #self.motor.openWaitForAttachment(1000)
        except PhidgetException as e:
            print(f"Erreur lors de l'initialisation du moteur : {e.details}")
            # Ajoutez ici tout code de gestion de l'erreur nécessaire.
        except Exception as e:
            print(f"Erreur inattendue : {e}")

    def set_position(self, degree):
        self.motor.setVelocityLimit(30)
        self.motor.setTargetPosition(degree)
        self.motor.setEngaged(True)
        time.sleep(3)
        self.motor.setEngaged(False)
    
    def move_motor(self) :
        duty = 2
        while duty <= 12:
            self.motor.ChangeDutyCycle(duty)
            duty += 1
            time.sleep(0.1)

        while duty >= 2:
            self.motor.ChangeDutyCycle(duty)
            duty -= 1
            time.sleep(0.1)

    def close_motor(self):
        self.motor.close()
        GPIO.cleanup()