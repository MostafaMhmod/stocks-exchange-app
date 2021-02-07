from rest_framework import serializers

from thndr.models import Holding
from thndr.serializers.user_serializer import NestedUserSerializer
from thndr.serializers.stock_serializer import StockRetrieveSerializer


class HoldingWriteSerializer(serializers.ModelSerializer):
    # user = NestedUserSerializer(required=True)
    # stock = StockRetrieveSerializer(required=True)
    # quantity = StockRetrieveSerializer(required=True)

    class Meta:
        model = Holding
        fields = ('user', 'stock', 'quantity')
