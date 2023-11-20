import RPi.GPIO as GPIO
import time

class Motor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.pin, 50)
        self.servo.start(0)
        time.sleep(1)

    def move_servo(self, start_duty, end_duty, step, delay):
        duty_cycle = start_duty
        while duty_cycle <= end_duty:
            self.servo.ChangeDutyCycle(duty_cycle)
            duty_cycle += step
            time.sleep(delay)

        while duty_cycle >= start_duty:
            self.servo.ChangeDutyCycle(duty_cycle)
            duty_cycle -= step
            time.sleep(delay)

    def stop(self):
        self.servo.stop()
        GPIO.cleanup()