from django.core.management.base import BaseCommand

import paho.mqtt.client as mqtt


def _on_connect(client, userdata, rc, properties=None):
    client.subscribe("thndr-trading")


def _on_message(client, userdata, msg):
    print(msg.payload.decode())


class Command(BaseCommand):
    help = "gets all stocks from the MQTT messeging service"

    def handle(self, *args, **options):
        client = mqtt.Client()
        client.on_connect = _on_connect
        client.on_message = _on_message

        client.connect("172.21.0.2", 1883, 60)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()
