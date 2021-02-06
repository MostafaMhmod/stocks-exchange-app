from rest_framework import serializers

from thndr.models import Account


class AccountBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("balance",)
