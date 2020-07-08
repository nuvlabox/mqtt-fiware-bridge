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
import fastjsonschema
import json
import pkg_resources
import paho.mqtt.client as mqtt
from abc import abstractmethod

socket.setdefaulttimeout(30)


class MqttFiwareBridge(object):
    def __init__(self, ):
        self.this_package_name = "mqtt_fiware_bridge"

        self.set_logger(self.this_package_name)
        self.log = logging.getLogger(self.this_package_name)

        self.args = self.arguments(self.this_package_name).parse_args()

        self.pkg_fiware_specs = 'fiware/specs'
        self.fiware_schema_filename = 'schema.json'

        self.fiware_models = self.map_all_fiware_models(self.pkg_fiware_specs)

    @staticmethod
    def set_logger(logger_name):
        """ Configures logging """
        # give logger a name: app
        root = logging.getLogger(logger_name)
        root.setLevel(logging.DEBUG)

        # print to console
        c_handler = logging.StreamHandler(sys.stdout)
        c_handler.setLevel(logging.DEBUG)

        # format log messages
        formatter = logging.Formatter('%(levelname)s - %(funcName)s - %(message)s')
        c_handler.setFormatter(formatter)

        # add handlers
        root.addHandler(c_handler)

    @staticmethod
    def arguments(description):
        """ Builds a generic argparse

        :return: parser
        """

        parser = argparse.ArgumentParser(description=description)
        parser.add_argument('--mqtt-host', dest='mqtt_host', metavar='MQTT BROKER HOSTNAME', required=True)
        parser.add_argument('--mqtt-topic', dest='mqtt_topic', metavar='MQTT TOPIC', required=True)
        parser.add_argument('--output-connector', dest='connector', default=None, metavar='CONNECTOR NAME')
        parser.add_argument('--output-endpoint', dest='output_endpoint', default=None, metavar='ENDPOINT')

        return parser

    def map_all_fiware_models(self, search_at):
        """ Generates a list of keypairs, containing the paths to all FIWARE data models

        Example: {'Alert': 'fiware/specs/Alert'} is the path where you can find the schema.json for the data model Alert
        """
        all_model_paths = {}

        listed_under = pkg_resources.resource_listdir(self.this_package_name, search_at)

        for item in listed_under:
            new_folder = f'{search_at}/{item}'
            if item == self.fiware_schema_filename:
                all_model_paths[search_at.split('/')[-1]] = search_at
            elif pkg_resources.resource_isdir(self.this_package_name, new_folder):
                all_model_paths.update(self.map_all_fiware_models(new_folder))
            else:
                continue

        return all_model_paths

    def fiware_validate(self, data):
        """ Takes the data and the list of fiware_data_type, and double checks against them all to
        see if the schema is correct """

        try:
            msg = json.loads(data)
        except json.decoder.JSONDecodeError:
            self.log.exception(f"Message {data} is not in JSON form and thus cannot be validated")
            return False

        # message needs to contain a top-level "type" attribute identifying the data model.
        # Otherwise it is straightaway NOT FIWARE compliant
        if "type" not in msg:
            self.log.warning(f"Message {msg} doesn't have a 'type' attribute, and thus is not FIWARE compliant")
            return False
        else:
            fiware_data_type = msg['type']

            if fiware_data_type in self.fiware_models:
                schema = f"{self.fiware_models[fiware_data_type]}/{self.fiware_schema_filename}"
                schema_json = json.loads(pkg_resources.resource_string(self.this_package_name, schema))
                validate = fastjsonschema.compile(schema_json)
                try:
                    validate(msg)
                    return True
                except fastjsonschema.exceptions.JsonSchemaException:
                    self.log.exception(f'The {fiware_data_type} message is not compliant with FIWARE: {msg}')
                    return False
            else:
                self.log.warning(f"The field 'type' ({fiware_data_type}) in the message {msg} is not a valid FIWARE "
                                 f"data type")
                return False

    @abstractmethod
    def do_something(self, message):
        # please redefine this function if you are inheriting this class
        pass

    def on_message(self, client, userdata, message):
        new_message = str(message.payload.decode("utf-8"))
        self.log.info(f"New message: {new_message}")
        self.log.info("Verifying FIWARE compliance...")
        if self.fiware_validate(new_message):
            self.log.info("Message is FIWARE compliant!")
            self.do_something(new_message)
        else:
            self.log.warning("Message validation failed...")

    def on_log(self, client, userdata, level, buf):
        self.log.info(f"MQTT log: {buf}")

    def connect(self):
        """ Connect to the MQTT broker and starts listening forever """

        self.log.info("Starting MQTT FIWARE bridge")

        client = mqtt.Client(self.this_package_name)

        try:
            client.connect(self.args.mqtt_host)
        except (socket.gaierror, socket.timeout):
            self.log.exception(f"Cannot connect to the provided MQTT host {self.args.mqtt_host}")

        client.on_message=self.on_message
        # client.on_log=self.on_log

        self.log.info(f"Subscribing to topic {self.args.mqtt_topic}")
        client.subscribe(self.args.mqtt_topic)

        client.loop_forever()
