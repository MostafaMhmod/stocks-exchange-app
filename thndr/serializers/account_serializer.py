from rest_framework import serializers

from thndr.models import Holding


class HoldingRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holding
        fields = ("pk", 'user', 'stock', 'quantity')
