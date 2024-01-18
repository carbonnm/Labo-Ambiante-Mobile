#!/bin/bash

# Update and upgrade system
sudo apt update
sudo apt upgrade -y

# Install Mosquitto MQTT broker and clients
sudo apt-get install -y mosquitto mosquitto-clients

# Install Python packages
sudo pip3 install -y rpi_ws281x adafruit-circuitpython-neopixel --break-system-packages
sudo python3 -m pip install -y --force-reinstall rpi_ws281x adafruit-circuitpython-neopixel adafruit-blinka paho-mqtt keyboard --break-system-packages

# Clone the Git repository
mkdir -p ~/App
cd ~/App
git clone -b clean https://github.com/carbonnm/Labo-Ambiante-Mobile.git

echo "Setup completed successfully!"

