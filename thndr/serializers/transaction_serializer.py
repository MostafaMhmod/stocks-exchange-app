from rest_framework import serializers

from thndr.models import Transaction
from thndr.serializers.user_serializer import NestedUserSerializer
from thndr.serializers.stock_serializer import StockRetrieveSerializer
from thndr.utils.get_user_balance import get_user_balance
from thndr.exceptions.negative_balance import NegativeBalanceAPIException


class TransactionCreateSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(required=True)
    stock = serializers.IntegerField(required=False)
    amount = serializers.IntegerField(min=1, required=True)
    is_wallet = serializers.BooleanField(required=True)
    is_stock = serializers.BooleanField(required=True)
    is_withdraw = serializers.BooleanField(required=True)
    is_deposit = serializers.BooleanField(required=True)

    def validate(self, attrs):
        if attrs['is_withdraw']:
            # check if balance allows it
            balance = get_user_balance(attrs['user'])
            new_balance = balance - attrs['amount']
            if new_balance < 0:
                raise NegativeBalanceAPIException

        return super().validate(attrs)

    class Meta:
        model = Transaction
        fields = ('user', 'stock', 'amount', 'is_wallet', 'is_stock')
