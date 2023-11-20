from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time

def onTag(self, tag, protocol):
	print("Tag: " + str(tag))
	print("Protocol: " + str(protocol))

ch = RFID()

ch.openWaitForAttachment(1000)

ch.setAntennaEnabled(True)

# Register for event before calling open
ch.setOnTagHandler(onTag)

ch.open()

while True:
	# Do work, wait for events, etc.
    print(ch.getTagPresent())
    time.sleep(1)
	