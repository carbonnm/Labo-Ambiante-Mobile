width=1920
height=1080
framerate=24
divide = width/6

class Lightning:
    def __init__(self):
        self.energy = framerate * 3
        
    def strike(self,xi):
        y = 0
        while y < 1000:
           endX = xi + int(random(-6,6))
           endY = y + 2
           strokeWeight(4)
           stroke(color(255,0,0))
           line(xi,y,endX,endY)
           xi = endX
           y = endY
           
    def show(self):
        for i in range(1,6):
            self.strike(divide*i)
        self.energy -= 1
    
    def isAlive(self):
        return self.energy > 0
