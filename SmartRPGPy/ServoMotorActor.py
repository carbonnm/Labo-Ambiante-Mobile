import RPi.GPIO as GPIO
import time
from pykka import *

class ServoMotorActor(ThreadingActor):
    def __init__(self, pin):
        super(ServoMotorActor, self).__init__()
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, 50)
        self.servo.start(0)
        time.sleep(1)

    def on_receive(self, message):
        if message.get('command') == 'start_motor':
            self.start_motor(2, 12, 1, 0.1)

    def start_motor(self, start_duty, end_duty, step, delay):
        duty_cycle = start_duty
        while duty_cycle <= end_duty:
            self.servo.ChangeDutyCycle(duty_cycle)
            duty_cycle += step
            time.sleep(delay)

        while duty_cycle >= start_duty:
            self.servo.ChangeDutyCycle(duty_cycle)
            duty_cycle -= step
            time.sleep(delay)

        self.stop()

    def stop(self):
        self.servo.stop()
        GPIO.cleanup()