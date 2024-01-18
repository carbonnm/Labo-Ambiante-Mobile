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

        # Connect to the broker
        self.client.connect(self.mqtt_server, self.mqtt_port, 60)

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
        print(message.topic+" "+str(message.payload))

    def start(self):
        """
        Start the MQTT client loop (blocking call).
        """
        self.client.loop_forever()
