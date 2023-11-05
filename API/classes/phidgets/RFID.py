from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time

class RFID :
    def __init__(self) :
        self.rfid = RFID()
        self.rfid.openWaitForAttachment(1000)
        self.rfid.setAntennaEnabled(True)
        self.rfid.setDeviceSerialNumber(384641)
    
    def onTag(self, tag, protocol):
        print("Tag: " + str(tag))
        print("Protocol: " + str(protocol))

    def read_tag(self) :
        self.rfid.setOnTagHandler(onTag)
        self.rfid.open()
        while True:
            print(self.rfid.getTagPresent())
            time.sleep(1)

    def write_tag(self) :
        self.rfid.write("TAG-1", RFIDProtocol.PROTOCOL_PHIDGETS, False)

    def close_rfid(self) :
        self.rfid.close_rfid()


