#!/usr/local/bin/python

from mqtt_fiware_bridge import MFB


class MockBridge(MFB.MqttFiwareBridge):

    def __init__(self, **kwargs):
        super(MockBridge, self).__init__(**kwargs)

    def do_something(self, message):
        self.log.info(f"Printing validated message from {__name__}")
        print(f"Voila: {message}")


if __name__ == "__main__":
    mocker_client = MockBridge()

    mocker_client.connect()
