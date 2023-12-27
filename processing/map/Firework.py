class Firework:
    def __init__(self,pos,v):
        self.c = color(random(255),random(255),random(255))
        self.trail = Firetrail(self.c)
        self.trail.pos = pos
        self.trail.v = v
        self.spark = None
        
    def update(self):
        if self.trail != None:
            self.trail.update()
            if self.trail.energy<0:
                self.spark = Spark(self.trail.pos,self.c)
                self.trail = None
                
    def show(self):
        if self.trail != None:
            self.trail.show()
        if self.spark != None:
            self.spark.show()
            
    def isAlive(self):
        return (self.trail != None) or (self.spark != None)
    
class Firetrail:
    def __init__(self,c):
        self.pos = PVector(0,0)
        self.v = PVector(0,0)
        self.ps = []
        self.energy=200
        self.c = c
        
    def update(self):
        self.energy -= random(3)
        if self.energy > 50:
            self.pos.add(self.v)
            self.v.add(PVector(0,0.05))
        self.ps.append(self.pos.copy())
        if len(self.ps)>25:
            del self.ps[0]
    
    def show(self):
        n = len(self.ps)
        prevP = None
        stroke(self.c,self.energy + 55)
        for i in range(n):
            strokeWeight(float(i)/n*10)
            p = self.ps[i]
            if prevP != None and prevP.x != 0 and prevP.y != 0:
                line(p.x,p.y,prevP.x,prevP.y)
            prevP = p
        strokeWeight(1)
        
    def kill_faster(self):
        self.energy -= random(3)
        
class Spark:  
    def __init__(self,center,c):
            self.center = center
            self.c = c
            self.trails = []
            for i in range(10):
                trail = Firetrail(self.c)
                trail.pos = center.copy()
                theta = random(PI)
                phi = random(TWO_PI)
                r = 2
                trail.v = PVector(r*sin(theta)*cos(phi), r*sin(theta)*sin(phi), r*cos(theta))
                self.trails.append(trail)
  
    def show(self):
        for i in range(len(self.trails)):
            trail = self.trails[i]
            if trail.energy > 0:
                trail.update()
                trail.show()
                trail.kill_faster()
        
