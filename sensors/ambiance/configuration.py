class AmbianceConfiguration:
    def __init__(self, music, image, lighting):
        self.music = music
        self.image = image
        self.lighting = lighting

ambiance_mapping = {
    1: AmbianceConfiguration(),
    2: AmbianceConfiguration(),
    3: AmbianceConfiguration(),
    4: AmbianceConfiguration()
}

pressed_button_id = None