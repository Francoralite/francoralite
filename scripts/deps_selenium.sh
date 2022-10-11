#!/bin/bash

# Reactivation of the main buster depot via snapshot.debian.org for firefox-esr 78.14 (with the worst priority to maintain a better overall download speed)
grep '^deb .*snapshot.* buster ' /etc/apt/sources.list >/dev/null 2>&1 || echo -e '\ndeb http://snapshot.debian.org/archive/debian/20220228T000000Z buster main' >> /etc/apt/sources.list

apt update

# Install web browser Firefox
apt install -y firefox-esr=78.14.0esr-1~deb10u1

# Install wget
apt install wget

# Install Gecko driver
export GECKO_DRIVER_VERSION='v0.30.0'
wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
tar -xvzf geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
rm geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/local/bin/
rm geckodriver
