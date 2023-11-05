from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
import time

class Motor :
    def __init__(self) :
        self.motor = RCServo()
        self.motor.openWaitForAttachment(1000)

    def set_position(self, degree) :
        self.motor.setVelocityLimit(30)
        self.motor.setTargetPosition(degree)
        self.motor.setEngaged(True)
        time.sleep(1)
        
    def close_motor(self) :
        self.motor.setEngaged(False)
        self.motor.close()