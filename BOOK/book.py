import RPi.GPIO as GPIO
import time

buttons = {
    "4": 7
}

GPIO.setmode(GPIO.BCM)


for button, pin in buttons.items():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        for button, pin in buttons.items():
            if GPIO.input(pin) == GPIO.LOW:
                print(f"{button} pressed.")
                time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()
