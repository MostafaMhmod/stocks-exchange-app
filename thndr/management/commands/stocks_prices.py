from django.core.management.base import BaseCommand

import paho.mqtt.client as mqtt
import json
from datetime import datetime
from thndr.models import Stock
from django.db import IntegrityError
import pytz
import docker


def _on_connect(client, userdata, rc, properties=None):
    client.subscribe("thndr-trading")


def _on_message(client, userdata, msg):
    print(msg.payload.decode())
    stock = json.loads(msg.payload.decode())
    stock_id = stock.get('stock_id')
    stock_name = stock.get('name')
    stock_availability = stock.get('availability')
    stock_price = stock.get('price')
    stock_timestamp = stock.get('timestamp')

    try:
        stock_timestamp = datetime.strptime(stock_timestamp, '%Y-%m-%d %H:%M:%S.%f')
        stock_timestamp = pytz.utc.localize(stock_timestamp)
    except ValueError:
        return
    try:
        Stock.objects.create(stock_uuid=stock_id, name=stock_name, quantity=stock_availability, price=stock_price)
    except IntegrityError:
        try:
            stock = Stock.objects.get(stock_uuid=stock_id)
            stock.name = stock_name
            stock.quantity = stock_availability
            stock.price = stock_price
            stock.modified_at = stock_timestamp
            stock.save()
        except Stock.DoesNotExist:
            return


class Command(BaseCommand):
    help = "gets all stocks from the MQTT messeging service"

    def handle(self, *args, **options):
        client = mqtt.Client()
        client.on_connect = _on_connect
        client.on_message = _on_message

        # getting the IP of the mqtt service
        docker_client = docker.DockerClient()
        container = docker_client.containers.get("thndr_vernemq_1")
        ip_add = container.attrs['NetworkSettings']['Networks']['thndr_default']['IPAddress']

        client.connect(ip_add, 1883, 60)

        # Blocking call that processes network traffic, dispatches callbacks and
        # handles reconnecting.
        # Other loop*() functions are available that give a threaded interface and a
        # manual interface.
        client.loop_forever()
