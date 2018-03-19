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
In you application bundle, inject the mqtt bundle

```python
import inject
import paho.mqtt.client as mqtt
import zope.event.classhandler
from mqtt_bundle import MqttMessageEvent

c = inject.instance(mqtt.Client)
# Puslish a message
c.publish("/myTopic", "myMessagePayload")

# Subscribe
c.subscribe("/testTopic")

# Listen for events
def message_handler(event):
   print(event.message)
   print(event.client)
   print(event.userdata)
      
zope.event.classhandler.handler(MqttMessageEvent, message_handler)

# Another dummy consumer
zope.event.classhandler.handler(MqttMessageEvent, lambda m: print("Message received", m.message.payload))
```

Everytime a message is received to a subscribed channel, the event MqttMessageEvent is
thrown so you can subscribe just once and then receive messages in many consumers

Going deeper
------------
This bundle use paho-mqtt so you can find more information and details at their documentation [https://pypi.python.org/pypi/paho-mqtt]()