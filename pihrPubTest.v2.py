# python2.7.15
# Simple program to test docker containerization of DL's (codename Pihr) Energy Ecosystem.
# Author: David Lawrence & Steve Hinkel
# Copyright: Duke Energy Corp
#
# Prerequisite installations:
# 1. sudo pip install paho-mqtt
# 
# Change Log:
# 1. 2019.11.26 - Initial program
# 2. 2019.12.03 - Fixed Topic pihr/test/ to be pihr/test
#
# 
# ---------------------------
# imports
import time
import paho.mqtt.client as mqtt  # import the client

# ----------------------------
# Global vars
sBrokerAddress = "192.168.101.2"
sClientID = "D2"	# ClientID must be unique for each client

# ----------------------------
# setup 
client = mqtt.Client(sClientID)  # create new instance
print("Connecting to Broker")
res = client.connect(sBrokerAddress)  # connect to broker
print(str(res))

# ----------------------------
# setup 
print("Publishing Topic message", sClientID)
while True:
    print(client.publish("pihr/test", "helloWorldTestYak"))
    time.sleep(10)
