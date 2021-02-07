from rest_framework import serializers
from thndr.exceptions.negative_balance import NegativeBalanceAPIException

from thndr.models import Wallet


class WalletWriteSerializer(serializers.ModelSerializer):
    balance = serializers.IntegerField(min_value=1, required=True)

    def validate(self, attrs):
        if attrs['balance'] < 0:
            raise NegativeBalanceAPIException
        return super().validate(attrs)

    class Meta:
        model = Wallet
        fields = ('balance',)
