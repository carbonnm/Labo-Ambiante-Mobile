import RPi.GPIO as GPIO
import requests
from configuration import button_pins, ambiance_mapping

class AthmosphereManager:
    def __init__(self, api_url):
        """
        Constructor for the AthmosphereManager class.

        :param api_url: The URL of the API to which to send ambiance configurations.
        """
        self.api_url = api_url
        GPIO.setmode(GPIO.BCM)

        # Configure buttons and associated GPIO pins
        for button_id, pin in button_pins.items():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            
            # Add event detection for each button
            GPIO.add_event_detect(
                pin, 
                GPIO.FALLING, 
                callback=self.button_pressed_callback(button_id), 
                bouncetime=300)
        
    def button_pressed_callback(self, button_id):
        """
        Method called when a button is pressed.

        :param button_id: The ID of the pressed button.
        """
        print(f"Button {button_id} pressed")
        
        # Check if the button ID is associated with an ambiance configuration
        if button_id in ambiance_mapping:
            ambiance_config = ambiance_mapping[button_id]

            # Send the ambiance configuration to the API using a PUT request
            response = requests.put(f"{self.api_url}/ambiance", json=ambiance_config.to_json())
            print(response.json())