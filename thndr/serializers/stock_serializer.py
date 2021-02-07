from rest_framework import serializers

from thndr.models import Stock


class StockRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ('pk', 'stock_uuid', 'name', 'price', 'quantity')
