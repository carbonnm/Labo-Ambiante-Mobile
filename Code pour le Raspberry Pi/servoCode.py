"""
import RPi.GPIO as GPIO
import time

#from Phidget22.Phidget import *
#from Phidget22.Devices.RCServo import *

#Habituellement, on attache le servo à la pin 11 du raspberry, qui sera donc un pin d'output

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

#Création du RCServo avec une fréquence de 50 Hz
servo = GPIO.PWM(11, 50)

#Start the servo but with value of 0 (no pulse)
servo.start(0)
time.sleep(1)

#Move the servo
duty = 2
while duty <= 12:
    servo.ChangeDutyCycle(duty)
    duty += 1
    time.sleep(0.1)

while duty >= 2:
    servo.ChangeDutyCycle(duty)
    duty -= 1
    time.sleep(0.1)

#Fin 
servo.stop()
GPIO.cleanup()
"""

from gpiozero import Servo
from time import sleep

# Utilisez le numéro de la broche GPIO connectée au servo
# (par exemple, la broche 17, mais cela dépend de votre configuration)
servo = Servo(11)

while True:
    servo.min()
    sleep(1)
    servo.mid()
    sleep(1)
    servo.max()
    sleep(1)