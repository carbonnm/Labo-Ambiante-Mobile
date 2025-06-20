import paho.mqtt.client as mqtt

class MQTTSubscriber:
    def __init__(self, server, port, username, password, channel):
        self.mqtt_server = server
        self.mqtt_port = port
        self.username = username
        self. password = password
        self.channel = channel

        # Create a MQTT client instance
        self.client = mqtt.Client()
        self.client.username_pw_set(username, password)

        # Set the callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.callback = None

        # Connect to the broker
        self.client.connect(self.mqtt_server, self.mqtt_port, 60)

    def set_callback(self, callback):
        """
        Set the callback function for handling received messages.
        """
        self.callback = callback

    def on_connect(self, client, userdata, flag, rc):
        """
        Callback function when the client connects to the MQTT broker.
        """
        print("Connected with result code "+str(rc))
        client.subscribe(self.channel)

    def on_message(self, client, userdata, message):
        """
        Callback function when a PUBLISH message is received from the server.
        """
        payload = message.payload.decode('utf-8')
        try:
            payload_dict = eval(payload)  # Assuming payload is a dictionary
            if self.callback:
                self.callback(payload_dict)
        except Exception as e:
            print(f"Error decoding message: {e}")

    def start(self):
        """
        Start the MQTT client loop (blocking call).
        """
        self.client.loop_forever()
