class MapChanger:
    def __init__(self):
        self.foret = loadImage("foret.png")
        self.montagne = loadImage("montagne.png")
        self.volcan = loadImage("volcan.png")
        self.desert = loadImage("desert.png")
        self.currentBG = self.foret
        
    def change_map(self,m):
        if m == "foret":
            self.currentBG = self.foret
        if m == "montagne":
            self.currentBG = self.montagne
        if m == "desert":
            self.currentBG = self.desert
        if m == "volcan":
            self.currentBG = self.volcan
            
    def draw(self):
        image(self.currentBG, 0, 0)
