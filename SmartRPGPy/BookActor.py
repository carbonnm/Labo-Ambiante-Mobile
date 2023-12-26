from pykka import *
import time

class BookActor(ThreadingActor):
    
    def __init__(self):
        pass

    def on_receive(self, message):
        if message.get('command') == 1:
            pass
        if message.get('command') == 2:
            pass
        if message.get('command') == 3:
            pass
        if message.get('command') == 4:
            pass