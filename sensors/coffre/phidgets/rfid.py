from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time

class RFIDReader:
    def __init__(self):
        self.ch = RFID()

    def on_tag(self, tag, protocol):
        print("Tag: " + str(tag))
        print("Protocol: " + str(protocol))

    def start(self):
        try:
            self.ch.openWaitForAttachment(1000)
            self.ch.setAntennaEnabled(True)
            # Register for event before calling open
            self.ch.setOnTagHandler(self.on_tag)
            self.ch.open()

            time.sleep(1)
                # Do work, wait for events, etc.
            if self.ch.getTagPresent() == True:
                return True
            time.sleep(1)

        except PhidgetException as e:
            print(f"Phidget Exception: {e}")

        finally:
            self.ch.close()