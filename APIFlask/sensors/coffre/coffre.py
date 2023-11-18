from sensors.coffre.phidgets.motor import Motor
from sensors.coffre.phidgets.rfid import Rfid

class Coffre:
    def __init__(self) :
        self.is_open = False
        
        self.motor = Motor()
        self.rfid = Rfid()

    def open(self) :
        """Ici mettre le code pour ouvrir le coffre"""
        pass