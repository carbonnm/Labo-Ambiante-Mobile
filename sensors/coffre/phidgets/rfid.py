from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time

class Rfid : 
    def __init__(self) :
        self.rfid = RFID()
        self.rfid.openWaitForAttachement(1000)
        self.rfid.setAntennaEnabled(True)
        self.rfid.setOnTagHandler(onTag)

    def onTag(self, tag) :
	    print("Tag: " + str(tag))
        #print("Protocol: " + str(protocol))