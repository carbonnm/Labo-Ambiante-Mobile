from Drops import Drops
from Snow import Snow

class WeatherSystem:
    def __init__(self):
        self.mode = 0
        self.d = []
        self.s = []
            
    def setup_weather(self):
        for i in range(500):
            self.s.append(Snow())
        for i in range(200):
            self.d.append(Drops())
            
    def set_mode(self,weather):
        self.mode = 0
        if weather == "snow":
            self.mode = 2
        elif weather == "rain":
            self.mode = 1
            
    def run(self):
        if self.mode == 1:
            self.draw_drops()
        elif self.mode == 2:
            self.draw_snow()
        
    def draw_drops(self):
        for i in range(len(self.d)):
            if self.d[i].y > self.d[i].endPos:
                self.d[i].end()
            else: 
                self.d[i].display()
            
    def draw_snow(self):
        for i in range(len(self.s)):
            if 0 > self.s[i].opacity:
                self.s[i].end()
            else: 
                self.s[i].display()
        
