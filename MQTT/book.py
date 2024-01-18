import RPi.GPIO as GPIO
import time
from mqtt_publisher import MQTTPublisher

GPIO.setmode(GPIO.BOARD)

pages_pin = {1 : 7, 2 : 11, 3 : 13, 4 : 15}
baguette_pin = 6

#Initialisation du publisher MQTT
def main():
    mqtt_publisher = MQTTPublisher("192.168.0.238", 1883, "SmartRPG", "SmartRPG", "channel_ambiances")

    for pin in pages_pin:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        while True:
            for pin_button, broche in pages_pin.items():
                if GPIO.input(broche) == GPIO.LOW:
                    print(f"Page numéro {pin_button} touchée")
                    #Envoi d'un message MQTT correspondant au numéro de page touché
                    mqtt_publisher.publish_message(pin_button, "channel_ambiances")

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Arrêt du programme.")

    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
