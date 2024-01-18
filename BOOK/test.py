import RPi.GPIO as GPIO
import time

pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(pin) == GPIO.LOW:
            print("Button Pressed.")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
