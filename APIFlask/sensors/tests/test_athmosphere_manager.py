# test_athmosphere_manager.py
import unittest
from unittest.mock import MagicMock
import requests
from book.athmosphere_manager import AthmosphereManager

class TestAthmosphereManager(unittest.TestCase):
    def test_button_pressed_callback(self):
        # Créez une instance d'AthmosphereManager avec une URL fictive
        api_url = "http://example.com/api"
        athmosphere_manager = AthmosphereManager(api_url)

        # Mock la fonction requests.put pour éviter les appels réseau réels pendant les tests
        requests.put = MagicMock()

        # Simulez l'appui sur le bouton 17
        athmosphere_manager.button_pressed_callback(17)

        # Vérifiez que requests.put a été appelé avec les paramètres attendus
        expected_url = f"{api_url}/ambiance"
        expected_json = AthmosphereManager(
            music='Ambiance 1 Music',
            image='Ambiance 1 Image',
            lighting='Ambiance 1 Lighting'
        ).to_json()
        requests.put.assert_called_once_with(expected_url, json=expected_json)

if __name__ == '__main__':
    unittest.main()
