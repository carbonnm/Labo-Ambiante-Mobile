from Phidget22.Phidget import *
from Phidget22.Devices.RFID import *
import time
from pykka import *

class RFIDReaderActor(ThreadingActor):
    def __init__(self, servo_actor):
        super(RFIDReaderActor, self).__init__()
        self.servo_actor = servo_actor
        self.ch = RFID()

    def on_receive(self, message):
        if message.get('command') == 'start_reading':
            self.start_reading()

    def start_reading(self):
        try:
            self.ch.openWaitForAttachment(1000)
            self.ch.setAntennaEnabled(True)
            self.ch.setOnTagHandler(self.on_tag)
            self.ch.open()

            while True:
                if self.ch.getTagPresent() == True:
                    return True
                time.sleep(1)

        except PhidgetException as e:
            print(f"Phidget Exception: {e}")

        finally:
            self.ch.close()

    def on_tag(self, tag, protocol):
        print("Tag: " + str(tag))
        print("Protocol: " + str(protocol))
        #Si on trouve un tag, on dit au moteur de se lancer
        self.servo_actor.tell({'command': 'start_motor'})