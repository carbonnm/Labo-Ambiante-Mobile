from WeatherSystem import WeatherSystem
from MapChanger import MapChanger
from DiceSystem import DiceSystem

from Firework import Firework

width=1800
height= 1000

def setup():
    global ws, m, d
    size(width,height)
    background(0,0,0)
    
    d = DiceSystem()
    
    m = MapChanger()

    ws = WeatherSystem()
    ws.setup_weather()
    ws.set_mode("rain")
    
    global f
    f = []
    
def event_handler():
    return 1

def keyPressed():
  if key == 'w':
    ws.set_mode("rain")
    m.change_map("foret")
  elif key == 'x':
    ws.set_mode("snow")
    m.change_map("montagne")
  elif key == 'c':
    ws.set_mode("dust")
    m.change_map("desert")
  elif key == 'v':
    ws.set_mode("lava")
    m.change_map("volcan")
  elif key == 'n':
    d.win()

def draw():
            
    m.draw()
    ws.run()
    d.run()
    
    
    
    
