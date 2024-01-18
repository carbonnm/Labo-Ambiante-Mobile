#!/bin/bash

# Update and upgrade system
sudo apt update
sudo apt upgrade -y

# Install coursier
curl -fL https://github.com/VirtusLab/coursier-m1/releases/latest/download/cs-aarch64-pc-linux.gz | gzip -d > cs && chmod +x cs && ./cs setup

# Add sbt repository
echo "deb https://repo.scala-sbt.org/scalasbt/debian all main" | sudo tee /etc/apt/sources.list.d/sbt.list
echo "deb https://repo.scala-sbt.org/scalasbt/debian /" | sudo tee /etc/apt/sources.list.d/sbt_old.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo apt-key add
sudo apt-get update
sudo apt-get install -y sbt

# Install Python packages
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel --break-system-packages
sudo python3 -m pip install --force-reinstall rpi_ws281x adafruit-circuitpython-neopixel adafruit-blinka --break-system-packages

# Clone the Git repository
mkdir -p ~/Projects
cd ~/Projects
git clone -b clean https://github.com/carbonnm/Labo-Ambiante-Mobile.git

echo "Setup completed successfully!"

