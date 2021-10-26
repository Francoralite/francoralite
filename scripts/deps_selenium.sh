#!/bin/bash

apt update

# Install web browser Firefox
apt install -y firefox-esr

# Install wget
apt install wget

# Install Gecko driver
export GECKO_DRIVER_VERSION='v0.29.1'
wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
tar -xvzf geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
rm geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/local/bin/
rm geckodriver