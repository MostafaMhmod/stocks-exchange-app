import os

from channels.routing import ProtocolTypeRouter, ChannelNameRouter

from thndr.consumers import MqttConsumer
from channels.layers import get_channel_layer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thndr.settings')


application = ProtocolTypeRouter({
    'channel': ChannelNameRouter(
        {
            "mqtt": MqttConsumer
        }
    )
})

# Layers
channel_layer = get_channel_layer()
