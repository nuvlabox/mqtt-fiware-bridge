#!/usr/local/bin/python

from mqtt_fiware_bridge import MFB

client = MFB.MqttFiwareBridge()

client.connect()