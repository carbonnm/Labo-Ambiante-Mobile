import RPi.GPIO as GPIO
import time
from pykka import *

class ServoMotorActor(ThreadingActor):
    def __init__(self):
        super(ServoMotorActor, self).__init__()
       	#GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        self.servo = GPIO.PWM(11, 50)
        self.servo.start(0)
        time.sleep(1)

    def on_receive(self, message):
        if message.get('command') == 'start_motor':
            print("Moteur active")
            duty = 2
            while duty <= 12:
                self.servo.ChangeDutyCycle(duty)
                duty += 1
                time.sleep(0.1)

            while duty >= 2:
                self.servo.ChangeDutyCycle(duty)
                duty -= 1
                time.sleep(0.1)

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