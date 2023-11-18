class AmbianceConfiguration:
    def __init__(self, music, image, lighting):
        self.music = music
        self.image = image
        self.lighting = lighting
    
    def to_json(self):
        """
        Convert AmbianceConfiguration to a JSON-serializable dictionary.

        :return: JSON-serializable dictionary representing the ambiance configuration.
        """
        return {
            'music': self.music,
            'image': self.image,
            'lighting': self.lighting
        }

button_pins = {
    1: 17,
    2: 18,
    3: 22,
    4: 23
}

ambiance_mapping = {
    1: AmbianceConfiguration(
        music='Ambiance 1 Music',
        image='Ambiance 1 Image',
        lighting='Ambiance 1 Lighting'
    ),
    2: AmbianceConfiguration(
        music='Ambiance 2 Music',
        image='Ambiance 2 Image',
        lighting='Ambiance 2 Lighting'
    ),
    3: AmbianceConfiguration(
        music='Ambiance 3 Music',
        image='Ambiance 3 Image',
        lighting='Ambiance 3 Lighting'
    ),
    4: AmbianceConfiguration(
        music='Ambiance 4 Music',
        image='Ambiance 4 Image',
        lighting='Ambiance 4 Lighting'
    )
}