from pykka import *
import time
from RFIDReaderActor import RFIDReaderActor
from ServoMotorActor import ServoMotorActor
from LedActor import LedActor
from BookActor import BookActor
from DiceActor import DiceActor
from MapActor import MapActor
from SoundActor import SoundActor
from mqtt_subscriber import MQTTSubscriber

#Lancement des acteurs
#servo_actor = ServoMotorActor.start(pin=11)
#rfid_actor = RFIDReaderActor.start(servo_actor)
led_actor = LedActor.start()
led_actor.tell({'command':'montagne'})
map_actor = MapActor.start()
sound_actor = SoundActor.start()
#mqtt_subscriber = MQTTSubscriber("138.48.254.33", 1883, "SmartRPG", "SmartRPG", "channel_ambiances")


#Le livre doit avoir en paramètre les leds, le baffle, la map
#book_actor = BookActor.start(led_actor, sound_actor, map_actor, mqtt_subscriber)
#mqtt_subscriber.start()
#Le dé a accès au baffle et aux lumières
dice_actor = DiceActor.start(led_actor, sound_actor)


async def notification_callback(number, stability_descriptor): #dice_actor
        """ 
        GoDice number notification callback.
        Called each time GoDice is flipped, receiving flip event data:
        :param number: a rolled number
        :param stability_descriptor: an additional value clarifying device movement state, ie stable, rolling...
        """
        print(f"Dice value: {number}, stability descriptor: {stability_descriptor}")
        # Envoyer un message à l'acteur Pykka pour traiter l'événement
        #dice_actor.tell({'command': 'mauvais' if number == 1 else 'excellent' == 6 else 'neutre'})
        if number == 1:
            led_actor.tell({'command':'mauvais'})
        elif number == 6:
            led_actor.tell({'command':'excellent'})
        else : 
            led_actor.tell({'command' : 'neutre'})


def filter_godice_devices(dev_advdata_tuples):
    """
    Receives all discovered devices and returns only GoDice devices
    """
    return [
        (dev, adv_data)
        for dev, adv_data in dev_advdata_tuples
        if (dev.name and dev.name.startswith("GoDice"))
    ]

def print_device_info(devices):
    """
    Prints summary of discovered Godice devices
    """
    for dev, adv_data in devices:
        print(f"Name : {dev.name}, Address : {dev.address}, rssi : {adv_data.rssi}")

def select_closest_device(dev_advdata_tuples): # à changer car un seul dé est utilisé
    """
    Finds the closest device based on RSSI are returns it
    """
    def _rssi_as_key(dev_advdata):
        _, adv_data = dev_advdata
        return adv_data.rssi
    return max(dev_advdata_tuples, key=_rssi_as_key)


async def main():
    print("Searching for GoDice devices...")
    discovery_res = await bleak.BleakScanner.discover(timeout=10, return_adv=True)
    dev_advdata_tuples = discovery_res.values()
    dev_advdata_tuples = filter_godice_devices(dev_advdata_tuples)

    print("Godice devices found :")
    print_device_info(dev_advdata_tuples)

    print("Connecting to a closest device...")
    dev, _adv_data = select_closest_device(dev_advdata_tuples)
    client = bleak.BleakClient(dev, timeout=15)

    async with godice.create(client, godice.Shell.D6) as dice:
        print(f"Connected to {dev.name}")

            # Créer l'acteur Pykka pour gérer les événements du dé
            #led_actor = LedActor.start()
            #sound_actor = SoundActor.start()
            #dice_actor = DiceActor.start(led_actor, sound_actor)

        blue_rgb = (0, 0, 255)
        yellow_rgb = (255, 255, 0)
        off_rgb = (0, 0, 0)
        orange_rgb = (255,68,51)


        await dice.set_led(orange_rgb, yellow_rgb)

        colour = await dice.get_color()
        battery_level = await dice.get_battery_level()
        print(f"Colour: {colour}")
        print(f"Battery level: {battery_level}")

        print("Listening to position updates. Move your dice")
        # Passer l'acteur Pykka à la fonction de rappel
        await dice.subscribe_number_notification(notification_callback) #lambda num, descr: notification_callback(num, descr, dice_actor)
        await asyncio.sleep(100)
        await dice.set_led(off_rgb, off_rgb)

asyncio.run(main())

#Démarrer la lecture de tags RFID
#rfid_actor.tell({'command': 'start_reading'})
