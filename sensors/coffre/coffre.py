from sensors.coffre.phidgets.motor import Motor
from sensors.coffre.phidgets.rfid import Rfid

class Coffre:
    def __init__(self) :
        self.is_open = False
        
        self.motor = Motor()
        self.rfid = Rfid()

    def has_to_open(self):
        if self.rfid.getTagPresent() == True:
            return True
        return False

    def open(self) :
        self.motor.set_position(self, 90)


coffre = Coffre
if coffre.has_to_open():
    coffre.open()