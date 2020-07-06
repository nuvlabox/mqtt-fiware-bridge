#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""MQTT Fiware Bridge

This microservice is optional for the NuvlaBox.

It takes as arguments:
 - --mqtt-host: (mandatory) MQTT broker endpoint to connect to
 - --mqtt-topic: (mandatory) MQTT topic to be subscribed
 - --output-connector: (optional) From the available connectors, which one to use. If empty, all messages go to STDOUT
 - --output-endpoint: (optional) Endpoint for the service where to push the messages to. Needs OUTPUT_CONNECTOR

This component connects to one and only one MQTT topic from one MQTT broker.

For each message received, a schema validation is performed against the FIWARE data models.
If the received data structure is FIWARE compliant, then forward the message to the OUTPUT_ENDPOINT.

There are several connectors available to choose from:
 - disk: appends the messages to a text file located inside the container. The default path is /opt/nuvlabox/output.txt.
         This path can be overwritten by OUTPUT_ENDPOINT

"""

import socket
import logging
import sys
import argparse
import paho.mqtt.client as mqtt


this_client_name = "mqtt-fiware-bridge"


def set_logger():
    """ Configures logging """
    # give logger a name: app
    root = logging.getLogger(this_client_name)
    root.setLevel(logging.DEBUG)

    # print to console
    c_handler = logging.StreamHandler(sys.stdout)
    c_handler.setLevel(logging.DEBUG)

    # format log messages
    formatter = logging.Formatter('%(levelname)s - %(funcName)s - %(message)s')
    c_handler.setFormatter(formatter)

    # add handlers
    root.addHandler(c_handler)


set_logger()
log = logging.getLogger(this_client_name)


def arguments():
    """ Builds a generic argparse

    :return: parser
    """

    parser = argparse.ArgumentParser(description=this_client_name)
    parser.add_argument('--mqtt-host', dest='mqtt_host', metavar='MQTT BROKER HOSTNAME', required=True)
    parser.add_argument('--mqtt-topic', dest='mqtt_topic', metavar='MQTT TOPIC', required=True)
    parser.add_argument('--output-connector', dest='connector', default=None, metavar='CONNECTOR NAME')
    parser.add_argument('--output-endpoint', dest='output_endpoint', default=None, metavar='ENDPOINT')

    return parser


def on_message(client, userdata, message):
    new_message = str(message.payload.decode("utf-8"))
    log.info(f"New message: {new_message}")
    log.info("Verifying FIWARE ")


def on_log(client, userdata, level, buf):
    log.info(f"MQTT log: {buf}")


if __name__ == "__main__":
    log.info("Starting MQTT FIWARE bridge")

    args = arguments().parse_args()

    client = mqtt.Client(this_client_name)

    try:
        client.connect(args.mqtt_host)
    except (socket.gaierror, socket.timeout):
        log.exception(f"Cannot connect to the provided MQTT host {args.mqtt_host}")

    client.on_message=on_message
    client.on_log=on_log

    log.info(f"Subscribing to topic {args.mqtt_topic}")
    client.subscribe(args.mqtt_topic)

    client.loop_forever()
