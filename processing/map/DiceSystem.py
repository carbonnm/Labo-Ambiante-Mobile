from Firework import Firework

class DiceSystem:
    def __init__(self):
        self.f = []
        self.n = 10
        
    def run(self):
        if len(self.f) != 0:
            c = 0
            for i in range(len(self.f)):
                self.f[i].update()
                self.f[i].show()
                if not self.f[i].isAlive():
                    c += 1
            if c == self.n:
                self.f = []
                
    def win(self):
        self.f = []
        for i in range(self.n):
            self.f.append(Firework(PVector(width/2, height), PVector(random(-6, 6), random(-10, -6))))
        
