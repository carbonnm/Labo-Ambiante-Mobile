import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pages_pin = [7, 11, 13, 15]
baguette_pin = 6

for pin in pages_pin:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        for pin_button in pages_pin:
            if GPIO.input(pin_button) == GPIO.LOW:
                print(f"Page numéro {pin_button} touchée")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Arrêt du programme.")

finally:
    GPIO.cleanup()
