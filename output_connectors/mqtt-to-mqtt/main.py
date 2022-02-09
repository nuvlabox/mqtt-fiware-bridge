#!/usr/local/bin/python

import argparse
import paho.mqtt.client as mqtt
import socket
from mqtt_fiware_bridge import MFB


class MQTT2MQTT(MFB.MqttFiwareBridge):
    def __init__(self):
        super(MQTT2MQTT, self).__init__(program_name="MQTT to MQTT Bridge")

        self.out_connector = self.connect_out()

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
        self.args.add_argument('--publish-to-mqtt-port', dest='publish_mqtt_port',
                               metavar='MQTT PORT TO PUBLISH TO', default='1883')
        self.args.set_defaults(ignore_fiware_validation=True)

        return self.args

    def connect_out(self) -> mqtt.Client:
        """ Connect to the output MQTT broker """

        self.log.info(f"Connecting to output MQTT broker at {self.args.publish_mqtt_host}")

        client = mqtt.Client("mqtt-to-mqtt")

        try:
            client.connect(self.args.publish_mqtt_host, port=int(self.args.publish_mqtt_port))
        except (socket.gaierror, socket.timeout):
            self.log.exception(f"Cannot connect to the provided output MQTT host {self.args.publish_mqtt_host}")

        return client

    def do_something(self, message):
        self.log.info(f"Sending message {message} to {self.args.publish_mqtt_host} on {self.args.publish_mqtt_topic}")
        self.out_connector.publish(self.args.publish_mqtt_topic, payload=message)


if __name__ == "__main__":
    bridge_client = MQTT2MQTT()

    bridge_client.connect()
