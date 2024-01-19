from pykka import *
import time
import board
import neopixel

class LedActor(ThreadingActor):
    def __init__(self):
        super(LedActor, self).__init__()
        self.pixel_pin = board.D18
        self.num_pixels = 60
        self.ORDER = neopixel.RGB
        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=0.2, auto_write=False, pixel_order=self.ORDER
        )

    def on_receive(self, message):
        """
        Reçoit un message qui indique quelle est le décor choisi
        Cela permet de changer la couleur des leds à une couleur appropriée
        """
        if message.get('command') == 'volcan':
            self.volcan()

        elif message.get('command') == 'montagne':
            self.montagne()

        elif message.get('command') == 'foret':
            self.foret()
            
        elif message.get('command') == 'desert':
            self.desert()
        
        elif message.get('command') == 'mauvais':
            self.mauvais(1, 3)

        elif message.get('command') == 'neutre':
            self.neutre(1, 3)

        elif message.get('command') == 'excellent':
            self.excellent(1, 3)
    

    def mauvais(self, duree, repetitions):
        for _ in range(repetitions):
            self.pixels.fill((255, 0, 0))
            self.pixels.show()
            time.sleep(duree)
            self.pixels.fill((0, 0, 0))
            self.pixels.show()
            time.sleep(duree)


    def neutre(self, duree, repetitions):
        for _ in range(repetitions):
            self.pixels.fill((255, 255, 255))
            self.pixels.show()
            time.sleep(duree)
            self.pixels.fill((0, 0, 0))
            self.pixels.show()
            time.sleep(duree)


    def excellent(self, duree, repetitions):
        for _ in range(repetitions):
            self.pixels.fill((0, 255, 0))
            self.pixels.show()
            time.sleep(duree)
            self.pixels.fill((0, 0, 0))
            self.pixels.show()
            time.sleep(duree)


    def volcan(self):
        for i in range(256):
            color = self.volcano_effect(i)
            self.pixels.fill(color)
            self.pixels.show()
            time.sleep(0.01)
    
    def montagne(self):
        for i in range(256):
            color = self.montagne_effect(i)
            self.pixels.fill(color)
            self.pixels.show()
            time.sleep(0.01)
    
    def foret(self):
        for i in range(256):
            color = self.foret_effect(i)
            self.pixels.fill(color)
            self.pixels.show()
            time.sleep(0.01)

    def desert(self):
        for i in range(256):
            color = self.desert_effect(i)
            self.pixels.fill(color)
            self.pixels.show()
            time.sleep(0.01)

    def volcano_effect(self, pos):
        # transition du jaune au rouge
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 128:
            r = 255 - int(pos * 2)
            g = 255
            b = 0
        else:
            pos -= 128
            r = 255
            g = int(pos * 2)
            b = 0
        return (r, g, b) if self.ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)
    
    def montagne_effect(self, pos):
        #transition du blanc au bleu 
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 128:
            r = g = int(pos * 2)
            b = 255
        else:
            pos -= 128
            r = g = 255 - int(pos * 2)
            b = 255
        return (r, g, b) if self.ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)
    
    def foret_effect(self, pos):
        #Transition du vert au noir
        if pos < 0 or pos > 255:
            r = g = b = 0
        else:
            r = 0
            g = int(255 - pos * 2)
            b = 0
        return (r, g, b) if self.ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)
    
    def desert_effect(self, pos):
        #Transition du blanc au jaune
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 128:
            r = g = b = int(pos * 2)
        else:
            pos -= 128
            r = g = 255
            b = int(pos * 2)
        return (r, g, b) if self.ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)