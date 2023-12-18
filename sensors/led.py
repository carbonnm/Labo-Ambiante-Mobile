import time
import board
import neopixel

# initialisation
pixel_pin = board.D18
num_pixels = 60
ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

# ambiance volcan (imitation du feu)
'''
def volcano(pos):
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
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

while True:
    for i in range(256):
        color = volcano(i)
        pixels.fill(color)
        pixels.show()
        time.sleep(0.01)
'''

# ambiance désert (imitation du sable qui vole)
'''
def desert(pos):
    #Transition du blanc au jaune
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 128:
        r = g = b = int(pos * 2)
    else:
        pos -= 128
        r = g = 255
        b = int(pos * 2)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

while True:
    for i in range(256):
        color = desert(i)
        pixels.fill(color)
        pixels.show()
        time.sleep(0.01)
'''

# ambiance forêt (imitaion des sous bois)
'''
def forest(pos):
    #Transition du vert au noir
    if pos < 0 or pos > 255:
        r = g = b = 0
    else:
        r = 0
        g = int(255 - pos * 2)
        b = 0
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

while True:
    for i in range(256):
        color = forest(i)
        pixels.fill(color)
        pixels.show()
        time.sleep(0.01)
'''

# ambiance montagne (imitation des rafales de neige)
'''
def mountain(pos):
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
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

while True:
    for i in range(256):
        color = mountain(i)
        pixels.fill(color)
        pixels.show()
        time.sleep(0.01)
'''
