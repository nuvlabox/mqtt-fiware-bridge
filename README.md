# mqtt-fiware-bridge
Optional NuvlaBox component that consumes data from a specified MQTT broker and topic, double checks the data structure against FIWARE's data schemas, and sends data to a specified endpoint


# How it works

At its core, the basic deployment of this component is achieved by:

```bash
docker run --rm --network <mqtt-broker-network> nuvlabox/mqtt-fiware-bridge:<tag> --mqtt-host <mqtt.broker> --mqtt-topic <topic>
```

where:
 - **mqtt-broker-network**: is the Docker network where your MQTT broker container is running. **This is only applicable** if you are collecting the MQTT messages from your local container cluster. If the MQTT broker is reachable via IP or DNS name, then you can ditch the `--network` argument
 - **tag**: the Docker image tag
 - **mqtt.broker**: the endpoint for the MQTT broker
 - **topic**: the MQTT topic to subscribe to
 
**At the moment**, this image is simply taking MQTT messages, validating them through FIWARE, and printing them if successful. 

**TODO**: _Output connectors will be coming soon_


## Inheriting this module

If you'd like to build your own bridge, you can base your own Docker image on this one:

 1. build your Dockerfile with `FROM nuvlabox/mqtt-fiware-bridge:<tag>`
 2. make sure you set your own `ENTRYPOINT` to replace this image's default one
 3. your entrypoint script must inherit the _mqtt_fiware_bridge_'s `MFB.MqttFiwareBridge` class. For example (as in _code/main.py_)
    
    ```python
    from mqtt_fiware_bridge import MFB

    class YourBridge(MFB.MqttFiwareBridge):
        def __init__(self, **kwargs):
            super(YourBridge, self).__init__(**kwargs)
    ```
 4. you **should** override the `do_something` abstract method, to meet your needs. This method is executed everytime there's a new MQTT message, after it is validated successfully against FIWARE. So your class from above becomes:

    ```python
    from mqtt_fiware_bridge import MFB

    class YourBridge(MFB.MqttFiwareBridge):
        def __init__(self, **kwargs):
            super(YourBridge, self).__init__(**kwargs)
            
        def do_something(self, message):
            # do whatever you want with the message here...
            # it has already been validated
    ```
    
 5. finally, from your main application, simply instantiate _YourBridge_ class, and `connect()` to subscribe to the MQTT broker and start listening to messages indefinitely
 
    ```python
    your_client = YourBridge()

    your_client.connect()
    # endless loop
    ``` 
  
