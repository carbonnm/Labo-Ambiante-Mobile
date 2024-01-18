import paho.mqtt.publish as publish
import time

MQTT_SERVER = "192.168.0.238"
MQTT_PORT = 1883
MQTT_PATH = "test_channel"

username = "SmartRPG"
password = "SmartRPG"

while True:
    publish.single(MQTT_PATH, "Hello MQTT CLIENT", hostname=MQTT_SEVER, port=MQTT_PORT, auth={'username': username, 'password': password})
    time.sleep(1)
