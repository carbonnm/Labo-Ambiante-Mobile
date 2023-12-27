width=1800
height=1000

class Drops:
    def __init__(self):
        self.x = random(width)
        self.y = random(-300,0)
        self.speed = random(5,10)
        self.c = color(28,163,236)
        self.history = []
        self.ellipseX = 0
        self.ellipseY = 0
        self.endPos = random(height)
        
    def init(self):
        self.x = random(width)
        self.y = random(-300,0)
        self.speed = random(5,10)
        self.c = color(28,163,236)
        self.history = []
        self.ellipseX = 0
        self.ellipseY = 0
        self.endPos = random(height)
    
    def update(self):
        self.y+=self.speed
        self.history.append(self.y)
        if len(self.history) > 2:
            del self.history[0]
        
    def display(self):
        fill(self.c)
        noStroke()
        rect(self.x,self.y,1,10)
        l = len(self.history)
        for i in range(l):
            fill(self.c,255-i*50)
            noStroke()
            rect(self.x,self.history[l-1-i],1,10)
        self.update()
        
    def end(self):
        stroke(self.c)
        noFill()
        ellipse(self.x,self.y,self.ellipseX,self.ellipseY)
        self.ellipseY += self.speed/2-1
        self.ellipseX += (self.speed/2)
        if (self.ellipseX>10):
            self.init()
