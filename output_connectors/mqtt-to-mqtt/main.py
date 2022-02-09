#!/usr/local/bin/python

import argparse
import paho.mqtt.client as mqtt
from mqtt_fiware_bridge import MFB


class MQTT2MQTT(MFB.MqttFiwareBridge):
    def __init__(self):
        super(MQTT2MQTT, self).__init__(program_name="MQTT to MQTT Bridge")

    def extra_arguments(self) -> argparse.ArgumentParser:
        """
        Takes the existing parser and adds new args required for this connector

        :param parser: existing parser
        :return: updated parser
        """
        self.args.add_argument('--publish-to-mqtt-host', dest='publish_mqtt_host',
                            metavar='MQTT BROKER HOSTNAME TO PUBLISH TO', required=True)
        self.args.add_argument('--publish-to-mqtt-topic', dest='publish_mqtt_topic',
                            metavar='MQTT TOPIC TO PUBLISH TO', required=True)
        self.args.set_defaults(ignore_fiware_validation=True)

        return self.args

    def do_something(self, message):
        self.log.info(f"Printing validated message from {__name__}")
        print(f"Voila: {message}")


if __name__ == "__main__":
    bridge_client = MQTT2MQTT()

    bridge_client.connect()