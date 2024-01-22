from pykka import * 
import asyncio
import bleak
import godice


class DiceActor(ThreadingActor):

    def __init__(self, led_actor, sound_actor): 
        super(DiceActor, self).__init__()
        self.led_actor = led_actor
        self.sound_actor = sound_actor
       

    def on_receive(self, message):
        """
        Lorsqu'un jet critique mauvais ou excellent a lieu, ceci a une incidence sur les leds et sur les baffles 
        Parameters:  
        self: current instance of the class
        """

        if message == "mauvais":
            self.sound_actor.tell({'command': 'mauvais'})
            self.led_actor.tell({'command': 'mauvais'})
        
        if message == "excellent":
            self.sound_actor.tell({'command': 'excellent'})
            self.led_actor.tell({'command': 'excellent'})

        if message == "neutre":
            self.sound_actor.tell({'command': 'neutre'})
            self.led_actor.tell({'command': 'neutre'})


    
    async def notification_callback(self, number, stability_descriptor): 
        """ 
        GoDice number notification callback.
        Called each time GoDice is flipped, receiving flip event data:
        Parameters:
        self: current instance of the class
        number: a rolled number
        stability_descriptor: an additional value clarifying device movement state, ie stable, rolling...
        """
        print(f"Dice value: {number}, Stability descriptor: {stability_descriptor}")
        # Envoyer un message à l'acteur Pykka pour traiter l'événement
        if number == 1:
            self.on_receive("mauvais")
        elif number == 6:
            self.on_receive("excellent")
        else : 
            self.on_receive("neutre")


    def filter_godice_devices(self, dev_advdata_tuples):
        """
        Receives all discovered devices and returns only GoDice devices
        Parameters:
        self: current instance of the class
        dev_advdata_tuples: tuples of devices informations
        """
        return [
            (dev, adv_data)
            for dev, adv_data in dev_advdata_tuples
            if (dev.name and dev.name.startswith("GoDice"))
        ]

    def print_device_info(self, devices):
        """
        Prints summary of discovered Godice devices
        Parameters:
        self: current instance of the class
        devices: list of Godice devices
        """
        for dev, adv_data in devices:
            print(f"Name : {dev.name}, Address : {dev.address}, rssi : {adv_data.rssi}")

    def select_closest_device(self, dev_advdata_tuples): 
        """
        Finds the closest device based on RSSI are returns it
        Parameters:
        self: current instance of the class
        dev_advdata_tuples: tuples of devices informations
        """
        def _rssi_as_key(dev_advdata):
            _, adv_data = dev_advdata
            return adv_data.rssi
        return max(dev_advdata_tuples, key=_rssi_as_key)


    async def main(self):
        print("Searching for GoDice devices...")
        discovery_res = await bleak.BleakScanner.discover(timeout=10, return_adv=True)
        dev_advdata_tuples = discovery_res.values()
        dev_advdata_tuples = self.filter_godice_devices(dev_advdata_tuples)

        print("Godice devices found :")
        self.print_device_info(dev_advdata_tuples)

        print("Connecting to a closest device...")
        dev, _adv_data = self.select_closest_device(dev_advdata_tuples)
        client = bleak.BleakClient(dev, timeout=15)

        async with godice.create(client, godice.Shell.D6) as dice:
            print(f"Connected to {dev.name}")


            yellow_rgb = (255, 255, 0)
            off_rgb = (0, 0, 0)
            orange_rgb = (255,68,51)


            await dice.set_led(orange_rgb, yellow_rgb)

            colour = await dice.get_color()
            battery_level = await dice.get_battery_level()
            print(f"Colour: {colour}")
            print(f"Battery level: {battery_level}")

            await asyncio.sleep(5)
            await dice.set_led(off_rgb, off_rgb)

            print("Listening to position updates. Move your dice")
            
            # Passer l'acteur Pykka à la fonction de rappel
            await dice.subscribe_number_notification(self.notification_callback) 
            await asyncio.sleep(100)
            await dice.set_led(off_rgb, off_rgb)


