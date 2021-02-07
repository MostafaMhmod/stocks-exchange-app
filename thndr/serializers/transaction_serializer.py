from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import NotAcceptable
from thndr.exceptions.negative_balance import NegativeBalanceAPIException
from thndr.exceptions.price_out_of_bounds import PriceOutOfBoundsAPIException
from thndr.models import Transaction
from thndr.models.stock import Stock
from thndr.utils.get_user_wallet_balance import get_user_wallet_balance
from thndr.utils.get_user_stocks_balance import get_user_stocks_balance


class TransactionWalletCreateSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(required=True)
    stock = serializers.IntegerField(required=False)
    amount = serializers.IntegerField(min_value=1, required=True)
    withdraw = serializers.BooleanField(required=True)
    deposit = serializers.BooleanField(required=True)

    def create(self, validated_data):
        validated_data['user'] = get_object_or_404(User, pk=validated_data['user'])

        if validated_data["withdraw"]:
            # check if balance allows it
            balance = get_user_wallet_balance(validated_data['user'].pk)
            new_balance = balance - validated_data['amount']
            if new_balance < 0:
                raise NegativeBalanceAPIException

        return super().create(validated_data)

    class Meta:
        model = Transaction
        fields = ('user', 'stock', 'amount', 'withdraw',
                  'deposit')


class TransactionStockCreateSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(required=True)
    stock = serializers.CharField(required=False)
    amount = serializers.IntegerField(min_value=1, required=False)
    withdraw = serializers.BooleanField(required=True)
    deposit = serializers.BooleanField(required=True)

    def validate(self, attrs):
        upper_bound = self.context.get('upper_bound')
        lower_bound = self.context.get('lower_bound')
        if not (type(upper_bound) == int or type(lower_bound) == int):
            raise NotAcceptable
        return super().validate(attrs)

    def create(self, validated_data):
        user = get_object_or_404(User, pk=validated_data['user'])
        stock = get_object_or_404(Stock, pk=validated_data['stock'])
        total = validated_data['stocks_total']
        upper_bound = self.context.get('upper_bound')
        lower_bound = self.context.get('lower_bound')

        user_wallet_balance = get_user_wallet_balance(user.pk)
        user_stocks_balance = get_user_stocks_balance(user.pk, stock.pk)
        order_total = stock.price * total

        if stock.price < lower_bound or stock.price > upper_bound:
            raise PriceOutOfBoundsAPIException

        if validated_data["deposit"]:
            if user_wallet_balance < order_total:
                raise NegativeBalanceAPIException
            if stock.quantity < total:
                raise NegativeBalanceAPIException

        elif validated_data["withdraw"]:
            if user_stocks_balance < total:
                raise NegativeBalanceAPIException

        validated_data['user'] = user
        validated_data['stock'] = stock
        validated_data['amount'] = order_total
        validated_data['stocks_total'] = total

        return super().create(validated_data)

    class Meta:
        model = Transaction
        fields = ('user', 'stock', 'amount', 'stocks_total', 'withdraw',
                  'deposit')
