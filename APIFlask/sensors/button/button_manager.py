import RPi.GPIO as GPIO
import requests
import threading
from configuration import button_pins

def button_pressed_callback(channel, button_id):
    print(f"Button {button_id} pressed")
    response = request.put(f"http://127.0.0.1:5000/ambiance/{button_id}")
    print(response.json())

def setup_button_manager():
    GPIO.setmode(GPIO.BCM)
    
    for button_id, pin in button_pins.items():
        
        callback_function = lambda channel, button_id = button_id: button_pressed_callback(channel, button_id)
        
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=callback_function, bouncetime=300)