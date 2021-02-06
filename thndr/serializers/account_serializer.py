from rest_framework import serializers

from thndr.models import Account


class AccountRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("pk", 'user', 'stock', 'quantity')
