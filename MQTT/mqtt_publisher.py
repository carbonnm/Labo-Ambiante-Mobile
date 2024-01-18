import paho.mqtt.publish as publish

class MQTTPublisher:
    def __init__(self, server, port, username, password, channel):
        self.mqtt_server = server
        self.mqtt_port = port
        self.username = username
        self.password = password
        self.default_channel = channel

    def publish_message(self, message, channel=None):
        """
        Publishes a message to the specified channel or the default channel if not provided.
        """
        if channel is None:
            channel = self.default_channel

        publish.single(channel, message, hostname=self.mqtt_server, port=self.mqtt_port, auth={'username': self.username, 'password': self.password})

if __name__ == "__main__":
    mqtt_publisher = MQTTPublisher("192.168.0.238", 1883, "SmartRPG", "SmartRPG", "test_channel")

    while True:
        mqtt_publisher.publish_message("Class OK")
