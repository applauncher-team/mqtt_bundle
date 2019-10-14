# MQTT bundle for AppLauncher
MQTT support for applauncher

Installation
-----------
```bash
pip install mqtt_bundle 
```
Then add to your main.py
```python
import mqtt_bundle

bundle_list = [
    mqtt_bundle.MqttBundle(),
]
```

Configuration
-------------
```yml
mqtt:
  host: localhost
```

How to use
----------
Instead of handling the routing by yourself, the bundle offers a high level and simple to use topic/message handler.
Check this example to see it in action

```python
import inject
from mqtt_bundle import MqttTopicManager, MqttConnectEvent
from applauncher.kernel import Event

class MyEvent(Event):
    event_name = "my_event"
    topic = "my_topic"

    def __init__(self, payload):
        self.payload = payload

class MyBundle(object):
    def __init__(self):
        self.event_listeners = [
            (MqttConnectEvent, self.mqtt_ready),
        ]


    def mqtt_ready(self, event):
        print("MQTT READY")
        mtm = inject.instance(MqttTopicManager)  # type: MqttTopicManager
        mtm.subscribe(MyEvent, lambda m: print(m))
        # d = mtm.publish(MyEvent("My Message!"))
```
The usage is simple, just inject `MqttTopicManager` and subscribe to an event providing the consumer function. The
consumer function will receive the message payload.

To send a message just send and Event providing the payload. The payload can be anything serialized to str or bytes.

Going deeper
------------
You can also manage the mqtt connection using directly the paho client.
```python
import paho.mqtt.client as mqtt
import inject

client = inject.instance(mqtt.Client)
# Subscribe to a topic
client.subscribe("my_topic")

# Sending a message
client.publish("my_topic", "my_payload")
```
And for receive messages, just listen for `MqttMessageEvent`

So an example of a bundle using that would be:
```python
from mqtt_bundle import MqttMessageEvent, MqttConnectEvent
import paho.mqtt.client as mqtt
import inject

class MyBundle(object):

    def __init__(self):

        self.event_listeners = [
            (MqttMessageEvent, self.new_message),
            (MqttConnectEvent, self.on_connect),
        ]
        
    @inject.params(client=mqtt.Client)
    def on_connect(self, event, client):
        client.subscribe("my_topic")
        client.publish("status_topic", "IM IN")
        
    def new_message(self, event, client):
        message = event.message
        # message variable is a paho message object
        print(f"New message received in topic {message.topic}: {message.payload}")
```

The cilent object is a paho-mqtt client so you can find more information and details at their documentation [https://pypi.python.org/pypi/paho-mqtt]()