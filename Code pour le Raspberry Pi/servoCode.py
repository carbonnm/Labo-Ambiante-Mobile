import RPi.GPIO as GPIO
import time

#Habituellement, on attache le servo à la pin 11 du raspberry, qui sera donc un pin d'output

GPIO.setmode(GPIO.board)
GPIO.setup(11, GPIO.OUT)

#Création d'un object PWM de contrôle avec une fréquence de 50 hertz
pwm = GPIO.PWM(11, 50)