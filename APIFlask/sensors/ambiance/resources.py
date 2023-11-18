from flask_restful import Resource
from configuration import ambiance_mapping, pressed_button_id
import RPi.GPIO as GPIO

# Configurer les pins
button_pin = 17

class AmbianceResource(Resource):
    def get(self, button_id):
        if button_id not in ambiance_mapping:
            return {'error': 'Button not found.'}, 404
        
        if button_id == pressed_button_id:
            pressed_button_id = None
        
        ambiance_config = ambiance_mapping[button_id]
        
        return {
            'music': ambiance_config.music,
            'image': ambiance_config.image,
            'lighting' : ambiance_config.lighting
        }
    
    def put(self, button_id):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        if GPIO.input(button_pin) == GPIO.LOW:
            pressed_button_id = button_id
            return {'status': 'Button pressed'}
        else:
            return {'status': 'Button not pressed'}