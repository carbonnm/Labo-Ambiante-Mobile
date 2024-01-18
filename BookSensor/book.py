import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pages_pin = [17, 18, 22, 23]
baguette_pin = 6

def page_touched(channel):
    page_number = pages_pin.index(channel) + 1
    print(f"Tu as touché la page {page_number} avec la baguette magique")

for pin in pages_pin:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback = page_touched, bouncetime=300)

GPIO.setup(baguette_pin, GPIO.IN)
GPIO.add_event_detect(baguette_pin, GPIO.FALLING, callback=page_touched, bouncetime=300)

try:
    print("En attente des touches de la baguette magique sur les pages...")
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Arrêt du programme.")

finally:
    GPIO.cleanup()
