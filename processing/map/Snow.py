width=1800
height=1000

class Snow:
    def __init__(self):
        self.init()
        
    def init(self):
        self.x = random(width)
        self.y = random(-300,0)
        self.speed = random(1,2)
        self.c = color(255,255,255)
        self.ellipseSize = random(6,10)
        self.opacity = 40*self.ellipseSize
        self.endPos = random(height)
    
    def update(self):
        self.y+=self.speed
        self.opacity -= 0.5
        
    def display(self):
        fill(self.c,self.opacity)
        stroke(0,self.opacity)
        strokeWeight(1)
        #noStroke()
        ellipse(self.x,self.y,self.ellipseSize,self.ellipseSize)
        self.update()
        
    def end(self):
        self.init()
